#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import pandas as pd
import random
import os
import smtplib
import tushare as ts
from email.mime.text import MIMEText
from pandas_datareader import data as pdr
import fix_yahoo_finance
import datetime

banknum='/lin/easybankPB/NeiBank/banknum.md'
#banknum='/Users/Linkding/Linkding.com/project.Linkding.com/easybankPB/NeiBank/test.md'
## collect data from yahoo finance
def collect():
    with open(banknum,'r') as f:
        for i in f.read().splitlines():
            url = 'http://table.finance.yahoo.com/table.csv?s=' + i +'.HK'
            filename = i + '.csv'
            urllib.urlretrieve (url, filename)

def collect_new():
    today = datetime.date.today()
    with open(banknum,'r') as f:
        for i in f.read().splitlines():
            tickers = i + '.HK'
            filename = i + '.csv'
            data2 = pdr.get_data_yahoo(tickers, start="2006-01-01", end=today)
            data2.sort_index(ascending=False).to_csv(filename)



## change pbvs to DataFrame
def change_dataframe():
    with open(banknum,'r') as f:
        for i in f.read().splitlines():
            filename1 = 'bookvalue' + i + '.txt'
            filename2 = 'bookvalue' + i + '.csv'
            x_0 = [x.strip().split(' ')[0] for x in open(filename1).readlines()]
            x_1 = [x.strip().split(' ')[1] for x in open(filename1).readlines()]
            x_2 = [x.strip().split(' ')[2] for x in open(filename1).readlines()]
            x_3 = [x.strip().split(' ')[3] for x in open(filename1).readlines()]
            x_4 = [x.strip().split(' ')[4] for x in open(filename1).readlines()]
            x_5 = [x.strip().split(' ')[5] for x in open(filename1).readlines()]
            x_6 = [x.strip().split(' ')[6] for x in open(filename1).readlines()]
            frame = list(zip(x_0,x_1,x_2,x_3,x_4,x_5,x_6))
            df = pd.DataFrame(data = frame, columns=['Codenumber','Name','Date','Bookvalue','Changerate','ROE','D_rate'])
            df.to_csv(filename2,index=False,header=True)

## merge two table(csv) to one result csv
def merge():
    with open(banknum,'r') as f:
            for i in f.read().splitlines():
                filename1 = i + '.csv'
                filename2 = 'bookvalue' + i + '.csv'
                filename3 = 'merge' + i + '.csv'
                stockdata = pd.read_csv(filename1)
                bookvalue = pd.read_csv(filename2)

                merge = pd.merge(stockdata, bookvalue, how='outer', on=['Date'])
                merge.sort_values('Date',ascending=False)


                index_num = []
                for i in bookvalue['Date']:
                    h = merge[merge.Date == i].index.tolist()
                    index_num.append(h)

                for i in range(len(index_num)):
                    i2 = i - 1
                    num1 = index_num[i][0]
                    num2 = index_num[i2][0]
                    if i == 0:
                        merge.loc[0:num1,'Bookvalue'] = merge['Bookvalue'][num1]
                        merge.loc[0:num1,'Name'] = merge['Name'][num1]
                        merge.loc[0:num1,'Codenumber'] = merge['Codenumber'][num1]
                        merge.loc[0:num1,'Changerate'] = merge['Changerate'][num1]
                        merge.loc[0:num1,'ROE'] = merge['ROE'][num1]
                        merge.loc[0:num1,'D_rate'] = merge['D_rate'][num1]
                    else:
                        merge.loc[num2:num1,'Bookvalue'] = merge['Bookvalue'][num1]
                        merge.loc[0:num1,'Name'] = merge['Name'][num1]
                        merge.loc[0:num1,'Codenumber'] = merge['Codenumber'][num1]
                        merge.loc[num2:num1,'Changerate'] = merge['Changerate'][num1]
                        merge.loc[num2:num1,'ROE'] = merge['ROE'][num1]
                        merge.loc[num2:num1,'D_rate'] = merge['D_rate'][num1]

                merge['PB'] = merge['Close'] /( merge['Bookvalue'] / merge['Changerate'])
                merge['AV_ROE'] = merge['ROE'].mean()
                merge['E_yield'] = ((1 + (merge['AV_ROE']* merge['D_rate']) / (merge['PB'] - merge['AV_ROE'] * merge['D_rate'])) * (1 + merge['AV_ROE'] * (1 - merge['D_rate']))) - 1
                #merge.columns=[]
                merge.round(3).to_csv(filename3,index=False,header=True)

## collect every lasted pb data
def collect_pb():
    frame = []
    with open(banknum,'r') as f:
            for i in f.read().splitlines():
                filename1 = 'merge' + i + '.csv'
                stockdata = pd.read_csv(filename1)
                line = stockdata[['Date','Codenumber','Name','Close','Bookvalue','Changerate','ROE','AV_ROE','D_rate','PB','E_yield']][:1]
                frame.append(line)
                result = pd.concat(frame)
                result.columns=['Date','Codenumber','Name','Close','Bookvalue','Changerate','ROE','AV_ROE','D_rate','PB','预期收益率']
            result.sort_values('PB').to_csv('hk_pb.csv',index=False,header=True)


def change_csv_html():
    os.system('python /lin/csv2html/csv2html/csv2html.py -o /lin/easybankPB/NeiBank/hk_pb.html /lin/easybankPB/NeiBank/hk_pb.csv')



if __name__ ==  "__main__":
        collect_new()
        change_dataframe()
        merge()
        collect_pb()
        change_csv_html()

#!/usr/bin/env python
import urllib
import pandas as pd
import random
import os
import smtplib
from email.mime.text import MIMEText

banknum='/Users/Linkding/Linkding.com/project.Linkding.com/easybankPB/banknum.md'

## collect data from yahoo finance
def collect():
    with open(banknum,'r') as f:
        for i in f.read().splitlines():
            url = 'http://table.finance.yahoo.com/table.csv?s=' + i +'.HK'
            filename = i + '.csv'
            urllib.urlretrieve (url, filename)

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
            frame = list(zip(x_0,x_1,x_2,x_3,x_4))
            df = pd.DataFrame(data = frame, columns=['Codenumber','Name','Date','bookvalue','changerate'])
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
                        merge.loc[0:num1,'bookvalue'] = merge['bookvalue'][num1]
                        merge.loc[0:num1,'Name'] = merge['Name'][num1]
                        merge.loc[0:num1,'Codenumber'] = merge['Codenumber'][num1]
                        merge.loc[0:num1,'changerate'] = merge['changerate'][num1]
                    else:
                        merge.loc[num2:num1,'bookvalue'] = merge['bookvalue'][num1]
                        merge.loc[0:num1,'Name'] = merge['Name'][num1]
                        merge.loc[0:num1,'Codenumber'] = merge['Codenumber'][num1]
                        merge.loc[num2:num1,'changerate'] = merge['changerate'][num1]

                merge['PB'] = merge['Close'] /( merge['bookvalue'] / merge['changerate'])
                merge.to_csv(filename3,index=False,header=True)

## collect every lasted pb data
def collect_pb():
    frame = []
    with open(banknum,'r') as f:
            for i in f.read().splitlines():
                filename1 = 'merge' + i + '.csv'
                stockdata = pd.read_csv(filename1)
                line = stockdata[['Codenumber','Name','Date','bookvalue','changerate','PB']][:1]
                frame.append(line)
                result = pd.concat(frame)
            result.sort_values('PB').to_csv('hk_pb.csv',index=False,header=True)


if __name__ ==  "__main__":
#        collect()
#        change_dataframe()
        merge()
        collect_pb()

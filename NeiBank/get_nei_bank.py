#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import pandas as pd
import random
import os
import smtplib
from email.mime.text import MIMEText

def collect():
    with open('banknum_china.md','r') as f:
        for i in f.read().splitlines():
            if i[0] == '0' :
                url = 'http://table.finance.yahoo.com/table.csv?s=' + i +'.SZ'
                filename = i + '.csv'
                urllib.urlretrieve (url, filename)
            else:
                url = 'http://table.finance.yahoo.com/table.csv?s=' + i +'.SS'
                filename = i + '.csv'
                urllib.urlretrieve (url, filename)

def change_dataframe():
    with open('banknum_china.md','r') as f:
        for i in f.read().splitlines():
            filename1 = 'bookvalue' + i + '.txt'
            filename2 = 'bookvalue' + i + '.csv'
            x_0 = [x.strip().split(' ')[0] for x in open(filename1).readlines()]
            x_1 = [x.strip().split(' ')[1] for x in open(filename1).readlines()]
            x_2 = [x.strip().split(' ')[2] for x in open(filename1).readlines()]
            x_3 = [x.strip().split(' ')[3] for x in open(filename1).readlines()]
            frame = list(zip(x_0,x_1,x_2,x_3))
            df = pd.DataFrame(data = frame, columns=['codenumber', 'name','Date','bookvalue'])
            df.to_csv(filename2,index=False,header=True)
def merge():
    with open('banknum_china.md','r') as f:
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
                        merge.loc[0:num1,'name'] = merge['name'][num1]
                        merge.loc[0:num1,'codenumber'] = merge['codenumber'][num1]
                    else:
                        merge.loc[num2:num1,'bookvalue'] = merge['bookvalue'][num1]
                        merge.loc[0:num1,'name'] = merge['name'][num1]
                        merge.loc[0:num1,'codenumber'] = merge['codenumber'][num1]

                merge['PB'] = merge['Close'] /( merge['bookvalue'])
#                merge['PB'].set_option('precision',3)
                merge.to_csv(filename3,index=False,header=True)

def collect_pb():
    frame = []
    with open('banknum_china.md','r') as f:
            for i in f.read().splitlines():
                filename1 = 'merge' + i + '.csv'
                stockdata = pd.read_csv(filename1)
                line = stockdata[['Date','codenumber','name','Close','bookvalue','PB']][:1]
                frame.append(line)
                result = pd.concat(frame)
            result.sort_values('PB').to_csv('nei_pb.csv',index=False,header=True)


def change_csv_html():
    os.system('sh /Users/Linkding/Linkding.com/project.Linkding.com/easybankPB/NeiBank/cvs2html.sh')

def send_mail():
        fp = open('nei_pb.html', 'r')

        msg = MIMEText(fp.read(),'html')
        # Create a text/plain message
        #msg = MIMEText(fp.read())
        fp.close()

        you = '619216759@qq.com'
        me = '13760613343@139.com'
        msg['Subject'] = '昨日的内银股PB排行'
        msg['From'] = me
        msg['To'] = you

        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP('smtp.139.com')
        s.login('13760613343','***')
        s.sendmail(me, [you], msg.as_string())
        s.quit()

if __name__ ==  "__main__":
#    collect()
#    change_dataframe()
#    merge()
#    collect_pb()
    change_csv_html()
    send_mail()
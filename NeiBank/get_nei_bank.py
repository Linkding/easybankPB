#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import pandas as pd
import random
import os
import smtplib
import tushare as ts
from email.mime.text import MIMEText

banknum_china='/lin/easybankPB/NeiBank/banknum_china.md'
#banknum_china='/Users/Linkding/Linkding.com/project.Linkding.com/easybankPB/NeiBank/banknum_china.md'
#maillist='/Users/Linkding/Linkding.com/project.Linkding.com/easybankPB/NeiBank/maillist.txt'
maillist='/lin/easybankPB/NeiBank/maillist.txt'


def collect():
    with open(banknum_china,'r') as f:
        for i in f.read().splitlines():
            if i[0] == '0' :
                url = 'http://table.finance.yahoo.com/table.csv?s=' + i +'.SZ'
                filename = i + '.csv'
                urllib.urlretrieve (url, filename)
            else:
                url = 'http://table.finance.yahoo.com/table.csv?s=' + i +'.SS'
                filename = i + '.csv'
                urllib.urlretrieve (url, filename)

def collect_new():
    with open(banknum_china,'r') as f:
        for i in f.read().splitlines():
                st = ts.get_hist_data(i)
                filename = i + '.csv'
                df = pd.DataFrame(data = st)
                df.to_csv(filename)

def change_dataframe():
    with open(banknum_china,'r') as f:
        for i in f.read().splitlines():
            filename1 = 'bookvalue' + i + '.txt'
            filename2 = 'bookvalue' + i + '.csv'
            x_0 = [x.strip().split(' ')[0] for x in open(filename1).readlines()]
            x_1 = [x.strip().split(' ')[1] for x in open(filename1).readlines()]
            x_2 = [x.strip().split(' ')[2] for x in open(filename1).readlines()]
            x_3 = [x.strip().split(' ')[3] for x in open(filename1).readlines()]
            x_4 = [x.strip().split(' ')[4] for x in open(filename1).readlines()]
            x_5 = [x.strip().split(' ')[5] for x in open(filename1).readlines()]
            frame = list(zip(x_0,x_1,x_2,x_3,x_4,x_5))
            df = pd.DataFrame(data = frame, columns=['codenumber','name','date','bookvalue','ROE','D_rate'])
            df.to_csv(filename2,index=False,header=True)
def merge():
    with open(banknum_china,'r') as f:
            for i in f.read().splitlines():
                filename1 = i + '.csv'
                filename2 = 'bookvalue' + i + '.csv'
                filename3 = 'merge' + i + '.csv'
                stockdata = pd.read_csv(filename1,error_bad_lines=False)
                bookvalue = pd.read_csv(filename2,error_bad_lines=False)

                merge = pd.merge(stockdata, bookvalue, how='outer', on=['date'])
                merge.sort_values('date',ascending=False)


                index_num = []
                for i in bookvalue['date']:
                    h = merge[merge.date == i].index.tolist()
                    index_num.append(h)

                for i in range(len(index_num)):
                    i2 = i - 1
                    num1 = index_num[i][0]
                    num2 = index_num[i2][0]
                    if i == 0:
                        merge.loc[0:num1,'bookvalue'] = merge['bookvalue'][num1]
                        merge.loc[0:num1,'name'] = merge['name'][num1]
                        merge.loc[0:num1,'codenumber'] = merge['codenumber'][num1]
                        merge.loc[0:num1,'ROE'] = merge['ROE'][num1]
                        merge.loc[0:num1,'D_rate'] = merge['D_rate'][num1]
                    else:
                        merge.loc[num2:num1,'bookvalue'] = merge['bookvalue'][num1]
                        merge.loc[0:num1,'name'] = merge['name'][num1]
                        merge.loc[0:num1,'codenumber'] = merge['codenumber'][num1]
                        merge.loc[num2:num1,'ROE'] = merge['ROE'][num1]
                        merge.loc[num2:num1,'D_rate'] = merge['D_rate'][num1]

                merge['PB'] = merge['close'] /( merge['bookvalue'])
                merge['AV_ROE'] = merge['ROE'].mean()
                merge['E_yield'] = ((1 + (merge['ROE']* merge['D_rate']) / (merge['PB'] - merge['AV_ROE'] * merge['D_rate'])) * (1 + merge['AV_ROE'] * (1 - merge['D_rate']))) - 1
#                merge['PB'].set_option('precision',3)
                merge.round(3).to_csv(filename3,index=False,header=True)

def collect_pb():
    frame = []
    with open(banknum_china,'r') as f:
            for i in f.read().splitlines():
                filename1 = 'merge' + i + '.csv'
                stockdata = pd.read_csv(filename1)
                line = stockdata[['date','codenumber','name','close','bookvalue','ROE','AV_ROE','D_rate','PB','E_yield']][:1]
                frame.append(line)
                result = pd.concat(frame)
                result.columns=['Date','codenumber','name','Close','bookvalue','ROE','AV_ROE','D_rate','PB','预期收益率']
            result.sort_values('PB').to_csv('nei_pb.csv',index=False,header=True)


def change_csv_html():
    os.system('sh /lin/easybankPB/NeiBank/cvs2html.sh')
    #os.system('sh /Users/Linkding/Linkding.com/project.Linkding.com/easybankPB/NeiBank/cvs2html.sh')
    os.system('cat /lin/easybankPB/NeiBank/hk_pb.html >>/lin/easybankPB/NeiBank/nei_pb.html')
    #os.system('cat /Users/Linkding/Linkding.com/project.Linkding.com/easybankPB/NeiBank/hk_pb.html >>/Users/Linkding/Linkding.com/project.Linkding.com/easybankPB/NeiBank/nei_pb.html')

def send_mail():
    pwd = os.getenv('MAIL_PW')
    mail_ser = os.getenv('MAIL_SER')
    mail_account = os.getenv('MAIL_account')
    sender = os.getenv('MAIL_SENDER')
    fp = open('nei_pb.html', 'r')
    msg = MIMEText(fp.read(),'html')
    # Create a text/plain message
    #msg = MIMEText(fp.read())
    fp.close()
    #with open(maillist,'r') as f:
    me = sender
    msg['Subject'] = '昨日银行股数据'
    msg['From'] = me
    #for i in f.read().splitlines():
    you1 = ['1105996033@qq.com','172055532@qq.com','1826994518@qq.com','254731853@qq.com','619216759@qq.com','389437787@qq.com','66210683@qq.com','770651456@qq.com','lf160@126.com']
    you2 = ['542627142@qq.com']
    #you1 = ['619216759@qq.com']
    #you2 = ['2413557718@qq.com']
    msg['To']=','.join(you1)
    #msg['To']= i
    #print msg['To']


    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP(mail_ser)
    s.login(mail_account,pwd)
    s.sendmail(me, you1, msg.as_string())
    s.sendmail(me, you2, msg.as_string())
    s.quit()

def update_into_mysql():
    os.system('sh /root/sh_dir/easypb_update_into_msyql.sh')

if __name__ ==  "__main__":
    collect_new()
    change_dataframe()
    merge()
    collect_pb()
    change_csv_html()
    send_mail()
#    update_into_mysql()

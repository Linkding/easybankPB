#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sns

merge0939 = pd.read_csv('merge0939.csv')
merge0998 = pd.read_csv('merge0998.csv')
merge1288 = pd.read_csv('merge1288.csv')
merge1398 = pd.read_csv('merge1398.csv')
merge1963 = pd.read_csv('merge1963.csv')
merge3328 = pd.read_csv('merge3328.csv')
merge3618 = pd.read_csv('merge3618.csv')
merge3988 = pd.read_csv('merge3988.csv')
merge6818 = pd.read_csv('merge6818.csv')

def every_bank():


    zhfront =  mpl.font_manager.FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc')
    fig, ax = plt.subplots(3,3,figsize=(22,15))


    #ax.set_yticks(np.arange(0, 2, 0.2))
    #ax.set_ylim(0,2)
    ax[0,0].set_yticks(np.arange(0, 2, 0.2))
    ax[0,0].set_ylim(0,2)
    ax[0,0].plot(merge0939['PB'],color='b',label=u'0939-建设银行H')
    ax[0,0].legend(prop=zhfront)

    ax[0,1].set_yticks(np.arange(0, 2, 0.2))
    ax[0,1].set_ylim(0,2)
    ax[0,1].plot(merge0998['PB'],color='r',label=u'0998-中信银行H')
    ax[0,1].legend(prop=zhfront)

    ax[0,2].set_yticks(np.arange(0, 2, 0.2))
    ax[0,2].set_ylim(0,2)
    ax[0,2].plot(merge1288['PB'],color='g',label=u'1288-农业银行')
    ax[0,2].legend(prop=zhfront)

    ax[1,0].set_yticks(np.arange(0, 2, 0.2))
    ax[1,0].set_ylim(0,2)
    ax[1,0].plot(merge1398['PB'],color='y',label=u'1398-工商银行H')
    ax[1,0].legend(prop=zhfront)

    ax[1,1].set_yticks(np.arange(0, 2, 0.2))
    ax[1,1].set_ylim(0,2)
    ax[1,1].plot(merge1963['PB'],color='brown',label=u'1963-重庆银行H')
    ax[1,1].legend(prop=zhfront)

    ax[1,2].set_yticks(np.arange(0, 2, 0.2))
    ax[1,2].set_ylim(0,2)
    ax[1,2].plot(merge3328['PB'],color='purple',label=u'3328-交通银行H')
    ax[1,2].legend(prop=zhfront)

    ax[2,0].set_yticks(np.arange(0, 2, 0.2))
    ax[2,0].set_ylim(0,2)
    ax[2,0].plot(merge3618['PB'],color='black',label=u'3618-重庆农村商业银行H')
    ax[2,0].legend(prop=zhfront)

    ax[2,1].set_yticks(np.arange(0, 2, 0.2))
    ax[2,1].set_ylim(0,2)
    ax[2,1].plot(merge3988['PB'],color='grey',label=u'3988-中国银行H')
    ax[2,1].legend(prop=zhfront)

    ax[2,2].set_yticks(np.arange(0, 2, 0.2))
    ax[2,2].set_ylim(0,2)
    ax[2,2].plot(merge6818['PB'],color='pink',label=u'6818-中国光大银行H')
    ax[2,2].legend(prop=zhfront);

    fig.tight_layout()
    fig.savefig('/Users/Linkding/screenshoot/everyHKbank.png')

def crontrast_bank():
    zhfront =  mpl.font_manager.FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc')
    fig, ax = plt.subplots(3,3,figsize=(22,15))


    #ax.set_yticks(np.arange(0, 2, 0.2))
    #ax.set_ylim(0,2)
    ax[0,0].set_yticks(np.arange(0, 2, 0.2))
    ax[0,0].set_ylim(0,2)
    ax[0,0].plot(merge0939['PB'],color='b',label=u'0939-建设银行H')
    ax[0,0].legend(prop=zhfront)

    ax[0,1].set_yticks(np.arange(0, 2, 0.2))
    ax[0,1].set_ylim(0,2)
    ax[0,1].plot(merge0998['PB'],color='r',label=u'0998-中信银行H')
    ax[0,1].legend(prop=zhfront)

    ax[0,2].set_yticks(np.arange(0, 2, 0.2))
    ax[0,2].set_ylim(0,2)
    ax[0,2].plot(merge1288['PB'],color='g',label=u'1288-农业银行')
    ax[0,2].legend(prop=zhfront)

    ax[1,0].set_yticks(np.arange(0, 2, 0.2))
    ax[1,0].set_ylim(0,2)
    ax[1,0].plot(merge1398['PB'],color='y',label=u'1398-工商银行H')
    ax[1,0].legend(prop=zhfront)

    ax[1,1].set_yticks(np.arange(0, 2, 0.2))
    ax[1,1].set_ylim(0,2)
    ax[1,1].plot(merge1963['PB'],color='brown',label=u'1963-重庆银行H')
    ax[1,1].legend(prop=zhfront)

    ax[1,2].set_yticks(np.arange(0, 2, 0.2))
    ax[1,2].set_ylim(0,2)
    ax[1,2].plot(merge3328['PB'],color='purple',label=u'3328-交通银行H')
    ax[1,2].legend(prop=zhfront)

    ax[2,0].set_yticks(np.arange(0, 2, 0.2))
    ax[2,0].set_ylim(0,2)
    ax[2,0].plot(merge3618['PB'],color='black',label=u'3618-重庆农村商业银行H')
    ax[2,0].legend(prop=zhfront)

    ax[2,1].set_yticks(np.arange(0, 2, 0.2))
    ax[2,1].set_ylim(0,2)
    ax[2,1].plot(merge3988['PB'],color='grey',label=u'3988-中国银行H')
    ax[2,1].legend(prop=zhfront)

    ax[2,2].set_yticks(np.arange(0, 2, 0.2))
    ax[2,2].set_ylim(0,2)
    ax[2,2].plot(merge6818['PB'],color='pink',label=u'6818-中国光大银行H')
    ax[2,2].legend(prop=zhfront);

    fig.tight_layout()
    fig.savefig('/Users/Linkding/screenshoot/everyHKbank.png')

def crontrast_bank2():

    fig, ax = plt.subplots(figsize=(40,20))
    zhfront =  mpl.font_manager.FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc')
    ax.set_xticks(np.arange(0, 1000, 50))
    ax.set_xlim(0,1000)
    ax.set_yticks(np.arange(0.3, 2, 0.05))
    ax.set_ylim(0.3,2)
    ax.set_ylabel(u'市净率',fontproperties=zhfront,fontsize=20)
    ax.plot(merge0939['PB'],color='b',label=u'0939-建设银行H')
    ax.plot(merge0998['PB'],color='r',label=u'0998-中信银行H')
    ax.plot(merge1288['PB'],color='g',label=u'1288-农业银行')
    ax.plot(merge1398['PB'],color='y',label=u'1398-工商银行H')
    ax.plot(merge1963['PB'],color='brown',label=u'1963-重庆银行H')
    ax.plot(merge3328['PB'],color='purple',label=u'3328-交通银行H')
    ax.plot(merge3618['PB'],color='black',label=u'3618-重庆农村商业银行H')
    ax.plot(merge3988['PB'],color='grey',label=u'3988-中国银行H')
    ax.plot(merge6818['PB'],color='pink',label=u'6818-中国光大银行H')

    ax.legend(prop=zhfront,loc='upper left')
    #mpl.rc('legend', fontsize=150)
    fig.savefig("/Users/Linkding/screenshoot/allHKbank2.png")

def crontrast_bank3():

    fig, ax = plt.subplots(figsize=(40,20))
    zhfront =  mpl.font_manager.FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc')
    ax.set_xticks(np.arange(0, 800, 100))
    ax.set_xlim(0,200)
    ax.set_yticks(np.arange(0.3, 2, 0.05))
    ax.set_ylim(0.3,2)
    ax.set_ylabel(u'市净率',fontproperties=zhfront,fontsize=20)
    ax.plot(merge0939['PB'],color='b',label=u'0939-建设银行H')
    ax.plot(merge0998['PB'],color='r',label=u'0998-中信银行H')
    ax.plot(merge1288['PB'],color='g',label=u'1288-农业银行')
    ax.plot(merge1398['PB'],color='y',label=u'1398-工商银行H')
    ax.plot(merge1963['PB'],color='brown',label=u'1963-重庆银行H')
    ax.plot(merge3328['PB'],color='purple',label=u'3328-交通银行H')
    ax.plot(merge3618['PB'],color='black',label=u'3618-重庆农村商业银行H')
    ax.plot(merge3988['PB'],color='grey',label=u'3988-中国银行H')
    ax.plot(merge6818['PB'],color='pink',label=u'6818-中国光大银行H')

    ax.legend(prop=zhfront,loc='upper left')

    fig.savefig("/Users/Linkding/screenshoot/allHKbank3.png")

def hight_low():
    with open('banknum.md','r') as f:
        minpb = []
        maxpb = []
        code = []
        for i in f.read().splitlines():
            mergedata = 'merge' + i
            filename = 'merge' + i + '.csv'
            mergedata = pd.read_csv(filename)
            code.append(i)
            minpb.append(mergedata.PB.min())
            maxpb.append(mergedata.PB.max())

    with open('bankname.md','r') as f:
        bankname = []
        for i in f.read().splitlines():
            bankname.append(i)

    min_max_data = list(zip(code,bankname,maxpb,minpb))
    minandmaxdata = pd.DataFrame(data=min_max_data,columns=['code','name','max','min'])

    n = len(minandmaxdata)
    X = np.arange(n)
    Y1 = minandmaxdata['max']
    Y2 = minandmaxdata['min']
    Y3 = minandmaxdata['code']

    for x,y,z in zip(X, Y1,Y3):
        Z = []
        z = 'u' + '"'+ z + '"'
        Z.append(z)

    fig,ax = plt.subplots(figsize=(15,5))
    zhfront =  mpl.font_manager.FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc')
    ax.bar(X,Y1,facecolor='#9999ff', edgecolor='white',label="max PB")
    ax.bar(X,-Y2,facecolor='#ff9999', edgecolor='white',label="min PB")

    for x, y in zip(X, Y1):
        ax.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va= 'bottom')


    for x, y, z in zip(X, Y1, Y3):
        ax.text(x + 0.4, y - 1,z, ha='center', va= 'bottom', fontproperties=zhfront)

    for x, y in zip(X, Y2):
        ax.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va= 'top')

    plt.xlim(0, n)
    plt.xticks(())
    plt.ylim(-1,5, 2)
    plt.yticks(())

    ax.legend()

    plt.show()
    fig.savefig('/Users/Linkding/screenshoot/max_min_PB.png')

if __name__ == '__main__':
    every_bank()
    crontrast_bank()
    crontrast_bank2()
    crontrast_bank3()
    hight_low()

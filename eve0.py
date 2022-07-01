# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 00:19:04 2022

@author: Acturus
"""

from astropy.io import fits;

import matplotlib.pyplot as plt;
import numppy as np;


x=[]

wl0={}
ir0={}
na0=['EVS_L2_2011046_00_007_02.fit.gz',
 'EVS_L2_2011221_07_007_02.fit.gz',
 'EVS_L2_2011249_21_007_02.fit.gz',
 'EVS_L2_2011250_21_007_02.fit.gz',
 'EVS_L2_2011265_10_007_02.fit.gz',
 'EVS_L2_2011267_08_007_02.fit.gz',
 'EVS_L2_2012028_17_007_02.fit.gz',
 'EVS_L2_2012065_03_007_02.fit.gz',
# 'EVS_L2_2012066_23_007_02.fit.gz',
 'EVS_L2_2012067_00_007_02.fit.gz',
 'EVS_L2_2012188_22_007_02.fit.gz',
 'EVS_L2_2012194_15_007_02.fit.gz',
 'EVS_L2_2013133_01_007_02.fit.gz',
 'EVS_L2_2013133_15_007_02.fit.gz',
 'EVS_L2_2013134_00_007_02.fit.gz',
 'EVS_L2_2013298_07_007_02.fit.gz',
 'EVS_L2_2013298_14_007_02.fit.gz',
 'EVS_L2_2013301_01_007_02.fit.gz',
 'EVS_L2_2013302_20_007_02.fit.gz',
 'EVS_L2_2013309_21_007_02.fit.gz',
 'EVS_L2_2013314_04_007_02.fit.gz',
 'EVS_L2_2013323_09_007_02.fit.gz',
 'EVS_L2_2014007_17_007_02.fit.gz',
 #'EVS_L2_2014056_00_007_02.fit.gz',
 'EVS_L2_2014088_16_007_02.fit.gz',
 #'EVS_L2_2014115_00_007_02.fit.gz',
 'EVS_L2_2014162_08_007_02.fit.gz',
 'EVS_L2_2017249_11_007_02.fit.gz',
 'EVS_L2_2017250_13_007_02.fit.gz',
 'EVS_L2_2017253_15_007_02.fit.gz']

for t in range(len(na0)):
    hk='C:/Users/Acturus/.spyder-py3/'+na0[t]
    hdu = fits.open(hk)
    #you can change the filename to something you like
    print(hdu.info())
    a=[]
    aa=[]
    bb=[]
    for i in range(5200):
        if hdu[3].data[0][6][i]>0:
            #print(i,end='\t')
            x.append(i)
            #print(hdu[1].data[i][0])
            a.append(hdu[1].data[i][0])
        if hdu[1].data[i][0]>34:
            break
    aa.append(a)
    for j in range(360):
        
        b=[]
        for i in range(5200):
            if hdu[3].data[0][6][i]>0:
                '''#print(i,end='\t')
                x.append(i)
                #print(hdu[1].data[i][0])
                a.append(hdu[1].data[i][0])'''
                #print(hdu[3].data[306][6][i])
                b.append(hdu[3].data[j][6][i])
            if hdu[3].data[0][6][i]>34:
                break
       
        bb.append(b)
            

    wl0[na0[t]]=aa
    ir0[na0[t]]=bb

result={}
xmm9=[]
xmm13=[]
xmm28=[]
xmm33=[]

for ik in wl0.keys():
    result[ik]=xianxin(wl0[ik][0],ir0[ik],ik)
    xmm9.append(np.sum(result[ik][4])/len(result[ik][4]))
    xmm13.append(np.sum(result[ik][5])/len(result[ik][5]))
    xmm28.append(np.sum(result[ik][6])/len(result[ik][6]))
    xmm33.append(np.sum(result[ik][7])/len(result[ik][7]))

c=300000
resultpe={}
for ipe in wl1.keys():
    resultpe[ipe]=xianxin(wl1[ipe][0],ir1[ipe],ipe)
    f9=list(map(lambda num:num*num,resultpe[ipe][4]))
    v9=(f9-xmm9[0]**2)/(f9+xmm9[0]**2)
    v9=-v9*c
    
    f13=list(map(lambda num:num*num,resultpe[ipe][5]))
    v13=(f13-xmm13[0]**2)/(f13+xmm13[0]**2)
    v13=-v13*c
    
    f28=list(map(lambda num:num*num,resultpe[ipe][6]))
    v28=(f28-xmm28[0]**2)/(f28+xmm28[0]**2)
    v28=v28*c
    
    f33=list(map(lambda num:num*num,resultpe[ipe][7]))
    v33=-(c*xmm33[0]**2 - c*f33)/(xmm33[0]**2 + f33)
    
    na=ipe+'.png'
    plt.plot(v9,c='red',label='Fe XVIII')
    plt.plot(v13,c='blue',label='Fe VIII')
    plt.plot(v28,c='green',label='Fe XV')
    plt.plot(v33,c='orange',label='Fe XVI')
    
    plt.title(ipe,size=20,loc = 'right')
    plt.xlabel('time')
    plt.ylabel('velocity')
    plt.savefig(na)
    
'''Fe XVIII 9.39 6.81 MEGS-A
2 Fe XVI 33.54 6.43 MEGS-A
3 Fe XV 28.42 6.30 MEGS-A

7 Fe VIII 13.09'''

#    -(c*f^2 - c*f4[1]^2)/(f^2 + f4[1]^2)
    
        

 
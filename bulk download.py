# -*- coding: utf-8 -*-

import pandas as pd;
import urllib.request;

q1=pd.read_excel(io=r'D:xflare.xlsx',usecols=['date'])
q2=pd.read_excel(io=r'D:xflare.xlsx',usecols=['peak'])
na1=[]
url1=[]
def zhuanhuan(t):
    months=[0,31,59,90,120,151,181,212,243,273,304,334]
    m=t%10000//100
    y=t//10000
    days=months[m-1]+t%100
    if(y%400==0) or ((y%4)==0) and (y%100!=0):
        days=days+1
    return days

#EVS_L2_2018001_17_007_02.fit.gz
s0='EVS_L2_'
s1='_'
s2='_007_02.fit.gz'

k0='https://lasp.colorado.edu/eve/data_access/evewebdata/products/level2/'

for i in range(len(q1)):
    z1=q1.iloc[i]
    z2=q2.iloc[i]
    if (int(z2)//100)>9:
        s=s0+str(zhuanhuan(int(z1))+(int(z1))//10000*1000)+s1+str(int(z2)//100)+s2
        na1.append(s)
        k=k0+str(int(z1)//10000)+'/'+'0'*(3-len(str(zhuanhuan(int(z1)))))+str(zhuanhuan(int(z1)))+'/'+s
        
        url1.append(k)
        print("downloading with urllib",i)
        try:
            urllib.request.urlretrieve(url1[i],na1[i])
            print(na1[i],'succeed')
        except Exception as e:
            print(na1[i],'failed',e)
            na1[i]=0
            url1[i]=0
            continue
            
        
    else:
        s=s0+str(zhuanhuan(int(z1))+(int(z1))//10000*1000)+s1+'0'+str(int(z2)//100)+s2
        k=k0+str(int(z1)//10000)+'/'+'0'*(3-len(str(zhuanhuan(int(z1)))))+str(zhuanhuan(int(z1)))+'/'+s
        na1.append(s)
        url1.append(k)
        print("downloading with urllib",i)
        try:
            urllib.request.urlretrieve(url1[i],na1[i])
            print(na1[i],'succeed')
        except Exception as e:
            print(na1[i],'failed',e)
            na1[i]=0
            url1[i]=0
            continue

na2=na1[:]
url2=url1[:]
for j in range(len(na2)):
    if na2[j]==0:
        na1.remove(na2[j])
        url1.remove(url2[j])
  
#print(na1)
#print(url1)




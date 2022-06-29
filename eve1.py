# -*- coding: utf-8 -*-
from astropy.io import fits;

import matplotlib.pyplot as plt;

x=[]
a=[]
b=[]
hdu = fits.open('D:\download\EVS_L2_2014007_18_007_02.fit.gz')
#you can change the filename to something you like
print(hdu.info())
for i in range(5200):
    if hdu[3].data[0][6][i]>0:
        #print(i,end='\t')
        x.append(i)
        #print(hdu[1].data[i][0])
        a.append(hdu[1].data[i][0])
        #print(hdu[3].data[306][6][i])
        b.append(hdu[3].data[3][6][i])

plt.axes(yscale = "log")
ax1=plt.plot(a,b)
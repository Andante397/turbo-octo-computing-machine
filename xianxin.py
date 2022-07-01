# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 09:49:52 2022

@author: Acturus
"""
import numpy as np
from astropy.modeling import models, fitting
def xianxin(xl,yl,key):
    x9=[9.35,9.37,9.39,9.41,9.43,9.45]
    x13=[13.01,13.03,13.05,13.07,13.09,13.11,13.13,13.15,13.17,13.19]
    x28=[28.37,28.39,28.41,28.43,28.45,28.47,28.49]
    x33=[33.47,33.49,33.51,33.53,33.55,33.57,33.59,33.61]
    y9=[]
    y13=[]
    y28=[]
    y33=[] 
    y99=[]
    y133=[]
    y288=[]
    y333=[] 
    for ix in range(len(xl)):
        if xl[ix]>9.33 and xl[ix]<9.45:
           # x9.append(xl[ix])
            y9.append(yl[0][ix])

        
        elif xl[ix]>13.01 and xl[ix]<13.19:
           # x13.append(xl[ix])
            y13.append(yl[0][ix])
   
        
        elif xl[ix]>28.37 and xl[ix]<28.49:
          #  x28.append(xl[ix])
            y28.append(yl[0][ix])
 
        
        elif xl[ix]>33.47 and xl[ix]<33.63:
           # x33.append(xl[ix])
            y33.append(yl[0][ix])
   
    if y9==[]:
        print(key,"x9 not found")
    else:
        y99.append(y9)
    if y13==[]:
        print(key,"x13 not found")
    else:
        y133.append(y13)
    if y28==[]:
        print(key,"x28 not found")
       
    else:
        y288.append(y28)
    if y33==[]:
        print(key,"x33 not found")
    else:
        y333.append(y33)
    for iy in range(1,360):
        y9=[]
        y13=[]
        y28=[]
        y33=[] 
        for ix in range(len(xl)):
            if xl[ix]>9.33 and xl[ix]<9.45 and y99!=[]:
               # x9.append(xl[ix])
                y9.append(yl[iy][ix])

            
            elif xl[ix]>13.01 and xl[ix]<13.19 and y133!=[]:
               # x13.append(xl[ix])
                y13.append(yl[iy][ix])
       
            
            elif xl[ix]>28.37 and xl[ix]<28.49 and y288!=[]:
              #  x28.append(xl[ix])
                y28.append(yl[iy][ix])
     
            
            elif xl[ix]>33.47 and xl[ix]<33.63 and y333!=[]:
               # x33.append(xl[ix])
                y33.append(yl[iy][ix])
        y99.append(y9)
        y133.append(y13)
        y288.append(y28)
        y333.append(y33)
    
    '''if y99[0]==[]:
        xmax9=0
    if y133[0]==[]:
        xmax13=0
    if y288[0]==[]:
        xmax28=0
    if y333[0]==[]:
        xmax33=0'''
    
    if y99[0]==[]:
        xmax9=0      
    else:
        xmax9=[]
        for k9 in y99:
            x2=x9
            y2=k9
            xs=np.sum(x2)/len(x2)
            ys=np.sum(y2)/len(y2)
            g_init = models.Gaussian1D(amplitude=ys, mean=xs, stddev=0.01)
            fit_g = fitting.LevMarLSQFitter()
            g = fit_g(g_init, x2, y2)
            xmax9.append(g.mean.value)
        

    if y133[0]==[]:
        xmax13=0
    else:
        xmax13=[]
        for k13 in y133:
            x2=x13
            y2=k13
            xs=np.sum(x2)/len(x2)
            ys=np.sum(y2)/len(y2)
            g_init = models.Gaussian1D(amplitude=ys, mean=xs, stddev=0.01)
            fit_g = fitting.LevMarLSQFitter()
            g = fit_g(g_init, x2, y2)
            xmax13.append(g.mean.value)
        
    if y288[0]==[]:
        xmax28=0
    else:
        xmax28=[]       
        for k28 in y288:
             x2=x28
             y2=k28
             xs=np.sum(x2)/len(x2)
             ys=np.sum(y2)/len(y2)
             g_init = models.Gaussian1D(amplitude=ys, mean=xs, stddev=0.01)
             fit_g = fitting.LevMarLSQFitter()
             g = fit_g(g_init, x2, y2)
             xmax28.append(g.mean.value)
    if y333[0]==[]:
        xmax33=0     
    else:
        xmax33=[]       
        for k33 in y333:
             x2=x33
             y2=k33
             xs=np.sum(x2)/len(x2)
             ys=np.sum(y2)/len(y2)
             g_init = models.Gaussian1D(amplitude=ys, mean=xs, stddev=0.01)
             fit_g = fitting.LevMarLSQFitter()
             g = fit_g(g_init, x2, y2)
             xmax33.append(g.mean.value)
            
        
    return y99,y133,y288,y333,xmax9,xmax13,xmax28,xmax33
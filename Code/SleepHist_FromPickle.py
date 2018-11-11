# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 19:26:42 2018

@author: Scott
"""

import numpy as np
import pandas as pd

pd.read_pickle('SD.pkl')


Window=.5
Ma=16
Mi=0
Edges=np.arange(np.ceil(Ma/Window))*Window+Mi
Sums=np.zeros((len(Edges)-1,1))
for ind,i in enumerate(Edges[0:len(Edges)-1]):
    for ind2,age in enumerate(SleepData["Sleep"]/60):
        if (age>=i) & (age<i+Window):
            Sums[ind]+=SleepData["Weight"][ind2]
            
Avgs=Sums  

import matplotlib.pyplot as plt
import matplotlib.lines as lt


fig, ax = plt.subplots()
X=Edges[0:len(Edges)]+.25
Y=Sums/np.sum(Sums)
Y=np.append(Y,0)
A=ax.fill(X,Y)
plt.xlabel('Sleep (hrs)')
plt.ylabel('Frequency')

Ea=np.transpose(np.array(Edges[0:len(Edges)-1])+.25)
Mea=np.sum(Ea*np.transpose(Sums))/np.sum(Sums)
SD=np.sqrt(np.sum(np.transpose(Sums)*np.square(Ea-Mea))/((len(Sums)-1)*np.sum(Sums)/len(Sums)))
#print(Ea*np.transpose(Sums))
print(Mea)
print(SD)
YL=plt.ylim()

plt.plot([Mea, Mea],[-10,10],'r')
plt.plot([Mea+SD, Mea+SD],[-10,10],'r--')
plt.plot([Mea-SD, Mea-SD],[-10,10],'r--')
plt.ylim([0,YL[1]])

#Mean=8.67, SD=2.11

#plt.savefig("SleepHistogram.png")
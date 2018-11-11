# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 19:45:27 2018

@author: Scott
"""

import matplotlib.pyplot as plt
import numpy as np

WeightDict=np.load('Data/WeightDict.npy').item()
SleepCounts=np.load('Data/SleepCounts.npy')
times=np.load('Data/times.npy')

NSample=sum(WeightDict.values())
NSleepCounts=[x/NSample*100 for x in SleepCounts]
ax=plt.subplot(1,1,1)

NP=np.array(NSleepCounts)
inds=NP==max(NP)
Tinds=times[inds]
plt.plot([Tinds,Tinds],[0, max(NP)],color=[.8,0,0],linewidth=3)

print('Max % = '+str(max(NP)) + ' @ ' + str(Tinds))

#inds=NP==min(NP)
#Tinds=times[inds]
#plt.plot([Tinds,Tinds],[0, min(NP)],'r')
#
#print('Min % = '+str(min(NP)) + ' @ ' + str(Tinds))

plt.ylim([0,100])
plt.xlim([0,24])


xq=np.arange(0,24,.01)
Idata=np.interp(xq,times,NP)
#plt.plot(xq,Idata)
inds=Idata<=6
Tinds=xq[inds]
Ninds=Idata[inds]
plt.plot([min(Tinds),max(Tinds)],[Ninds[0], Ninds[len(Ninds)-1]],color=[.5,.5,0],linewidth=3)
print(Tinds)
#11:20-8:05

xq=np.arange(0,24,.01)
Idata=np.interp(xq,times,NP)
inds=Idata<=50
Tinds=xq[inds]
Ninds=Idata[inds]
plt.plot([min(Tinds),max(Tinds)],[Ninds[0], Ninds[len(Ninds)-1]],'k',linewidth=3)
print(Tinds)

plt.plot(times,NSleepCounts,linewidth=3)
plt.xticks(np.arange(0,28,4))
plt.yticks(np.arange(20,120,20))
#XL=['12AM','3AM','6AM','9AM','12PM','3PM','6PM','9PM','12AM']
XL=['12AM','4AM','8AM','12PM','4PM','8PM','12AM']
ax.set_xticklabels(XL)
plt.xlabel('Hour of the Day',fontsize=20)
plt.ylabel('People Asleep (%)',fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=16)






#plt.savefig("SleepVsTime.png")
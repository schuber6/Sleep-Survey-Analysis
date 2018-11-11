# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 19:31:19 2018

@author: Scott
"""

#import packages and data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Codes=pd.read_csv(r"C:\Users\Scott\Python Code\ATUS_Survey\codes.csv")
Activities=pd.read_csv(r"C:\Users\Scott\Python Code\ATUS_Survey\atusact.csv")
Summary=pd.read_csv(r"C:\Users\Scott\Python Code\ATUS_Survey\atussum.csv")
Respondent=pd.read_csv(r"C:\Users\Scott\Python Code\ATUS_Survey\atusresp.csv")
#print(SU.head(10))
N_people=len(Summary["tucaseid"])  #Initialize all dataframes and store number of people as variable
Roster=pd.read_csv(r"C:\Users\Scott\Python Code\ATUS_Survey\atusrost.csv")

#Record age, day of week, and stat weight data from Respondent and Roster files

import math
import ATUS_Functions as AF

cols=["DayOfWeek","Sleep","Weight","Age"]

#keys from "tucaseid
DOWDict={}  #tudiaryday--frum Respondent
WeightDict={}  #tufnwgtp--from Respondent
AgeDict={}  #teage--from Roster

for ind,row in Roster.iterrows():
    if (row["tulineno"]==1):
        AgeDict[row["tucaseid"]]=row["teage"]

for ind, row in Respondent.iterrows():
    if (row["tulineno"]==1 and math.isnan(row["tudiaryday"]) != True):
        DOWDict[row["tucaseid"]]=row["tudiaryday"]
        WeightDict[row["tucaseid"]]=row['tufnwgtp']
        
times=np.arange(0,24+1/2,1/2)
Ages=np.arange(11,90,15)
SleepCounts=np.zeros((len(Ages),len(times)))
SleepCounts_DOW=np.zeros((7,len(times)))
WSum=np.zeros(len(Ages))
WSum_DOW=np.zeros(7)
for ID in AgeDict.keys():
    W=WeightDict[ID]
    Age=AgeDict[ID]
    AI=AF.AgeInd(Age,Ages)
    WSum[AI]+=W
for ID in DOWDict.keys():
    W=WeightDict[ID]
    DOW=DOWDict[ID]
    WSum_DOW[DOW-1]+=W
    
Sample=len(Activities)

import numpy as np
sleepinds=(Activities["trcodep"]==10101) | (Activities["trcodep"]==10199)
print(np.sum(sleepinds))

for ind,row in Activities[sleepinds].head(Sample).iterrows():
    ID=row["tucaseid"]
    W=WeightDict[ID]
    Age=AgeDict[ID]
    DOW=DOWDict[ID]
    AI=AF.AgeInd(Age,Ages)
    S=AF.Hour_Decimal(row["tustarttim"])
    E=AF.Hour_Decimal(row["tustoptime"])
    if S<4 and E>4: #Make sure people don't have >24 hr logged
        E=3.99
    #index=(times>=S) & (times<=E)
    for ind,counts in enumerate(SleepCounts[AI,:]):
        if S<E and (times[ind]>=S and times[ind]<=E):
            SleepCounts[AI,ind]+=W
            SleepCounts_DOW[DOW-1,ind]+=W
        else:
            if S>E and (times[ind]>=S or (times[ind]<=E and times[ind]<4)):
                SleepCounts[AI,ind]+=W
                SleepCounts_DOW[DOW-1,ind]+=W
                


import numpy as np
sleepinds=(Activities["trcodep"]==10101) | (Activities["trcodep"]==10199)
print(np.sum(sleepinds))

                
#np.save('SleepCounts_Ages',SleepCounts)
#np.save('WeightDict',WeightDict)
#np.save('times',times)
#np.save('Ages',Ages)
#np.save('WSum',WSum)
np.save('SleepCounts_DOW',SleepCounts_DOW)
np.save('WSum_DOW',WSum_DOW)


times=np.arange(0,24+1/2,1/2)
SleepCounts=np.zeros(len(times))
Sample=len(Activities)
for ind,row in Activities[sleepinds].head(Sample).iterrows():
    ID=row["tucaseid"]
    S=AF.Hour_Decimal(row["tustarttim"])
    E=AF.Hour_Decimal(row["tustoptime"])
    if S<4 and E>4: #Make sure people don't have >24 hr logged
        E=3.99
    #index=(times>=S) & (times<=E)
    for ind,counts in enumerate(SleepCounts):
        if S<E and (times[ind]>=S and times[ind]<=E):
            SleepCounts[ind]+=WeightDict[ID]
        else:
            if S>E and (times[ind]>=S or (times[ind]<=E and times[ind]<4)):
                SleepCounts[ind]+=WeightDict[ID]
#np.save('SleepCounts',SleepCounts)
print(AgeDict[ID])
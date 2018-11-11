# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 19:17:41 2018

@author: Scott
"""

#import packages and data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Codes=pd.read_csv("ATUS_Survey/codes.csv")
Activities=pd.read_csv("ATUS_Survey/atusact.csv")
Summary=pd.read_csv("ATUS_Survey/atussum.csv")
Respondent=pd.read_csv("ATUS_Survey/atusresp.csv")
#print(SU.head(10))
N_people=len(Summary["tucaseid"])  #Initialize all dataframes and store number of people as variable
Roster=pd.read_csv("ATUS_Survey/atusrost.csv")

#Tabulate how much sleep each ID got (Slow)

import math
SleepDict={} 
for ind, row in Activities.iterrows():
    if (row["trcodep"]==10101) | (row["trcodep"]==10199):
        if row["tucaseid"] in SleepDict.keys():
            SleepDict[row["tucaseid"]]+=row["tuactdur24"]
        else:
            SleepDict[row["tucaseid"]]=row["tuactdur24"]
            
#Combine day of week and stat weight from Respondent file with Sleep amount from above

cols=["DayOfWeek","Sleep","Weight"]

SleepList=[]
SleepInd=0
#SleepData.loc[1]=[5,2]

for ind, row in Respondent.iterrows():
    if (row["tulineno"]==1 and math.isnan(row["tudiaryday"]) != True) and row["tucaseid"] in SleepDict.keys():
        SleepList.append([row["tudiaryday"],SleepDict[row["tucaseid"]],row["tufnwgtp"]])
        #SleepData.loc[SleepInd]=[row["teage"],SleepDict[row["tucaseid"]]]
        #SleepInd+=1
SleepData=pd.DataFrame(SleepList,columns=cols)
SleepData["WeightXSleep"]=SleepData["Weight"]*SleepData["Sleep"]
print(SleepData.head())

SleepData.to_pickle('SD.pkl')
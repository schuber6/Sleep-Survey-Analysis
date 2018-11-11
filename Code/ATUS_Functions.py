# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:49:38 2018

@author: Scott
"""

def Hour_Decimal(time):
    L=time.split(":")
    return int(L[0])+int(L[1])/60 +int(L[2])/3600

def AgeInd(age,Ages):
    for ind,a in enumerate(Ages):
        if age>a and (ind==len(Ages)-1 or age<=Ages[ind+1]):
            return ind
#Simple Square: Graph={1:{"L":0,"R":2,"D":3,"U":0},2:{"L":1,"R":0,"D":4,"U":0},3:{"L":0,"R":4,"D":0,"U":1},4:{"L":3,"R":0,"D":0,"U":2}}
Graph={1:{"R":{"R":3,"U":2}},2:{"R":4,"D":{"R":3,"L":1}},3:{"L":{"L":1,"U":2},"U":4},4:{"L":2,"D":3}} #Simple card game with nested dicts
import random
import math
import numpy as np
import pandas as pd
def MoveSingleHB(World,Pos):
    Weights={"L":1,"R":1,"U":1,"D":1}
    choices=World[Pos]
    MaxNesting=5
    for ite in np.arange(MaxNesting):
        tot=0
        Vals={}
        for i in choices:
            if choices[i]!=0:
                tot+=Weights[i]
                Vals[tot]=i
        RNG=math.ceil(random.random()*tot)
        if type(choices[Vals[RNG]])==int:
            return choices[Vals[RNG]]
        else:
            choices=choices[Vals[RNG]]
    return 0
        
Data=pd.DataFrame([],columns=list("ME"))
start=1
prev=1
for i in np.arange(10000):
    prev=start
    start=MoveSingleHB(Graph,start)
    Data=Data.append({"M":start,"E":start*100+prev},ignore_index=True)
print(Data["M"].value_counts())
#print(Data["M"])
                

    
    
    
    
    
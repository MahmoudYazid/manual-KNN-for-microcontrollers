

#KNN Algorithms.

import numpy as np


class var():
  x=[[1,1],[1,1.5],[1,2.5],[1,2],[2,1],[2,2]]
  y=[1,1,2,2,1,2]
  x1=[]
  x2=[]

  

def IsolateX1(): 
  for x in range(0,len(var.x)):var.x1.append(var.x[x][0])  
  return 0



def IsolateX2(): 
  for x in range(0,len(var.x)):var.x2.append(var.x[x][1])  
  return 0


def SqrX1PredictminX1(x1_pred):return [(x1_pred-var.x1[x])**2 for x in range(0,len(var.x))] 

def SqrX2PredictminX2(x2_pred):return [(x2_pred-var.x2[x])**2 for x in range(0,len(var.x))]

def Distance(x1_pred,x2_pred): return [ np.sqrt( SqrX1PredictminX1(x1_pred)[x]+ SqrX2PredictminX2(x2_pred)[x]) for x in range(0,len(SqrX2PredictminX2(x2_pred)))] 

def predict(x1_pred,x2_pred):
  IsolateX1()
  IsolateX2()
  
  return print(var.y[Distance(x1_pred,x2_pred).index(np.min(Distance(x1_pred,x2_pred)))])

if __name__=="__main__":
  
  predict(x1_pred=1,x2_pred=1.7)

from inspect import currentframe
from typing import Tuple
import numpy as np
import pandas as pd
import os
from pandas.io.formats.format import _VALID_JUSTIFY_PARAMETERS
import seaborn as sns
import matplotlib.pyplot as plt

# constants
R = 0
C = 1
S = 2


a = 0
with open ("12-hill-climbing-algorithm.txt") as inputFile:
    a = inputFile.read().splitlines()

def height(c):
    if ord(c) in range(ord('a'),ord('z')+1): return ord(c)-ord('a')
    elif c == 'S': return ord('a')-ord('a')
    elif c == 'E': return ord('z')-ord('a')
    else: raise Exception("wtf I missed something?")

b = [list(x) for x in a]
c = [[height(y) for y in x] for x in b]
d = pd.DataFrame(c)
sns.heatmap(data=d, cmap='RdBu_r')
plt.show()                      # show visualisation, the actual code starts below

def findChar(df:pd.DataFrame, ch) -> Tuple:
    (rows,cols) = df.shape
    for r in range(rows):
        for c in range(cols):
            if df.iloc[r,c] == ch:
                return (r,c)
def findStart(df): return findChar(df, 'S')
def findEnd  (df): return findChar(df, 'E')

e = pd.DataFrame(b)
start = findStart(e)
end   = findEnd  (e)



def inPlayfield(df, p:Tuple): return p[0] in range(0,df.shape[R]) and p[1] in range(0,df.shape[C])
def scalable(df,c:Tuple,n:Tuple): return height(df.iloc[n[R],n[C]]) - height(df.iloc[c[R],c[C]]) <= 1
def ok(df,c,n): return inPlayfield(df,n) and scalable(df,c,n)

visited = []
edges = [(start[R],start[C],0)]

def adjacent(n):
    r,c,s = n
    return [(r+1,c,s+1),
            (r-1,c,s+1),
            (r,c+1,s+1),
            (r,c-1,s+1)]
def posList(l:list): return [posNode(n) for n in l]
def posNode(n:Tuple): return (n[R],n[C])

def unrecorded(v:list,e:list,l:list): return [n for n in l if not (posNode(n) in posList(v) or posNode(n) in posList(e))]
def traversable(df,c,l): return [n for n in l if ok(df,(c[R],c[C]),(n[R],n[C]))]

def popMin(e:list):
    m = min(e, key=lambda x:x[S])
    print(m[S])
    e.remove(m)
    return m
    
while edges:
    curr = popMin(edges)
    visited.append(curr)
    g = traversable(e,curr,unrecorded(visited,edges,adjacent(curr)))
    print(g)
    edges.extend(g)

def makeDF(df,ps):
    x = np.zeros(df.shape, dtype=int)
    for n in ps:
        x[n[R],n[C]] = n[S]
    return pd.DataFrame(x)

f = makeDF(e, visited)
sns.heatmap(data=f, cmap='RdBu_r')
plt.show()

def getPos(r,c,ps):
    for n in ps:
        if n[R]==r and n[C]==c:
            return n

g = getPos(20,146,visited)

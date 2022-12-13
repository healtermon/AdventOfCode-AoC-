import numpy as np
import pandas as pd

w = 0
with open ("constellations.txt") as inputFile:
    w = inputFile.read().splitlines()

# get list of vectors [x, y, z, t]
v = list( map(lambda x : np.array(list(map(eval,x.split(",")))), w))
v

def dist(v1,v2):
    return sum(abs(v1-v2))

lv = len(v)
u = np.zeros((lv,lv))
for x in range(lv):
    for y in range (lv):
        u[x,y] = dist(v[x],v[y])
du = pd.DataFrame(u)
du

t = du.applymap(lambda y:1 if y<=3 else 0)

s = t - pd.DataFrame(np.identity(lv))
corr = s.astype(int)

notVisited = list(range(lv))
def visit(x:int):
    notVisited.remove(x)
    for i in range(lv):
        if corr.iloc[x,i]==1 and i in notVisited: visit(i)


no = 0
while notVisited:
    print("new While")
    print(notVisited[0])
    visit(notVisited[0])
    no += 1
    
no # answer to part 1



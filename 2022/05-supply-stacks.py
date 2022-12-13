# [S]                 [T] [Q]        
# [L]             [B] [M] [P]     [T]
# [F]     [S]     [Z] [N] [S]     [R]
# [Z] [R] [N]     [R] [D] [F]     [V]
# [D] [Z] [H] [J] [W] [G] [W]     [G]
# [B] [M] [C] [F] [H] [Z] [N] [R] [L]
# [R] [B] [L] [C] [G] [J] [L] [Z] [C]
# [H] [T] [Z] [S] [P] [V] [G] [M] [M]
#  1   2   3   4   5   6   7   8   9 

import numpy as np
import pandas as pd
from functools import partial
import os
import re
import copy

w = 0
with open ("5-supply-stacks.txt") as inputFile:
    w = inputFile.read().splitlines()
    
def findmove(x):
    for i in range (len(x)):
        if "move" in x[i]:
            return i
m = findmove(w)

a = w[:m-2]
b = w[m:]
c = [list(x[1::4]) for x in a]
d = np.array(c)
e = np.transpose(d)
f = e.tolist()
g = [x[::-1] for x in f]
h = list(map(lambda x: list(filter(lambda y: y!=' ', x)), g))
p = copy.deepcopy(h)

# for x in h:
    # l = re.search(r".*\d+.*",x)
# brain too dead for the above

l = [x.split(" ") for x in b]
m = [list(filter((lambda x: x.isnumeric()), y)) for y in l]
n = [[eval(y) for y in x]for x in m]
o = [[x[0],x[1]-1,x[2]-1] for x in n]

for x in o:
    for y in range(x[0]):
        h[x[2]].append(h[x[1]].pop())
"".join([x.pop() for x in h]) #part1 ans

for x in o:
     y = p[x[1]][len(p[x[1]])-x[0]:]
     p[x[1]] = p[x[1]][:len(p[x[1]])-x[0]]
     p[x[2]] = p[x[2]] + y


"".join([x.pop() for x in p]) #part2 ans

        

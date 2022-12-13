
w = 0
with open ("3-rucksack.txt") as inputFile:
    w = inputFile.read().splitlines()
w = list(map(list,w))

def splitHalf(l):
    m = int(len(l)/2)
    return [l[:m], \
            l[m:]]


def findMatchingItem(r):
    w = list(map(set,r))
    return w[0].intersection(*w[1:]).pop()

def toPriority(i):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    
    v = ord(i)
    if v in range(a, z+1): return v-a + 1
    if v in range(A, Z+1): return v-A + 27

def group_every(step, source):
    return [source[i:i+step]for i in range(0,len(source),step)]
    

sum(map(lambda x: toPriority(findMatchingItem(splitHalf(x))), w)) #part1 ans

sum(map(lambda x: toPriority(findMatchingItem(x)), group_every(3,w))) #part2 ans

def pp(it):
    for i in it:
        print(i)

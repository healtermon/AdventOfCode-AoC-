w = 0
with open ("4-camp-cleanup.txt") as inputFile:
    w = inputFile.read().splitlines()

# ["24-66,23-25",...]
j = list(map(lambda x: x.split(","), w))
# [["24-66" "23-25"],...]
k = list(map(lambda x: list(map(lambda y: y.split("-"), x)), j))
# [[["24" "66"]["23" "25"]],...]
l = [[sToR(*i[0]),sToR(*i[1])] for i in k]

def sToR(s1, s2): return set(range(int(s1),int(s2)+1))

def containsOneAnother(s1,s2):
    s = s1.union(s2)
    return (s1 == s or s2 == s)

len(list(filter(lambda y:y, map(lambda x: containsOneAnother(*x),l)))) #part1 ans

def intersectsAtAll(s1,s2): return len(list(s1.intersection(s2)))>0

len(list(filter(lambda y:y, map(lambda x: intersectsAtAll(*x), l)))) #part2 ans

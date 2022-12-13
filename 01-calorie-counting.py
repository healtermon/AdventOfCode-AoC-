import itertools

w = 0
with open ("1-calorie-counting.txt") as inputFile:
    w= inputFile.read().splitlines()
spl = [list(y) for x, y in itertools.groupby(w, lambda z: z == "") if not x]
cbag = list(map(sum,map(lambda bag: map(eval,bag), spl)))
cbag.sort(reverse=True)
cbag[0]                                 #part 1 ans, the bag containing most calories
sum(cbag[:3])                           #part 2 ans, the sum of top 3 bags' calories

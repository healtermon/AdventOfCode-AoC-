import toolz
w = 0
with open ("6-tuning-trouble.txt") as inputFile:
    w = list(inputFile.read())
w.pop() # get rid of newline
l = 14
a = {i:w[i-l:i] for i in range (l,len(w))}
b = toolz.valmap(set,a)
c = toolz.valmap(lambda x: len(list(x)), b)
d = toolz.valfilter(lambda x: x==l, c) # first key is part1 ans, change l to 14 and re-run, first key is also part2 ans



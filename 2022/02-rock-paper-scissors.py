
# |               | A    | B     |        C |    X |   Y |    Z |
# |---------------+------+-------+----------+------+-----+------|
# | ASCII decimal | 65   | 66    |       67 |   88 |  89 |   90 |
# | play          | 0    | 1     |        2 |    0 |   1 |    2 |
# | outcome       |      |       |          | lose | win | draw |
# | outcome value |      |       |          |   -1 |   0 |   +1 |
# |               | rock | paper | scissors |      |     |      |
# |               | X    | Y     | Z        |      |     |      |

# in a battle between x and y, for y to:
# lose, y = (x-1)%3
# draw  y = (x+0)%3
# win   y = (x+1)%3

import copy

def convertP1PlayToValue(p): return ord(p)-ord('A')
def convertP2PlayToValue(p): return ord(p)-ord('X')


w = 0
with open ("2-rock-paper-scissors.txt") as inputFile:
    w = inputFile.read().splitlines()

rounds = map(lambda x: x.split(" "), w)

rs = map(lambda x: [convertP1PlayToValue(x[0]), convertP2PlayToValue(x[1])], rounds)
rs2 = copy.deepcopy(rs)

def computeRound(r):
    score = 0
    score += r[1] + 1# basic score addition
    
    if r[1] == r[0] + 0:
        score += 3 # draw
    else:
        if r[1] == (r[0]+1)%3: # u win
            score += 6
    return score

def computeRounds(rs): return sum(map(computeRound, rs))

computeRounds(rs) #part1 ans
computeRounds (map(lambda x: [x[0], (x[1]-1 + x[0])%3 ], rs2)) #part2 ans

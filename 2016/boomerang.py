# fbhc 2016
# q1: boomerang constellations
# 50 testcases (-> 1 sec testcase)
#  1000 stars per testcase... Naive permutation solution >> 1 min/testcase

#from itertools import permutations
#from collections import defaultdict
from math import sqrt
from random import randint
from utils import memo, logger

TESTCASE = 'input/boomerang_constellations_example_input.txt'
INPUT = 'input/boomerang_constellations.txt'

#@logger
@memo
def distance(star1, star2):
    return sqrt((star2[0]-star1[0])**2 + (star2[1]-star1[1])**2)

if __name__ == '__main__':
    with open(TESTCASE) as f:
        T = int(f.readline())

        for case in range(1,T+1):
            N = int(f.readline())
            field = [tuple(map(int,f.readline().rstrip('\n').split())) for line in range(N)]
            #N = 10
            #field = [(randint(-10000,10000), randint(-10000,10000)) for line in range(N)]
            # check for duplicate stars in field?

            result = 0
            for star in field:
                for i in range(len(field)):
                    if field[i] == star: continue
                    for j in range(len(field)):
                        if i==j: continue
                        if field[j] == star: continue
                        if distance(star, field[i]) == distance(star, field[j]):
                            result += 1

            print "Case #%d: %d" % (case, result/2)

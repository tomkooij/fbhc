# fbhc 2016
# q1: boomerang constellations
# 50 testcases (-> 1 sec testcase)
#  1000 stars per testcase... Naive permutation solution >> 1 min/testcase

from itertools import groupby
from collections import defaultdict
from math import sqrt
from random import randint

TESTCASE = 'input/boomerang_constellations_example_input.txt'
TESTTOM = 'input/tom_boomerang.txt'
INPUT = 'input/boomerang_constellations.txt'
CHECKNAIVE = 0        # compare solution against SLOW naive solution
RANDOM_STARFIELD = 0  # generate a random starfield

def distance(star1, star2):
    return sqrt((star2[0]-star1[0])**2 + (star2[1]-star1[1])**2)


if __name__ == '__main__':
    with open(INPUT) as f:
        T = int(f.readline())

        for case in range(1,T+1):
            N = int(f.readline())
            stars = [tuple(map(int,f.readline().rstrip('\n').split())) for line in range(N)]

            if RANDOM_STARFIELD:
                N = 30
                stars = [(i,j) for i in range(N) for j in range(N)]
                for _ in range(randint(0,(N-1)*(N-1))):
                    stars.pop(randint(0,len(stars)-1))
                print "%d stars left in starfield" % (len(stars))

            # create a dict with all distances. Values = list of star indexes
            d = defaultdict(list)
            for i in range(len(stars)):
                for j in range(i, len(stars)):
                    if i==j: continue
                    d[distance(stars[i], stars[j])].append((i,j))

            result = 0
            for dist, index_list in d.items():
                #print "search d =", dist
                if len(index_list) == 1:
                    continue

                # create a sorted list of all indexes
                l = []
                for x,y in index_list:
                    l.append(x)
                    l.append(y)
                l = sorted(l)

                # count frequencies of star indexes
                frequencies = [len(list(group)) for key, group in groupby(l)]
                #print frequencies

                # count the number of boomerang constellations:
                #  number = number of edges in graph with n nodes => n*(n+1)/2
                for freq in frequencies:
                    result += freq*(freq-1)/2
                #print "intermediate result = ", result
            #
            # extremely slow (complex) naive solution
            #
            if CHECKNAIVE:
                print "computing naive solution (SLOW!)"
                result_naive = 0
                for star in stars:
                    for i in range(len(stars)):
                        if stars[i] == star: continue
                        for j in range(i, len(stars)):
                            if i==j: continue
                            if stars[j] == star: continue
                            if distance(star, stars[i]) == distance(star, stars[j]):
                                result_naive += 1
                if result != result_naive:
                    print result_naive, result
                assert result_naive == result, 'solution != naive solution'

            print "Case #%d: %d" % (case, result)

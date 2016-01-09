# fbhc 2016
# q1: boomerang constellations
# 50 testcases (-> 1 sec testcase)
#  1000 stars per testcase... Naive permutation solution >> 1 min/testcase

from itertools import groupby
from math import sqrt
from random import randint

TESTCASE = 'input/boomerang_constellations_example_input.txt'
TESTTOM = 'input/tom_boomerang.txt'
INPUT = 'input/boomerang_constellations.txt'
CHECKNAIVE = 1      # compare solution against SLOW naive solution


def distance(star1, star2):
    return sqrt((star2[0]-star1[0])**2 + (star2[1]-star1[1])**2)


if __name__ == '__main__':
    with open(TESTTOM) as f:
        T = int(f.readline())

        for case in range(1,T+1):
            N = int(f.readline())
            stars = [tuple(map(int,f.readline().rstrip('\n').split())) for line in range(N)]
            #N = 10
            #field = [(randint(-10000,10000), randint(-10000,10000)) for line in range(N)]
            # check for duplicate stars in field?

            # get all distances
            d = {}
            for i in range(len(stars)):
                for j in range(len(stars)):
                    if i==j: continue
                    if (j,i) in d: continue
                    d[(i,j)] = distance(stars[i], stars[j])

            # get all unique distances
            unique_d = set(d.values())

            result = 0
            for dist in unique_d:
                print "search d =", dist
                l = []   # list of star indexes
                for (x,y), d1 in d.iteritems():
                    if d1 == dist:
                        #print (x,y)
                        l.append(x)
                        l.append(y)
                l = sorted(l)
                # count frequencies of star indexes
                frequencies = [len(list(group)) for key, group in groupby(l)]
                print frequencies

                # count the number of boomerang constellations:
                #  number = number of edges in graph with n nodes => n*(n+1)/2
                for freq in frequencies:
                    result += freq*(freq-1)/2
                #print "intermediate result = ", result
            #
            # extremely slow (complex) naive solution
            #
            if CHECKNAIVE:
                result_naive = 0
                for star in stars:
                    seen = []
                    for i in range(len(stars)):
                        if stars[i] == star: continue
                        for j in range(len(stars)):
                            if i==j: continue
                            if (j,i) not in seen:
                                seen.append((i,j))
                                if stars[j] == star: continue
                                if distance(star, stars[i]) == distance(star, stars[j]):
                                    result_naive += 1
                if result != result_naive:
                    print result_naive, result
                assert result_naive == result, 'solution != naive solution'

            print "Case #%d: %d" % (case, result)

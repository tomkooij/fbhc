# fbhc 2016
# q1: boomerang constellations
# 50 testcases (-> 1 sec testcase)
#  1000 stars per testcase... Naive permutation solution >> 1 min/testcase

from collections import defaultdict, Counter
from math import sqrt
from random import randint

TESTCASE = 'input/boomerang_constellations_example_input.txt'
TESTTOM = 'input/boomerang_constellations_BIG_INPUT.txt'
INPUT = 'input/boomerang_constellations.txt'
CHECKNAIVE = 0        # compare solution against SLOW naive solution

def distance(star1, star2):
    # sqrt not necessary
    return (star2[0]-star1[0])**2 + (star2[1]-star1[1])**2


if __name__ == '__main__':
    with open(INPUT) as f:
        T = int(f.readline())

        for case in range(1,T+1):
            N = int(f.readline())
            stars = [tuple(map(int,f.readline().rstrip('\n').split())) for line in range(N)]



            # create a dict with all distances. Values = list of star indexes
            d = defaultdict(list)
            for i in range(len(stars)):
                for j in range(i, len(stars)):
                    if i==j: continue
                    d[distance(stars[i], stars[j])].extend([i,j])

            # for each distance count the number of boomerang constellations
            result = 0
            for dist, index_list in d.items():
                if len(index_list) == 2:
                    continue

                # count the frequency of each star index:
                frequencies = Counter(index_list)

                # number of boomerang constellations:
                #  = number of edges in graph with n nodes => n*(n+1)/2
                for freq in frequencies.values():
                    result += freq*(freq-1)/2

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

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

def get_distances(stars):
    length = len(stars)
    d = defaultdict(lambda : defaultdict(int))
    for i in xrange(length):
        for j in xrange(i, length):
            if i==j: continue
            x = (stars[j][0]-stars[i][0])
            y = (stars[j][1]-stars[i][1])
            dd = x**2 + y**2
            d[dd][i] += 1
            d[dd][j] += 1
    return d


def count_frequencies(d):
    result = 0
    for frequencies in d.values():
        # number of boomerang constellations:
        #  = number of edges in graph with n nodes => n*(n+1)/2
        for freq in frequencies.values():
            result += freq*(freq-1)/2
    return result

if __name__ == '__main__':
    with open(INPUT) as f:
        T = int(f.readline())

        for case in range(1,T+1):
            N = int(f.readline())
            stars = [tuple(map(int,f.readline().rstrip('\n').split())) for line in range(N)]

            # create a dict with key = distances. Values = dict with list of index frequencies
            distances = get_distances(stars)
            # for each distance count the number of boomerang constellations
            result = count_frequencies(distances)

            print "Case #%d: %d" % (case, result)

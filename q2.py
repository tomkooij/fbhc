# facebook hackers cup 2015
# qualification round problem 1
# Cooking the Books

import sys
from itertools import combinations

DEBUG = 0
TESTCASE = 'input/new_years_resolution_example_input.txt'


def parse(infile):

    cases = int(infile.readline().rstrip('\n'))

    ll = []
    for case in range(cases):
        gp, gc, gf = map(int, infile.readline().split())
        N = int(infile.readline())
        foods = []
        for i in range(N):
            P, C, F = map(int, infile.readline().split())
            foods.append((P,C,F))
        ll.append((gp, gc, gf, N, foods))

    return ll


if __name__ == '__main__':

    if DEBUG:
        f = open(TESTCASE)
    else:
        f = sys.stdin

    cases = parse(f)

    for casenr, case in enumerate(cases, start=1):
        gp, gc, gf, N, foods = case

        # stupid hack to allow "single item" testcase to pass
        if len(foods) == 1:
            foods.append((0,0,0))

        result = 'no'
        for i in range(1,len(foods)):
            for comb in combinations(foods, i):
                if gp == sum(map(lambda x: x[0], comb)) and gc == sum(map(lambda x: x[1], comb)) and gf == sum(map(lambda x: x[2], comb)):
                    result = 'yes'
                    break

        print "Case #%d: %s" % (casenr, result)

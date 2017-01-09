from math import atan, sqrt, pi

TESTCASES = 'q1_pie_example_input.txt'
INPUT = 'q1_pie_input.txt'


def solve(P, X, Y):
    """ return white if X, Y is outside of the pie, black if inside """

    # use coordinate frame at center of pie
    x = X - 50
    y = Y - 50

    # inside circle?
    if x**2 + y**2 > 50**2:
        return 'white'

    # "edges" and/or special cases
    if P == 0:
        return 'white'
    if x == 0 and y == 0:
        return 'black'

    # theta and phi 0 from y-axis clockwise
    theta = 2*pi * (P / 100)
    if x >= 0:
        phi = pi/2 - atan(y/x)
    else:
        phi = 3*pi/2 - atan(y/x)

    if phi <= theta:
        return 'black'
    else:
        return 'white'


with open(INPUT) as f:
    T = int(f.readline())

    for case in range(1,T+1):
        P, X, Y = tuple(map(int,f.readline().split()))

        print("Case #%d: %s" % (case, solve(P, X, Y)))

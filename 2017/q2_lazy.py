from math import ceil

TESTCASES = 'q2_lazy_example_input.txt'
INPUT = 'q2_lazy_input.txt'


def solve(weights):
    i = 0
    weights.sort(reverse=True)
    while weights:
        #print(weights)
        w = weights.pop(0)
        n = ceil(50 / w) - 1
        for _ in range(n):
            try:
                weights.pop()
            except IndexError:
                return i
        i += 1
    return i


with open(INPUT) as f:
    T = int(f.readline())

    for case in range(1,T+1):
        N = int(f.readline())
        weights = [int(f.readline()) for _ in range(N)]
        print("Case #%d: %d" % (case, solve(weights)))

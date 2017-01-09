import numpy as np

TESTCASES = 'q3_zombie_example_input.txt'
INPUT = 'q3_zombie_input.txt'


def gen_dice_numpy(X, Y):
    """
    return the occurences per value (sum of dice faces) for throwing
    an Y sided dice X times. (XdY)

    examples:
    1d6: [1 1 1 1 1 1]
    2d6: [1 2 3 4 5 6 5 4 3 2 1]
    3d6: [1 3 6 10 15 21 25 27 27 25 21 15 10 6 3 1]
    """
    lst = [1 for _ in range(Y)]

    for k in range(2, X+1):
        # compute productmatrix ('convolution')
        #
        # [1 1 1 1 1 1 0 0 0 0 0]
        # [0 1 1 1 1 1 1 0 0 0 0]
        # ...
        # [0 0 0 0 0 1 1 1 1 1 1]
        #
        # sum of columns:
        # [1 2 3 4 5 6 5 4 3 2 1]
        len_lst = len(lst)
        m = np.zeros((Y, len_lst+Y-1))
        for row in range(Y):
            m[row][row:len_lst+row] = lst
        lst = np.sum(m, axis=0)

    return list(map(int, lst))


def p_dice(H, X, Y, Z):
    """ return the probability that the sum of dices XdY+Z >= H"""

    values = range(X+Z, X*Y+Z+1)

    if H > max(values):
        return 0
    if H <= min(values):
        return 1

    n_per_value = gen_dice_numpy(X, Y)

    assert(len(n_per_value) == len(values))

    n_tot = sum(n_per_value)
    p_list = [n / n_tot for n in n_per_value]

    idx = values.index(H)
    return sum(p_list[idx:])


def parse_spell(spell):
    X, rest = spell.split('d')
    if len(rest.split('+')) == 2:
        Y, Z = rest.split('+')
    elif len(rest.split('-')) == 2:
        Y, Z = rest.split('-')
        Z = int(Z) * -1
    else:
        Y, Z = rest, 0
    return tuple(map(int, (X, Y, Z)))


def solve(H, spells):
    P = []
    for spell in spells:
        X, Y, Z = parse_spell(spell)
        p = p_dice(H, X, Y, Z)
        P.append(p)
    return max(P)


# some testcases
assert parse_spell('3d6-10') == (3, 6, -10)
assert sum(gen_dice_numpy(1, 6)) == 6
assert sum(gen_dice_numpy(2, 6)) == 6**2
assert sum(gen_dice_numpy(3, 6)) == 6**3
assert sum(gen_dice_numpy(20, 4)) == 4**20
#p_dice(H, X, Y, Z):
assert p_dice(7, 1, 6, 0) == 0
assert p_dice(10, 3, 6, 7) == 1
assert p_dice(1, 6, 4, -24) == 0


with open(INPUT) as f:
    T = int(f.readline())
    for case in range(1,T+1):
        H, S = tuple(map(int, f.readline().split()))
        spells = f.readline().split()
        #print(H,S,spells)
        print("Case #%d: %1.6f" % (case, solve(H, spells)))

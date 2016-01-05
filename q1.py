# facebook hackers cup 2015
# qualification round problem 1
# Cooking the Books

import sys

DEBUG = 1
TESTCASE = 'input/cooking_the_books_example_input.txt'


def parse():

    if DEBUG:
        with open(TESTCASE) as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    lines = map(int, lines)
    length = lines.pop(0)
    assert len(lines) == length, 'Input len() != lines[0]'

    return lines


if __name__ == '__main__':

    for case, number in enumerate(parse(), start=1):
        high = 0
        low = number
        digits = list(str(number))
        for i in range(len(digits)):
            for j in range(len(digits)):
                digits[i], digits[j] = digits[j], digits[i]
                if digits[0] != '0':
                    p = int(''.join(digits))
                    high = max(p, high)
                    low = min(p, low)

        print "Case #%d: %d %d" % (case, low, high)

# fbhc 2014
# square detector

TESTCASE = 'input/square_detector_example_input.txt'
INPUT = 'input/square_detector.txt'

if __name__ == '__main__':
    with open(INPUT) as f:
        T = int(f.readline())

        for case in range(1,T+1):
            N = int(f.readline())
            field = [f.readline().rstrip('\n') for line in range(N)]

            # find all black squares ('#')
            blacksquares = []
            for y in range(N):
                for x in range(N):
                    if field[y][x] == '#':
                        blacksquares.append((y,x))

            # top left and bottom right corner
            (y1,x1) = blacksquares[0]
            (y2,x2) = blacksquares[-1]

            # check if all squares black
            result = 'YES'
            for y in range(y1,y2+1):
                for x in range(x1,x2+1):
                    if field[y][x] != '#':
                        result = 'NO'
            # square?
            if (y2-y1) != (x2-x1):
                result = 'NO'

            print "Case #%d: %s" % (case, result)

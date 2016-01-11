# fbhc 2016: boomerang_constellations
# generate big testcases
# grid with random deleted stars.

from random import randint

OUTPUTFILE = 'input/boomerang_constellations_BIG_INPUT.txt'

T = 5
N = 30

if __name__ == '__main__':

    with open(OUTPUTFILE, 'w') as f:
        f.write('%d\n' % T)
        for case in range(1, T+1):
            # N*N grid
            stars = [(i,j) for i in range(N) for j in range(N)]

            # remove random stars
            for _ in range(randint(0,(N-1)*(N-1))):
                stars.pop(randint(0,len(stars)-1))

            print "%d stars left in starfield" % (len(stars))

            f.write('%d\n' % len(stars))
            for x,y in stars:
                f.write('%d %d\n' % (x,y))

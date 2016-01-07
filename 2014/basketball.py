# fbhc 2014
# square detector


TESTCASE = 'input/basketball_game_example_input.txt'
INPUT = 'input/basketball_game.txt'

playerconv = lambda x : (x[0], int(x[1]), int(x[2]))

if __name__ == '__main__':
    with open(TESTCASE) as f:
        T = int(f.readline())


        for case in range(1,T+1):
            N,M,P =  map(int,f.readline().split())
            print "DBG, case",(T,N,M,P)

            players = []
            for _ in range(0,N):
                players.append(playerconv(f.readline().split()))

            players = sorted(players, key = lambda x: x[2], reverse=True)
            players = sorted(players, key = lambda x: x[1])

            print "DBG, players",players

        result = 'fixen!'
        print "Case #%d: %s" % (case, result)

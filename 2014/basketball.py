# fbhc 2014
# square detector


TESTCASE = 'input/basketball_game_example_input.txt'
INPUT = 'input/basketball_game.txt'

playerconv = lambda x : (x[0], int(x[1]), int(x[2]))
addtime = lambda x : (x[0], x[1]+1, x[2])

if __name__ == '__main__':
    with open(TESTCASE) as f:
        T = int(f.readline())


        for case in range(1,T+1):
            N, M, P =  map(int,f.readline().split())
            #print "DBG, case",(case,N,M,P)

            players = [playerconv(f.readline().split()) for _ in range(0,N)]

            players = sorted(players, key = lambda x: (x[1], x[2]), reverse=True)

            assert len(players) == N, 'read wrong number of players!'

            team1, team2 = [], []
            for number, player in enumerate(players, start=1):
                if number % 2:
                    # odd
                    team1.append((number, 0, player[0]))
                else:
                    team2.append((number, 0, player[0]))

            playing = [team1[:P], team2[:P]]
            bench = [team1[P:], team2[P:]]

            for minute in range(M):
                for team in range(2):
                    #print "M, team", M, team
                    #print playing[team]
                    #print bench[team]
                    # add minute for everyone on the field
                    playing[team] = [addtime(player) for player in playing[team]]
                    # subs
                    if bench[team]:
                        subout = sorted(playing[team], key=lambda x: (x[1], x[0]), reverse=True)[0]
                        playing[team].remove(subout)
                        subin = sorted(bench[team], key=lambda x: (x[1], x[0]))[0]
                        #print "DBG: in, out: ", subin, subout
                        bench[team].remove(subin)
                        playing[team].append(subin)
                        bench[team].append(subout)

            result = []
            for team in range(2):
                for player in playing[team]:
                    result.append(player[2])
            print "Case #%d: %s" % (case, ' '.join(sorted(result)))

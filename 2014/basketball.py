# fbhc 2014
# square detector

from collections import defaultdict

TESTCASE = 'input/basketball_game_example_input.txt'
INPUT = 'input/basketball_game.txt'


def playing(team):
    return filter(lambda x: x['playing'], team)
def bench(team):
    return filter(lambda x: not x['playing'], team)
def teamA(team):
    return filter(lambda x: x['number'] % 2, team)
def teamB(team):
    return filter(lambda x: not (x['number'] % 2), team)


if __name__ == '__main__':
    with open(TESTCASE) as f:
        T = int(f.readline())

        for case in range(1,T+1):
            N, M, P =  map(int,f.readline().split())
            #print "DBG, case",(case,N,M,P)

            # read players from input
            players = []
            for _ in range(0, N):
                player = defaultdict()
                name, shot, height= f.readline().split()
                player['name'] = name
                player['shot'] = int(shot)
                player['height'] = int(height)
                players.append(player)

            assert len(players) == N, 'read wrong number of players!'

            # assign draft number
            players = sorted(players, key = lambda x: (x['shot'], x['height']), reverse=True)
            for number, player in enumerate(players, start=1):
                player['number'] = number
                player['playing'] = number < 2*P+1  # True if playing
                player['time'] = 0

            for minute in range(M):
                # add minute for everyone on the field
                for player in playing(players):
                    player['time'] += 1

                # subs for each team
                for team in [teamA, teamB]:
                    max(team(playing(players)), key=lambda x: (x['time'], x['number']))['playing'] = False
                    min(team(bench(players)), key=lambda x: (x['time'], x['number']))['playing'] = True

            result = map(lambda x: x['name'], playing(players))
            print "Case #%d: %s" % (case, ' '.join(sorted(result)))

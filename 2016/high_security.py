# fbhc 2016
# q2: high security


TESTCASE = 'input/high_security_example_input.txt'
INPUT = 'input/high_security.txt'


def find_next_X(line, idx):
    i = line.find('X', idx)
    if i == -1:
        return len(line)
    else:
        return i-1

if __name__ == '__main__':
    with open(INPUT) as f:
        T = int(f.readline())

        for case in range(1,T+1):
            N = int(f.readline())
            line1 = f.readline().rstrip('\n') + 'X'
            line2 = f.readline().rstrip('\n') + 'X'

            #print line1
            #print line2
            #print "0123456789012345"

            guards = [0] * len(line1)
            guard1 = guard2 = -1
            guard1_optimal = 0
            guard2_optimal = 0

            for idx, (elem1, elem2) in enumerate(zip(line1,line2)):
                if guard1 < idx and guard2 < idx:
                    # new strip
                    if elem1 == 'X' and elem2 == 'X':
                        continue
                    if elem1 == '.' and elem2 == '.':
                        if find_next_X(line1, idx) == find_next_X(line2, idx):
                            if line1[idx+1] == '.':
                                guards[idx] = 2
                                guard1 = find_next_X(line1,idx)
                                guard2 = find_next_X(line2,idx)
                            else:
                                guards[idx] = 1  # single cell
                        elif find_next_X(line1, idx) > find_next_X(line2, idx):
                            guards[idx]=1
                            guard1 = find_next_X(line1,idx)
                            if line2[idx+1] == 'X':
                                guard1_optimal = 1
                            else:
                                guard1_optimal = 0
                            #print "new section: place top guard1 at", idx

                        else:
                            #print "new section: place first bottom guard2 at", idx
                            guards[idx]=1
                            guard2 = find_next_X(line2,idx)
                            if line1[idx+1] == 'X':
                                guard2_optimal = 1
                            else:
                                guard2_optimal = 0
                        continue
                if elem1 == '.' and guard1 < idx:
                    if guard2_optimal == 0 and guard2 >= idx and line1[idx+1] != '.':
                        # other guard can do this!
                        if line1[idx+1] == 'X':
                            guard2_optimal = 1
                        else:
                            guard2_optimal = 0
                        #print "skipped top guard1 at", idx
                    else:
                        # place guard, find next X
                        #print "place top gaurd1 at", idx
                        guards[idx] = 1
                        # gaurd 1 is the maximum "reach" of gaurd1
                        guard1 = find_next_X(line1,idx)
                        guard1_optimal = 0
                if elem2 == '.' and guard2 < idx:
                    if guard1_optimal == 0 and guard1 >= idx and line2[idx+1] != '.':
                        if line2[idx+1] == 'X':
                            guard1_optimal = 1
                        else:
                            guard1_optimal = 0
                        #print "skipped bottom gaurd2 at", idx
                    else:
                        # place guard, find next X
                        #print "place bottom guard2 at", idx
                        guards[idx] = 1
                        guard2 = find_next_X(line2,idx)
                        guard2_optimal = 0
            #print guards

            print "Case #%d: %d" % (case, sum(guards))

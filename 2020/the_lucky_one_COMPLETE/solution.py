f = open('testInput.txt', 'r')
output = open('testOutput.txt', 'w')
C = int(f.readline().strip())

for case in range(1, C + 1):
    N = int(f.readline().strip())
    players = {}
    for match in range(1, N + 1):
        A, B, R = list(map(int, f.readline().strip().split()))
        winner = A if R else B
        try:
            players[winner] += 1
        except:
            players[winner] = 1

    output.write('Case #{}: {}\n'.format(case, max(players, key=players.get)))

print('Done')
output.close()

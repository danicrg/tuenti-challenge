from math import floor

f = open('submitInput.txt', 'r')
output = open('submitOutput.txt', 'w')
C = int(f.readline().strip())


def solve(n):
    tuenti_divisions = n // 20
    remainder = n - tuenti_divisions * 20
    return tuenti_divisions if tuenti_divisions * 9 >= remainder else 'IMPOSSIBLE'


for case in range(1, C + 1):
    N = int(f.readline().strip())
    print('Case #{}: {}'.format(case, solve(N)))
    output.write('Case #{}: {}\n'.format(case, solve(N)))

f.close()
output.close()
print('Done!')

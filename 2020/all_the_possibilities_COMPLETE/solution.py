from util import findNCombinations

class PWithCache:

    def __init__(self):
        self.computed_pn = {0: 1}

    def __call__(self, n: int) -> int:

        if n in self.computed_pn:
            return self.computed_pn[n]

        total = 0
        for k in range(1, n + 1):
            minus_one_term = n - k * (3 * k - 1) // 2
            plus_one_term = n - k * (3 * k + 1) // 2
            first_term = 0 if minus_one_term < 0 else self(minus_one_term)
            second_term = 0 if plus_one_term < 0 else self(plus_one_term)
            if k % 2:
                total += first_term + second_term
            else:
                total -= first_term + second_term

        self.computed_pn[n] = total

        return total


P = PWithCache()

f = open('submitInput.txt', 'r')
output = open('submitOutput.txt', 'w')

T = int(f.readline().strip())

print(T, ' test cases:')

for case in range(1, T + 1):
    line = f.readline().strip().split(' ')
    x = int(line[0])
    nums = list(map(int, line[1:]))

    available = [n for n in range(1, x) if n not in nums]

    print('Case: {} x: {} available: {}'.format(case, x, available))
    if len(nums) == 0:
        solution = P(x) - 1
    else:
        solution = findNCombinations(x, available)
    output.write('Case #{}: {}\n'.format(case, solution))
    print('Solution: ', solution)
    print()

print('DONE!')
output.close()

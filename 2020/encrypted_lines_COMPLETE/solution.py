f = open('submitInput.txt', 'r')
output = open('submitOutput.txt', 'w')
N = int(f.readline().strip())

cipher = {
    '.': 'e',
    'o': 's',
    'l': 'p',
    'y': 't',
    'm': 'm',
    'x': 'b',
    'p': 'r',
    'f': 'y',
    'd': 'h',
    'r': 'o',
    'b': 'n',
    'e': 'd',
    'j': 'c',
    'k': 'v',
    't': 'k',
    ';': 'z',
    ',': 'w',
    'n': 'l',
    'c': 'i',
    'v': '.',
    'u': 'f',
    'i': 'g',
    'w': ',',
    'g': 'u',
    'q': 'x',
    'a': 'a',
    's': ';',
    'h': 'j',
    "'": 'q',
    '-': "'",
    'z': '/'
}

print(N, ' cases')

for case in range(1, N + 1):
    line = f.readline().replace('\n', '')
    solution = []
    for letter in list(line):
        try:
            solution.append(cipher[letter])
        except:
            solution.append(letter)
            if letter not in [' ', '(', ')'] and not letter.isdigit():
                print('There was a problem with character ', letter)
    solution = ''.join(solution)
    output.write('Case #{}: {}\n'.format(case, solution))


f.close()
output.close()
print('Done!')

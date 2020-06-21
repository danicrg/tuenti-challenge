#!/usr/local/bin/python3

f = open('testInput.txt', 'r')
lines = f.readlines()
testCases = lines[0]

f = open('testOutput.txt', 'w')
counter = 0

for text in lines[1:]:
    text = text.replace('\n', '')
    base = len(text)
    max = base
    min = pow(base, base - 1)
    for i in range(2, base):
        max += i * pow(base, i)
        min += i * pow(base, base - i - 1)
    dif = max - min
    counter += 1
    f.write(f'Case #{counter}: {dif}\n')
print('Complete')

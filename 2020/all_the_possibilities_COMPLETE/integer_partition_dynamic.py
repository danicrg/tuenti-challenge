def integerPartition(n, summands):

    summands = summands + [n]
    l_summands = len(summands) + 1
    n = n + 1

    partitionMatrix = [[0] * n for x in range(l_summands)]

    for summandIndex in range(0, l_summands):
        partitionMatrix[summandIndex][0] = 1

    for summandIndex in range(1, l_summands):
        summand = summands[summandIndex - 1]
        for numberIndex in range(1, n):
            number = numberIndex
            if summand > number:

                partitionMatrix[summandIndex][numberIndex] = partitionMatrix[summandIndex - 1][numberIndex]

            else:

                combosWithoutSummand = partitionMatrix[summandIndex - 1][numberIndex]

                combosWithSummand = partitionMatrix[summandIndex][number - summand]

                # combosWithSummand = findCombosWithSummand(number, available[:summandIndex])

                partitionMatrix[summandIndex][numberIndex] = combosWithoutSummand + combosWithSummand

    # print(''.join([' '.join(str(l) for l in x) + '\n' for i, x in enumerate(partitionMatrix)]))

    return partitionMatrix[-1][-1]



f = open('testInput.txt', 'r')
output = open('testOutput.txt', 'w')

T = int(f.readline().strip())

print(T, ' test cases:')

for case in range(1, T + 1):
    line = f.readline().strip().split(' ')
    x = int(line[0])
    nums = list(map(int, line[1:]))

    available = [n for n in range(1, x) if n not in nums]

    print('Case: {} x: {} available: {}'.format(case, x, available))

    solution = integerPartition(x, available) - 1
    output.write('Case #{}: {}\n'.format(case, solution))
    print('Solution: ', solution)
    print()

print('DONE!')
output.close()

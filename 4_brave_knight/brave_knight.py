#!/usr/local/bin/python3

import numpy as np
import itertools as it


def test_jump(matrix, start, jump):
    end = (start[0] + jump[0], start[1] + jump[1])
    if end[0] < np.shape(matrix)[0] and end[1] < np.shape(matrix)[1] and end[0] > -1 and end[1] > -1:
        return end, matrix[end]
    else:
        return (-1, -1), '#'


def move_forward(matrix, previous, start, destination, counter):
    global return_able, limit
    if counter < limit:
        for jump in jumps:
            end, tile = test_jump(matrix, start, jump)

            if tile == '#':
                continue
            elif tile == destination:
                if destination == 'P':
                    return_able = True
                    path = move_forward(matrix, start, end, 'D', counter + 1)
                    if len(path) == 0:
                        continue
                    return [end] + path
                elif destination == 'D':
                    limit = 1000
                    return [end]
            else:
                if previous != end:
                    return_able = False
                    path = move_forward(matrix, start, end, destination, counter + 1)
                    if len(path) == 0:
                        continue
                    return [end] + path
                elif return_able:
                    return_able = False
                    path = move_forward(matrix, start, end, destination, counter + 1)
                    if len(path) == 0:
                        continue
                    return [end] + path
                else:
                    continue

    return []


f = open('testInput.txt', 'r')

return_able = False
limit = 5

cases = int(f.readline())

jumps = it.product((-1, -2, 1, 2), repeat=2)
jumps = sorted([jump for jump in jumps if abs(jump[0]) != abs(jump[1])])

for case in range(cases):

    # A little cleansing
    dimensions = f.readline().replace('\n', '').split(' ')
    matrix = []
    s = ()
    for i in range(int(dimensions[0])):
        row = list(f.readline().replace('\n', ''))
        if 'S' in row:
            s = (i, row.index('S'))
        matrix.append(row)
    matrix = np.array(matrix)

    # Now we got the matrix and the location of S

    path = []
    for i in range(1, 13):
        limit = i
        path = move_forward(matrix, s, s, 'P', 0)
        if len(path) > 0:
            print(f'Case #{case+1}: ' + str(len(path)))
            break
    if len(path) == 0:
        print(f'Case #{case+1}: IMPOSSIBLE')

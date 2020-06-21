#!/usr/local/bin/python3

import numpy as np
import collections
import heapq
import tqdm


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class KnightGrid:
    def __init__(self, grid):
        self.grid = np.array(grid)
        self.width = self.grid.shape[1]
        self.height = self.grid.shape[0]

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.height and 0 <= y < self.width

    def not_lava(self, id):
        (x, y) = id
        return self.grid[x, y] != '#'

    def neighbors(self, id):
        # Returns a list of neighbors
        (x, y) = id
        jumps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        if self.grid[x, y] == '*':
            jumps = [(-4, -2), (-4, 2), (-2, -4), (-2, 4), (2, -4), (2, 4), (4, -2), (4, 2)]
        results = [(x + j[0], y + j[1]) for j in jumps]
        results = filter(self.in_bounds, results)
        results = filter(self.not_lava, results)
        # print(id, list(results))
        return list(results)


def dijkstra(graph, start, goal):
        # Search
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

    # Reconstruction
    if current == goal:
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
        return path

    return [0, 0]


if __name__ == "__main__":
    f = open('testInput.txt', 'r')
    cases = int(f.readline())
    out = open('testOutput.txt', 'w')

    for case in tqdm.tqdm(range(cases)):

        # A little cleansing
        dimensions = f.readline().replace('\n', '').split(' ')
        matrix = []
        s = ()
        d = ()
        p = ()
        for i in range(int(dimensions[0])):
            row = list(f.readline().replace('\n', ''))
            if 'S' in row:
                s = (i, row.index('S'))
            if 'D' in row:
                d = (i, row.index('D'))
            if 'P' in row:
                p = (i, row.index('P'))
            matrix.append(row)

        graph = KnightGrid(matrix)

        path = dijkstra(graph, s, p) + dijkstra(graph, p, d)[1:]

        if path[-1] != 0 and path[0] != 0:
            out.write(f'Case #{case+1}: ' + str(len(path) - 1) + '\n')
        else:
            out.write(f'Case #{case+1}: IMPOSSIBLE\n')

    out.close()
    print('Complete!')

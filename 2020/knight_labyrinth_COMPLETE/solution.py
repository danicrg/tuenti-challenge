import numpy as np
import collections
import heapq
from netcat import Netcat
nc = Netcat('52.49.91.111', 2003)


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


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

    def __init__(self, grid, kp):
        self.grid = grid
        self.width = self.grid.shape[1]
        self.height = self.grid.shape[0]
        self.kp = kp
        self.visited = []
        self.expand_map(kp, self.read_grid())

    def __str__(self):

        return '\n'.join([''.join(row) for row in np.array(graph.grid[50:114, 50:170])])

    def read_grid(self):
        answer = nc.read()
        if len(answer) != 32:
            print(answer)

        return np.matrix([list(row) for row in answer.split('\n')[:5]])

    def expand_map(self, kp, mmap):
        try:
            for i, row in enumerate(mmap):
                self.grid[kp[0] - 2 + i, kp[1] - 2:kp[1] + 3] = row
                self.grid[kp[0], kp[1]] = '.'
        except:
            return 'Challenge Complete!'

    def move_knight(self, kp, dx, dy):
        if dx == 0 and dy == 0:
            return
        self.kp = (kp[0] + dx, kp[1] + dy)

        order = str(abs(dx)) + 'u' if dx < 0 else str(dx) + 'd'
        order += str(abs(dy)) + 'l' if dy < 0 else str(dy) + 'r'

        nc.write(bytes(order, 'utf-8'))

        self.expand_map(self.kp, self.read_grid())

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.height and 0 <= y < self.width

    def not_lava(self, id):
        (x, y) = id
        return self.grid[x, y] != '#'

    def neighbors(self, id):
        # Returns a list of neighbors
        (x, y) = id
        jumps = [(-1, 2), (2, 1), (1, -2), (1, 2), (-2, -1), (-2, 1), (-1, -2), (2, -1)]
        results = [(x + j[0], y + j[1]) for j in jumps]
        results = filter(self.in_bounds, results)
        results = list(filter(self.not_lava, results))

        for result in results:
            if result not in self.visited:
                d_destination = (result[0] - x, result[1] - y)
                self.move_knight(id, d_destination[0], d_destination[1])
                self.move_knight(result, -d_destination[0], -d_destination[1])
                self.visited.append(result)

        return results

    def neighbors_original(self, id):
        # Returns a list of neighbors
        (x, y) = id
        jumps = [(-1, 2), (2, 1), (1, -2), (1, 2), (-2, -1), (-2, 1), (-1, -2), (2, -1)]
        results = [(x + j[0], y + j[1]) for j in jumps]
        results = filter(self.in_bounds, results)
        results = list(filter(self.not_lava, results))
        return results


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path


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
        path = dijkstra_original(graph, graph.kp, current)
        for move in path:
            graph.move_knight(graph.kp, move[0] - graph.kp[0], move[1] - graph.kp[1])

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

        print(graph)

    # Reconstruction
    if current == goal:
        return reconstruct_path(came_from, start, goal)

    return [0, 0]


def dijkstra_original(graph, start, goal):
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

        for next in graph.neighbors_original(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

    # Reconstruction
    if current == goal:
        return reconstruct_path(came_from, start, goal)

    return [0, 0]


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start, goal):

    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()
        path = dijkstra_original(graph, graph.kp, current)
        for move in path:
            graph.move_knight(graph.kp, move[0] - graph.kp[0], move[1] - graph.kp[1])

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

        print(graph)

    return came_from, cost_so_far


def breadth_first_search_2(graph, start, goal):

    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        path = dijkstra_original(graph, graph.kp, current)
        for move in path:
            graph.move_knight(graph.kp, move[0] - graph.kp[0], move[1] - graph.kp[1])

        if current == goal:
            break

        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
        print(graph)
    return came_from

################# SEVERAL ALGORITHMS WERE TESTED ##############


if __name__ == "__main__":

    matrix = np.matrix([['#'] * 220] * 220)
    kp = (110, 110)
    p = (110, 111)

    graph = KnightGrid(matrix, kp)

    path = breadth_first_search_2(graph, kp, p)

    print('Complete!')

#!/usr/local/bin/python3

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


def get_coinciding_notes(notes, root_note):
    coinciding_notes = [note for note in notes if note[0] <= root_note[1] and root_note[0] <= note[0] and note != root_note]
    return coinciding_notes


def get_next_notes(notes, root_note):
    new_notes = [note for note in notes if note[0] > root_note[1]]
    if len(new_notes) > 0:
        return [new_notes[0]] + get_coinciding_notes(new_notes, new_notes[0])
    return []


f = open('testInput.txt', 'r')
cases = int(f.readline())


output = open('testOutput.txt', 'w')

for i in range(0, cases):
    all_notes = []
    number_of_notes = int(f.readline())
    for j in range(0, number_of_notes):
        initial_position, length, speed, score = list(map(int, f.readline().replace('\n', '').split(' ')))

        initial_time = initial_position / speed
        final_time = (initial_position + length) / speed

        all_notes.append((initial_time, final_time, score))

    all_notes.sort(key=lambda i: i[0])
    starts = [all_notes[0]]
    starts += get_coinciding_notes(all_notes, all_notes[0])

    # starts = all_notes
    best = 0

    frontier = PriorityQueue()
    came_from = {}
    score_so_far = {}

    for start in starts:
        frontier.put(start, start[-1])
        came_from[start] = None
        score_so_far[start] = start[-1]

    while not frontier.empty():
        current = frontier.get()
        for next in get_next_notes(all_notes, current):
            new_score = score_so_far[current] + next[-1]
            if next not in score_so_far or new_score > score_so_far[next]:
                score_so_far[next] = new_score
                priority = new_score
                frontier.put(next, priority)
                came_from[next] = current

    for current in came_from:
        score = 0
        while current != None:
            repeats = [note for note in all_notes if current[0:2] == note[0:2]]
            score += sum([note[-1] for note in repeats])
            current = came_from[current]
        if score > best:
            best = score

    print('Case #%i: %i' % (i + 1, best))
    output.write(f'Case #{i+1}: {best}\n')


print('\nComplete!')

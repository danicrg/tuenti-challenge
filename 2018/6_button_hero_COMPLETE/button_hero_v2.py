#!/usr/local/bin/python3


import tqdm
from profiler import profile


def get_previous_compatible_notes(notes, root_note):
    return [note for note in notes if note[1] < root_note[0]]


def merge_equal_notes(notes):
    notes = sorted(notes)
    notes = [(0.0, 0.0, 0.0)] + notes
    new_notes = []
    for j in range(1, len(notes)):
        if notes[j][0:2] == notes[j - 1][0:2]:
            new_notes[-1] = (notes[j][0:2] + (notes[j][-1] + new_notes[-1][-1],))
        else:
            new_notes.append(notes[j])
    return new_notes


@profile
def main():
    f = open('testInput.txt', 'r')
    cases = int(f.readline())

    output = open('testOutput.txt', 'w')

    for i in tqdm.tqdm(range(0, cases)):
        all_notes = []
        number_of_notes = int(f.readline())
        for j in range(0, number_of_notes):
            initial_position, length, speed, score = list(map(int, f.readline().replace('\n', '').split(' ')))

            initial_time = initial_position / speed
            final_time = (initial_position + length) / speed

            all_notes.append((initial_time, final_time, score))

        all_notes = merge_equal_notes(all_notes)
        new_all_notes = []

        for note in all_notes:

            compatible_notes = get_previous_compatible_notes(new_all_notes, note)

            if len(compatible_notes) > 0:
                max_score = max(n[-1] for n in compatible_notes)
            else:
                max_score = 0

            new_note = note[:2] + (max_score + note[-1],)
            new_all_notes.append(new_note)

        best = max(n[-1] for n in new_all_notes)
        output.write(f'Case #{i+1}: {best}\n')

    print('\nComplete!')


if __name__ == "__main__":
    main()

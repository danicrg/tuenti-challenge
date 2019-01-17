#!/usr/local/bin/python3

f = open('testInput.txt', 'r')
cases = int(f.readline())

notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

major = [0, 2, 4, 5, 7, 9, 11]
minor = [0, 2, 3, 5, 7, 8, 10]

major_scales = []
minor_scales = []
for note in notes:
    major_scale = []
    minor_scale = []
    for i in major:
        major_scale.append((notes + notes)[notes.index(note) + i])
    for i in minor:
        minor_scale.append((notes + notes)[notes.index(note) + i])
    major_scales.append(major_scale)
    minor_scales.append(minor_scale)

output = open('testOutput.txt', 'w')
counter = 1

for i in range(0, cases):
    if int(f.readline()) > 0:

        text = f.readline()
        text = text.replace('Cb', 'B')
        text = text.replace('Db', 'C#')
        text = text.replace('Eb', 'D#')
        text = text.replace('Fb', 'E')
        text = text.replace('Gb', 'F#')
        text = text.replace('Ab', 'G#')
        text = text.replace('Bb', 'A#')
        text = text.replace('B#', 'C')
        text = text.replace('E#', 'F')
        notes_to_test = text.replace('\n', '').split(' ')

        scales = []
        for scale in major_scales:
            if all(note in scale for note in notes_to_test):
                scales.append('M' + scale[0])
        for scale in minor_scales:
            if all(note in scale for note in notes_to_test):
                scales.append('m' + scale[0])

        if len(scales) > 0:
            output.write(f'Case #{counter}: ' + ' '.join(sorted(scales)) + '\n')
        else:
            output.write(f'Case #{counter}: None\n')

    else:

        scales = []
        for scale in major_scales:
            scales.append('M' + scale[0])
        for scale in minor_scales:
            scales.append('m' + scale[0])
        output.write(f'Case #{counter}: ' + ' '.join(sorted(scales)) + '\n')

    counter += 1

print('Complete!')

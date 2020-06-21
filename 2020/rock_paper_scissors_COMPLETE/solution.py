f = open('submitInput.txt', 'r')
output = open('submitOutput.txt', 'w')
N = int(f.readline().strip())

for case in range(1, N + 1):
    shapes = f.readline().strip().split()
    if len(set(shapes)) < len(shapes):
        output.write('Case #{}: {}\n'.format(case, '-'))
        continue
    elif 'R' in shapes and 'S' in shapes:
        output.write('Case #{}: {}\n'.format(case, 'R'))
        continue
    elif 'R' in shapes and 'P' in shapes:
        output.write('Case #{}: {}\n'.format(case, 'P'))
        continue
    elif 'P' in shapes and 'S' in shapes:
        output.write('Case #{}: {}\n'.format(case, 'S'))
        continue
print('Done')

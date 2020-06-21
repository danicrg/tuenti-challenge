
def read_grid():
    return np.matrix([list(row) for row in nc.read().split('\n')[:5]])


def expand_map(kp, matrix, mmap):
    for i, row in enumerate(mmap):
        matrix[kp[0] - 2 + i, kp[1] - 2:kp[1] + 3] = row


def move_knight(kp, dx, dy):
    kp = (kp[0] + dx, kp[1] + dy)

    order = str(abs(dx)) + 'u' if dx < 0 else str(dx) + 'd'
    order += str(abs(dy)) + 'l' if dx < 0 else str(dy) + 'r'

    nc.write(bytes(order, 'utf-8'))

    expand_map(kp, matrix, read_grid())


expand_map(kp, matrix, read_grid())

move_knight(kp, -2, -1)

print(matrix[105:115, 105:115])

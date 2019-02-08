#!/usr/local/bin/python3


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return int(a * b / gcd(a, b))


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def intersect(door1, door2):
    return (door1[0] + (door2[0] - door1[0]) * modinv(door1[1], door2[1]) * door1[1]) % lcm(door1[1], door2[1])


f = open('testInput.txt', 'r')
out = open('testOutput.txt', 'w')

cases = int(f.readline())

for case in range(cases):
    number_of_doors = int(f.readline())
    doors = []
    for index, door in enumerate(range(number_of_doors)):
        p, t = f.readline().replace('\n', '').split(' ')
        first_open = int(p) - int(t)
        doors.append((first_open - index, int(p)))

    doors = sorted(doors, key=lambda x: -x[1])
    door_counter = 2

    try:
        new_t = intersect(doors[0], doors[1])
    except:
        out.write(f'Case #{case+1}: NEVER\n')
        continue
    new_p = lcm(doors[0][1], doors[1][1])

    while True:

        if door_counter >= len(doors):
            solution = new_t
            break
        new_door = (new_t, new_p)

        try:
            new_t = intersect(new_door, doors[door_counter])
        except:
            solution = 'NEVER'
            break

        new_p = lcm(new_door[1], doors[door_counter][1])
        door_counter += 1

    out.write(f'Case #{case+1}: {solution}\n')

print('Complete!')

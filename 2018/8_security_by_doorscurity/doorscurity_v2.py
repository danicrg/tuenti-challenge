#!/usr/local/bin/python3

from fractions import gcd


def ext_gcd(a, b):
    v1 = [1, 0, a]
    v2 = [0, 1, b]

    if a > b:
        a, b = b, a
    while v1[2] > 0:
        q = v2[2] / v1[2]
        for i in range(0, len(v1)):
            v2[i] = v2[i] - q * v1[i]
        v1, v2 = v2, v1
    return v2[0], v2[1]


def chinese_remainder(a, m):
    n = len(a)

    a1 = a[0]
    m1 = m[0]

    for i in range(1, n):
        a2 = a[i]
        m2 = m[i]

        g = gcd(m1, m2)

        if a1 % g != a2 % g:
            return None

        p, q = ext_gcd(m1 / g, m2 / g)

        mod = m1 / g * m2
        x = (a1 * (m2 / g) % mod * q % mod + a2 * (m1 / g) % mod * p % mod) % mod

        a1 = x
        if a1 < 0:
            a1 += mod
        m1 = mod
    if type(a1) == None:
        return 'NEVER'
    return int(a1)


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


# def chinese_remainder(n, a):
#     sum = 0
#     prod = reduce(lambda a, b: a * b, n)
#     for n_i, a_i in zip(n, a):
#         p = prod // n_i
#         try:
#         	sum += a_i * modinv(p, n_i) * p
#         except:
#         	return 'NEVER'
#     return sum % prod


def main():
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

        n, a = zip(*doors)
        solution = chinese_remainder(n, a)

        # out.write(f'Case #{case+1}: {solution}\n')

    print('Complete!')


if __name__ == "__main__":
    main()

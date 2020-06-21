#!/usr/local/bin/python3

import sys


def main():
    f = open(sys.argv[1], 'r')
    output = open(sys.argv[2], 'w')
    cases = int(f.readline())

    for case in range(1, cases + 1):
        waffle = f.readline().rstrip().split(' ')
        holes = (int(waffle[0]) - 1) * (int(waffle[1]) - 1)
        output.write(f'Case #{case}: {holes}\n')
    output.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: waffles input.in output.out')
    else:
        main()

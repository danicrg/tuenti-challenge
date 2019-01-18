#!/usr/local/bin/python3

import sys


def get_arguments(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    waffles = []
    for waffle in lines[1:]:
        waffle = waffle.replace('\n', '').split(' ')
        waffles.append(waffle)
    return waffles


def main():
    f = open(sys.argv[2], 'w')
    counter = 0
    for waffle in waffles:
        counter += 1
        holes = (int(waffle[0]) - 1) * (int(waffle[1]) - 1)
        f.write(f'Case #{counter}: {holes}\n')
    f.close()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: waffles input.in output.out')
    else:
        waffles = get_arguments(sys.argv[1])
        main()

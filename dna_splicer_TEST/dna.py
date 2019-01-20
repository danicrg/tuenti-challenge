#!/usr/local/bin/python3

import itertools as it
import socket


def reconstruct(input):
    """receives input as a string"""
    input = input.replace('\n', '').split(' ')
    print(input)

    repeater = 1
    samples = []
    while True:
        print(repeater)
        subsets = it.product(input, repeat=repeater)

        winner = ''
        for subset in subsets:
            sample = ''.join(i for i in subset)
            if sample not in samples:
                samples.append(sample)
            else:
                winner = sample
                break

        set_of_winner = [i for i in input if i in winner]
        solution = [input.index(i) + 1 for i in set_of_winner]
        if len(solution) > 0:
            break

    solution = ','.join(str(index) for index in solution)
    return solution


ip = '52.49.91.111'
port = 3241

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((ip, port))

socket.recv(2048)
socket.recv(2048)
socket.send(b'TEST\n')
socket.recv(1024)

while True:
    input = socket.recv(1024).decode("utf-8")
    solution = reconstruct(input)
    print(solution)
    socket.send(bytes(solution + '\n', 'utf-8'))
    message = socket.recv(2048).decode("utf-8")
    print(message)
    if 'Congratulations' in message:
        break

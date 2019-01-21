#!/usr/local/bin/python3

import itertools as it
import socket


def test_chunk(input, chunk, indexes):
    for slice in input:
        if slice == chunk:
            continue
        big = max(slice, chunk)
        small = min(slice, chunk)
        if big[0:len(small)] == small:
            if input.index(slice) + 1 not in indexes:
                indexes += [input.index(slice) + 1]

            else:
                continue
            remainder = big[len(small):]
            if len(remainder) > 0:
                new_indexes = test_chunk(input, remainder, indexes)
                if len(new_indexes) > 0:
                    return indexes
                indexes.pop(-1)

    if chunk in input:
        index = input.index(chunk) + 1
        if index not in indexes:
            indexes += [index]
            return indexes
        else:
            return []
    return []


def reconstruct(input):
    """receives input as a string"""
    input = input.replace('\n', '').split(' ')
    print(input)
    for slice_index, slice in enumerate(input):
        indexes = [slice_index + 1]
        indexes = test_chunk(input, slice, indexes)
        if len(indexes) > 1:
            return ','.join(str(i) for i in sorted(indexes))
            break
    return ''


ip = '52.49.91.111'
port = 3241

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((ip, port))

socket.recv(2048)
socket.recv(2048)
socket.send(b'SUBMIT\n')
socket.recv(1024)

while True:
    input = socket.recv(1024).decode("utf-8")
    solution = reconstruct(input)
    print(solution)
    socket.send(bytes(solution + '\n', 'utf-8'))
    message = socket.recv(2048).decode("utf-8")
    print(message)
    if 'Congratulations' in message or 'not correct' in message:
        break

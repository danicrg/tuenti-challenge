def findCombinationsUtil(arr, index, num, reducedNum, available):
    # print(arr)
    solutions = []

    if (reducedNum < 0):
        return solutions

    if (reducedNum == 0):
        solutions.append(arr[:index])
        return solutions

    prev = available[0] if(index == 0) else arr[index - 1]  # Initial case
    prev = available.index(prev)

    for k in available[prev:len(available) - prev + 1]:
        arr[index] = k

        solutions.extend(findCombinationsUtil(arr, index + 1, num, reducedNum - k, available))

    return solutions


def findCombinations(n, available):
        # Initiate recursion
    arr = [0] * n
    return findCombinationsUtil(arr, 0, n, n, available)


def findNCombinations(n, available):
    arr = [0] * n
    return findNCombinationsUtil(arr, 0, n, n, available)


def findNCombinationsUtil(arr, index, num, reducedNum, available):
    solutions = 0

    if (reducedNum < 0):
        return solutions

    if (reducedNum == 0):
        return solutions + 1

    prev = available[0] if(index == 0) else arr[index - 1]  # Initial case
    prev = available.index(prev)
    for k in available[prev:len(available) - prev + 1]:
        arr[index] = k
        solutions += findNCombinationsUtil(arr, index + 1, num, reducedNum - k, available)

    return solutions


class PCustomWithCache:

    def __init__(self, n, available):
        self.available = available
        self.n = n
        self.computed_pn = {
            0: 0,
            1: findNCombinations(1, available)

        }

    def __call__(self, n: int) -> int:

        print(self.computed_pn)

        if n in self.computed_pn:
            return self.computed_pn[n]

        total = 0
        for i in [x for x in self.available if x in range(1, self.n - n + 1)]:
            calculate = n - i
            if calculate > 0:
                arr = [0] * calculate
                print('Calculate: ', calculate)
                total += self(calculate)

        self.computed_pn[n] = total

        return total

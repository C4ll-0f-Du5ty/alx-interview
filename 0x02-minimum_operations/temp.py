#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
    """
import math


def summation(n, num_times):
    """_summary_

    Args:
        n (_type_): _description_
        num_times (_type_): _description_

    Returns:
        _type_: _description_
    """
    total = 0
    for _ in range(num_times):
        total += n
    return total


def minOperations(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if (n < 1):
        return 0

    primes = []

    for j in range(2, n):
        flag = True
        if j == 2:
            primes.append(j)
            continue
        if j % 2 == 0:
            continue
        if j % 2 != 0:
            for i in range(3, math.floor(j / 2), 3):
                if (j % i) == 0:
                    flag = False
                    break
        if flag:
            primes.append(j)

    if len(primes) == 1:
        if pow(primes[0], 2) == n:
            return pow(primes[0], 2)
    p = 1
    while p != n:
        for i in primes:
            for j in primes:
                if pow(i, p) * j == n:
                    return summation(i, p) + j
        p += 1

    # print(summation(primes[0], 5))


print(minOperations(4))

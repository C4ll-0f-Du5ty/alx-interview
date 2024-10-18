#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
    """
import math


def summation(nums):
    """_summary_

    Args:
        n (_type_): _description_
        num_times (_type_): _description_

    Returns:
        _type_: _description_
    """
    total = 0
    for i in nums:
        total += i
    return total


# def isPrime(n):
#     """_summary_

#     Args:
#         n (_type_): _description_

#     Returns:
#         _type_: _description_
#     """
#     if n == 2:
#         return True
#     elif n % 2 == 0:
#         return False
#     else:
#         for i in range(3, math.floor(n/2), 3):
#             if n % i == 0:
#                 return False
#     return True


def minOperations(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n <= 1:
        return 0

    primeFactors = []

    k = n
    divisor = 2
    while k > 1:
        if (k % divisor) == 0:
            primeFactors.append(divisor)
            k /= divisor
        else:
            divisor += 1

    return summation(primeFactors)
    # print(summation(primes[0], 5))


# print(minOperations(19170307))

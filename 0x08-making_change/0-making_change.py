#!/usr/bin/python3


# def timesCheck(total, i, times):
#     n = i * (total/i)
#     print("N:", int(n))
#     print(total > int(n))
#     return n if times > int(n) or times == 0 else times

# def check(total, i):
#     return total // i == total / i

# def makeChange(coins, total):

#     if total < 1:
#         return 0

#     times = 0
#     for i in coins:
#         if check(total, i):
#             # print(i, ' The first: am in')
#             times = timesCheck(total, i, times)
#         elif total > i:
#             n = total - i
#             for j in coins:
#                 if check(n, j):
#                     # print(j, ' The second: am in')
#                     times = timesCheck(n, j, times + 1)

#     return -1 if times == 0 else times


""" Contains makeChange function"""


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1

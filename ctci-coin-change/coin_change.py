#!/bin/python3

import sys


memoized = {}


def hash_key(coins, n):
    return '%s:%s' % ('-'.join(map(str, coins)), n)


def _make_change(coins, n):
    key = hash_key(coins, n)
    if key in memoized:
        return memoized[key]

    if n < 0:
        return 0

    if n == 0:
        return 1

    if len(coins) == 0:
        return 0

    coin, rest = coins[0], coins[1:]

    if coin == n:
        return 1

    value = _make_change(coins, n-coin) + _make_change(rest, n)
    memoized[key] = value
    return value


def make_change(coins, n):
    coins.sort()
    return _make_change(coins, n)

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))

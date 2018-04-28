from functools import reduce
from collections import defaultdict


def letter_count(string):
    def reducer(agg, cur):
        agg[cur] += 1
        return agg

    return reduce(reducer, string, defaultdict(int))


def deletions_needed(a, b):
    acc = 0
    all_keys = set(a.keys()) | set(b.keys())
    for key in all_keys:
        acc += abs(a.get(key, 0) - b.get(key, 0))
    return acc


def number_needed(a, b):
    lc_a = letter_count(a)
    lc_b = letter_count(b)
    return deletions_needed(lc_a, lc_b)


a = input().strip()
b = input().strip()


print(number_needed(a, b))

#!/bin/python3

import sys

SWAPS = 0
def merge_halves(arr, left_half, right_half):
    # print('merge_halves(%r, %r, %r)' % (arr, left_half, right_half))
    global SWAPS

    left_half_start, left_half_end = left_half
    right_half_start, right_half_end = right_half

    idx = left_half_start

    left_arr = arr[left_half_start:left_half_end+1]
    right_arr = arr[right_half_start:right_half_end+1]
    left_idx, right_idx = 0, 0

    sorted_value = []
    while True:
        if left_arr[left_idx] > right_arr[right_idx]:
            sorted_value.append(right_arr[right_idx])
            print('left_arr[left_idx]=%d' % left_arr[left_idx])
            print('right_arr[right_idx]=%d' % right_arr[right_idx])
            print('right_idx=%d, right_half_start=%d' % (right_idx, right_half_start))
            print('left_idx=%d, left_half_start=%d' % (left_idx, left_half_start))
            print('swaps=%d' % (right_idx + right_half_start - left_idx - left_half_start))
            print('------')
            SWAPS += (right_idx + right_half_start - left_idx - left_half_start)
            right_idx += 1
        else:
            sorted_value.append(left_arr[left_idx])
            left_idx += 1
        if left_idx >= len(left_arr) or right_idx >= len(right_arr):
            break

    sorted_value += left_arr[left_idx:]
    sorted_value += right_arr[right_idx:]

    arr[left_half_start:right_half_end+1] = sorted_value


def merge_sort(arr, left_start, right_end):
    # print('merge_sort(%r, %r, %r)' % (arr, left_start, right_end))
    if left_start >= right_end:
        return

    middle = int((left_start + right_end) / 2)
    merge_sort(arr, left_start, middle)
    merge_sort(arr, middle+1, right_end)
    merge_halves(arr, (left_start, middle), (middle+1, right_end))
    return arr


def countInversions(arr):
    return merge_sort(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        SWAPS = 0
        countInversions(arr)
        print(SWAPS)

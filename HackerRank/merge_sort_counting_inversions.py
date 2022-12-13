#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def merge_sort(arr, count):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]

        right = arr[mid:]

        count = merge_sort(left, count)

        count = merge_sort(right, count)

        l_idx = r_idx = k = 0

        while l_idx < len(left) and r_idx < len(right):
            if left[l_idx] > right[r_idx]:
                arr[k] = right[r_idx]
                r_idx += 1
                count += mid - l_idx
            else:
                arr[k] = left[l_idx]
                l_idx += 1
            k += 1

        while l_idx < len(left):
            arr[k] = left[l_idx]
            l_idx += 1
            k += 1

        while r_idx < len(right):
            arr[k] = right[r_idx]
            r_idx += 1
            k += 1
    return count


def countInversions(arr):
    return merge_sort(arr, count = 0)


if __name__ == '__main__':
    arr = [7, 5, 3, 1]

    print(countInversions(arr))

    print(arr)
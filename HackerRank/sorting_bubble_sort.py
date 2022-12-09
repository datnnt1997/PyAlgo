#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#


def countSwaps(a):
    min = a[0]
    max = a[0]
    swap = 0
    for i in range(len(a)):
        max = a[i] if a[i] > max else max
        for j in range(len(a) - 1):
            min = a[j] if a[j] < min else min
            if a[j] > a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
                swap += 1
    print(f"Array is sorted in {swap} swaps.")
    print(f"First Element: {min}")
    print(f"Last Element: {max}")


if __name__ == '__main__':
    a = [6, 4, 1]
    countSwaps(a)

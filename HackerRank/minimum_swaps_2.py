#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    cached = {}
    for i, n in enumerate(arr):
        if n != i + 1:
            while n in cached:
                n = cached.pop(n)
            if n != i + 1:
                cached[i+1] = n
                count+=1
    return count


if __name__ == '__main__':
    arr = [5, 3, 1, 2]
    print(minimumSwaps(arr))



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

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]

        right = arr[mid+1:]

        merge_sort(left)

        merge_sort(right)

        i = j = len(left)

        while i


def countInversions(arr):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

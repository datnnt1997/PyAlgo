#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # Write your code here
    hash_table = {}
    count = 0
    for a in arr:
        if a - k in hash_table:
            count += 1
        if a + k in hash_table:
            count += 1
        hash_table[a] = a
    return count


if __name__ == '__main__':

    k = 2
    arr = [1, 5, 3, 4, 2]

    print(pairs(k, arr))

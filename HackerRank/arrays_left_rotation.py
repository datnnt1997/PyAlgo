#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    return a[d:] + a[:d]


if __name__ == '__main__':
    n = 5
    d = 4
    a = [1, 2, 3, 4, 5]
    print(rotLeft(a, d))

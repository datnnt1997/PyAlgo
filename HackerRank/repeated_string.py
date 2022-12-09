#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeatedString(s, n):
    len_s = len(s)
    return s.count('a') * (n // len_s) + s[: n % len_s].count('a')


if __name__ == '__main__':
    s = 'aba'
    n = 10

    print(repeatedString(s, n))

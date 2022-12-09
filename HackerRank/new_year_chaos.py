#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    moves = 0
    q = [P - 1 for P in q]
    for i, P in enumerate(q):
        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P - 1, 0), i):
            if q[j] > P:
                moves += 1
    print(moves)


if __name__ == '__main__':
    t = [[2, 1, 5, 3, 4], [2, 5, 1, 3, 4], [1, 2, 5, 3, 7, 8, 6, 4]]

    for q in t:
        minimumBribes(q)



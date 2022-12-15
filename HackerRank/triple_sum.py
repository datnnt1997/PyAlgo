#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the triplets function below.
def triplets(a, b, c):
    # p < q and q > r
    a_idx, c_idx = 0, 0
    num_p, num_c = 0, 0
    count = 0
    for q in set(b):
        while a_idx < len(a) and a[a_idx] <= q:
            num_p += 1
            a_idx += 1
        while c_idx < len(c) and c[c_idx] <= q:
            num_c += 1
            c_idx += 1
        count += math.comb(num_p, 1) * math.comb(num_c, 1)
    return count


if __name__ == '__main__':
    arra = [1, 3, 5]

    arrb = [2, 3]

    arrc =  [1, 2, 3]

    print(triplets(arra, arrb, arrc))


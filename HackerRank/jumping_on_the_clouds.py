#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    num_jumps, curr_step = 0, 0
    while curr_step < len(c) - 1:
        curr_step += 2 if curr_step + 2 < len(c) and c[curr_step+2] == 0 else 1
        num_jumps += 1
    return num_jumps

if __name__ == '__main__':
    c = [0, 0, 1, 0, 0, 1, 0]
    print(jumpingOnClouds(c))

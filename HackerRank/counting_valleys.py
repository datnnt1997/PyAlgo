#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    sea_lv = 0
    start_velley = False
    velley_counter = 0
    for p in path:
        if p == 'U':
            sea_lv += 1
            if sea_lv == 0 and start_velley:
                velley_counter += 1
                start_velley = False
        else:
            sea_lv -= 1
            if sea_lv < 0 and not start_velley:
                start_velley= True
    return velley_counter

if __name__ == '__main__':
    steps = 8
    path = 'UDDDUDUU'

    print(countingValleys(steps, path))

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#


def whatFlavors(cost, money):
    hash_table = {}

    for idx, c in enumerate(cost):
        if c in hash_table:
            if idx + 1 < hash_table[c]:
                print(f"{idx + 1} {hash_table[c]}")
            else:
                print(f"{hash_table[c]} {idx + 1}")
        hash_table[money - c] = idx + 1


if __name__ == '__main__':

    cost = [1, 4, 5, 3, 2]
    money = 4
    whatFlavors(cost, money)

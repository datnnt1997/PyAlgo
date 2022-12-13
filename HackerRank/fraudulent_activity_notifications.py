#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def get_median(count_arr, median_idx):
    sum_count = 0
    for i in range(201):
        # if i in count_arr:
        sum_count += count_arr[i]
        if sum_count >= median_idx:
            return i


def activityNotifications(expenditure, d):
    count = 0
    count_array = [0] * 201

    for i in range(len(expenditure) - 1):
        count_array[expenditure[i]] += 1
        if i >= d - 1:
            if not len(expenditure[i - (d - 1): i + 1]) == d:
                return count
            if d % 2 == 0:
                twice_median = 2 * ((get_median(count_array, d // 2) +
                                     get_median(count_array, d // 2 + 1)) / 2)
            else:
                twice_median = 2 * get_median(count_array, d / 2)
            if expenditure[i + 1] >= twice_median:
                count += 1
            count_array[expenditure[i - d + 1]] -= 1
    return count


if __name__ == '__main__':
    d = 4
    expenditure = [1, 2, 3, 4, 4]
    print(activityNotifications(expenditure, d))
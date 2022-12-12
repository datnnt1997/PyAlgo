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

#
# def activityNotifications(expenditure, d):
#     freq = {}
#     notify=0
#     def find(idx):
#         total_count = 0
#         for i in range(201):
#             if i in freq:
#                 total_count = total_count + freq[i]
#             if total_count >= idx:
#                 return i
#     for i in range(len(expenditure)-1):
#         if expenditure[i] in freq:
#             freq[expenditure[i]]+=1
#         else:
#             freq[expenditure[i]]=1
#         #print(f"i: {i},val: {expenditure[i]}, freq: {freq}")
#         if i>=d-1:
#             if d%2 ==0:
#                 median = (find(d//2)+find(d//2+1))/2
#             else:
#                 median = find(d/2)
#             #print("median: ",median)
#             if expenditure[i+1]>= (median*2) :
#                 notify +=1
#                 print("notify: ",notify)
#             #remove the previous element from dictionary
#             freq[expenditure[i-d+1]]-=1
#
#     return notify

#
# def get_median(count_arr, median_idx):
#     sum_count = 0
#     for i in range(201):
#         if i in count_arr:
#             sum_count += count_arr[i]
#         if sum_count >= median_idx:
#             return i
#
#
# def activityNotifications(expenditure, d):
#     count = 0
#     count_array = {}
#
#     for i in range(len(expenditure)-1):
#         if expenditure[i] in count_array:
#             count_array[expenditure[i]] += 1
#         else:
#             count_array[expenditure[i]] = 1
#         if i >= d - 1:
#             if not len(expenditure[i-(d-1): i+1]) == d:
#                 return count
#             if d % 2 == 0:
#                 twice_median = 2 * ((get_median(count_array, d // 2) +
#                                     get_median(count_array, d // 2 + 1)) / 2)
#             else:
#                 twice_median = 2 * get_median(count_array, d / 2)
#             if expenditure[i+1] >= twice_median:
#                 count += 1
#             count_array[expenditure[i-d+1]] -= 1
#
#     return count


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

    # lines = open('case.txt', 'r').readlines()
    #
    # d = int(lines[0].split()[-1])
    # expenditure = [int(i) for i in lines[1].split()]
    d = 4
    expenditure = [1, 2, 3, 4, 4]
    print(activityNotifications(expenditure, d))
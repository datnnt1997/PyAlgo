#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
from tqdm import tqdm


class SegmentTreeNode:
    def __init__(self, start, end, value):
        self.start = start
        self.end = end
        self.mid = self.__get_mid()
        self.value = value
        self.left_child: SegmentTreeNode = None
        self.right_child: SegmentTreeNode = None
        self.max_child_value = 0

    def __get_mid(self):
        return (self.start + self.end) // 2


def update_node(node, ss, se, value):
    if ss <= node.start and se >= node.end:
        node.value += value
        return node.max_child_value + node.value
    if se < node.start or ss > node.end:
        return node.max_child_value + node.value

    # if (ss >= node.start and ss <= node.mid) or (se <= node.mid and se >= node.start) or (ss >= node.start and se <= node.mid):
    if not (se < node.start or ss > node.mid):
        if node.left_child is None:
            node.left_child = SegmentTreeNode(node.start, node.mid, 0)
        max_left = update_node(node.left_child, ss, se, value)
    else:
        if node.left_child is not None:
            max_left = node.left_child.max_child_value + node.left_child.value
        else:
            max_left = 0
    # if (ss >= node.mid+1 and ss <= node.end) or (se <= node.end and se >= node.mid+1) or (ss >= node.mid+1 and se <= node.end):
    if not (se < node.mid + 1 or ss > node.end):
        if node.right_child is None:
            node.right_child = SegmentTreeNode(node.mid+1, node.end, 0)
        max_right = update_node(node.right_child, ss, se, value)
    else:
        if node.right_child is not None:
            max_right = node.right_child.max_child_value + node.right_child.value
        else:
            max_right = 0

    max_value = max(max_left, max_right)

    node.max_child_value = max_value
    return node.max_child_value + node.value


def solution2ArrayManipulation(n, queries):
    st_root = SegmentTreeNode(start=1, end=n, value=0)
    for q in tqdm(queries):
        update_node(st_root, ss=q[0], se=q[1], value=q[2])
    return st_root.max_child_value + st_root.value


def arrayManipulation(n, queries):
    arr = [0] * n
    max_value, sum_value = 0, 0
    for q in queries:
        arr[q[0]-1] += q[2]
        arr[q[1]] -= q[2]
    for i in range(n):
        sum_value += arr[i]
        max_value = max(sum_value, max_value)
    return max_value


if __name__ == '__main__':

    n = 10
    queries = [
        [1, 5, 3],
        [4, 8, 7],
        [6, 9, 1]
    ]

    print(arrayManipulation(n, queries))

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
            continue
        tmp = grade % 5
        if 5 - tmp < 3:
            rounded_grades.append(grade + 5 - tmp)
        else:
            rounded_grades.append(grade)
    return rounded_grades


if __name__ == '__main__':

    grades = [4, 73, 67, 38, 33]

    result = gradingStudents(grades)

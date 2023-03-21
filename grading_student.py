#!/bin/python3

import math
import os
import random
import re
import sys



def gradingStudents(grades):
    grade_lst = []
    for grade in grades:
        if grade < 38:
            grade_lst.append(grade)
        else:
            last_digit = grade % 10
            if last_digit > 5:
                check_digit = 10 - last_digit
            else:
                check_digit = 5 - last_digit
            if check_digit < 3:
                grade_lst.append(grade + check_digit)
            else:
                grade_lst.append(grade)
            
    return grade_lst

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip()) 
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

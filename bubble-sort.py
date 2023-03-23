#!/bin/python3

import math
import os
import random
import re
import sys

def countSwaps(a):
    numSwaps = 0
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if(a[j] > a[j +1]):
                temp = a[j]
                a[j] = a[j +1]
                a[j + 1] = temp
                numSwaps += 1
                        
    firstElement = a[0]
    lastElement = a[len(a) - 1]
    print(f'Array is sorted in {numSwaps} swaps.')
    print(f'First Element: {firstElement}')
    print(f'Last Element: {lastElement}')
     
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

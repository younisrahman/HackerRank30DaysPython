#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    totalswap = 0

    # Write your code here
    for i in range(n):
        numberOfSwaps = 0
        for j in range((n-1)):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                numberOfSwaps = numberOfSwaps + 1
                totalswap = totalswap + 1
        if numberOfSwaps == 0:
            break

    print(f"Array is sorted in {totalswap} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[n-1]}")

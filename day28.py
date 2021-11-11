#!/bin/python3

import math
import os
import random
import re
import sys


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]gmail.com'
database = {}
if __name__ == '__main__':
    N = int(input().strip())

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        database[emailID] = firstName

    sort_name = dict(sorted(database.items(), key=lambda item: item[1]))
    for key, value in sort_name.items():
        if re.search(regex, key):
            print(value)

# 6
# riya riya@gmail.com
# julia julia@julia.me
# julia sjulia@gmail.com
# julia julia@gmail.com
# samantha samantha@gmail.com
# tanya tanya@gmail.co

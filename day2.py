import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip = meal_cost / 100 * tip_percent
    tax =  meal_cost / 100 * tax_percent
    sum = int(round(meal_cost + tip + tax))
    # print(sum)
    return sum

# if __name__ == '__main__':
# meal_cost = float(input().strip())

# tip_percent = int(input().strip())

# tax_percent = int(input().strip())

print(solve(12.00, 20, 8))
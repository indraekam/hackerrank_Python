#!/bin/python3

import math
import os
import random
import re
import sys

def task_fucn(n):
    if not (1 <= n <= 100):
        raise ValueError('Input out of range (1 - 100)')
        
    if n % 2 != 0:
        return 'Weird'
    elif n in range(2, 6):
        return 'Not Weird'
    elif n in range (6,21):
        return 'Weird'
    else:
        return 'Not Weird'
    

if __name__ == '__main__':
    try:
        n = int(input().strip())
        result = task_fucn(n)
        print(result)
    except ValueError as e:
        print(f'Invalid input :{e}')

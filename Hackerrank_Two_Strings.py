# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:42:33 2020

@author: user
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    for i in s1:
        if i in s2:
            return "YES"
            break
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
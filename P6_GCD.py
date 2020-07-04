#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:54:39 2020

@author: adityadubey
"""
"""
Write a function called gcd that calculates the greatest common divisor of two positive 
integers. The gcd of two or more integers, when at least one of them is not zero, is 
the largest positive integer that divides the numbers without a remainder.
One way is recursively, where the greatest common denominator of a and b can be 
calculated as gcd(a, b) = gcd(b, a mod b). Hint: remember the mod symbol is % in Python. 
Do not import anything.
For example, the greatest common divisor (gcd) between a = 20 and b = 12 is:
gcd(20,12) is the same as gcd(12, 20 mod 12) = gcd(12,8)
gcd(12,8) is the same as gcd(8, 12 mod 8) = gcd(8,4)
gcd(8,4) is the same as gcd(4, 8 mod 4) = gcd(4,0)
The gcd is found (and the gcd is equal to a) when we reach 0 for b.

"""

#Solution1: List Comprehension
def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    return max([i for i in range(1,max(int(a),int(b))+1) if int(a)%i ==0 and int(b)%i ==0])


# Solution2: Iteration & List
def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    l1 = []
    for i in range(1,max(int(a),int(b))+1):
        if int(a)%i ==0 and int(b)%i ==0:
            l1.append(i)
    return max(l1)


# Solution3: through Recurssion
def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    if min(int(a),int(b)) == 0:
        return max(int(a),int(b))
    else:
        return(gcd(min(int(a),int(b)),max(int(a),int(b))%min(int(a),int(b))))





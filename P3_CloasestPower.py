#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 10:52:19 2020

@author: adityadubey
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    x = 1
    for i in range(0,int(num)):
        if abs(int(base)**i - int(num)) < abs(int(base)**x - int(num)):
            x = i
        elif abs(int(base)**i - int(num)) == abs(int(base)**x - int(num)) and i < x:
            x = i
    return x

print(closest_power(10, 550.0))
        
        

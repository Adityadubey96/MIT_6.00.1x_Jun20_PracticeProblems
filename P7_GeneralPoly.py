#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:45:02 2020

@author: adityadubey
"""
"""
Write a function called general_poly, that meets the specifications below. 
For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because
1∗103+2∗102+3∗101+4∗100 .
"""

L = [1, 2, 3, 4] # Test Case

#Solution 1: Iteration over a Function within the Function
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    """
    def f(x):
        sum = 0
        for i in range(len(L)):
            sum += L[i]*x**(len(L)-1-i)
        return sum
    return f


#Solution 2: Using List Comprehenssion within Function.
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    """
    def f(x):
        return sum([L[i]*x**(len(L)-1-i)for i in range(len(L))])
    return f


print(general_poly(L)(10)) #Output Test Case
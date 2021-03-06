#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 20:14:35 2020

@author: adityadubey
"""
def f(i):
    return i + 2

def g(i):
    return i%2 == 0

L = [0, -10, 5, 6, -4, -5]

# print(applyF_filterG(L, f, g))
# print(L)
# Should print:6
# [5, 6]

#Solution1: Using Simple Iteration
def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
       returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    L_Copy = L[:]
    for i in range(len(L_Copy)):
        if g(f(L_Copy[i])) == False:
            L.remove(L_Copy[i])

    return L

#Solution2: Using Iteration over List Comprehenssion
def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
       returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    for i in ([i for i in L if g(f(i)) == False]):
        L.remove(i)
    return L


print(applyF_filterG(L, f, g))



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 12:21:57 2020

@author: adityadubey
"""
# Write a function to flatten a list. The list contains other lists, strings, or ints.
#For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).


l = [(1,'a',['cat'],2),[[3],'dog'],4,5] #TestCase


#Solution 1: Iterative Recurssion
def flatten(l):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    f = []
    for i in l:
        if type(i) == list or type(i) == tuple:
            f.extend(flatten(i))
        else:
            f.append(i)
    return f


print(flatten(l)) #OutputTestCase
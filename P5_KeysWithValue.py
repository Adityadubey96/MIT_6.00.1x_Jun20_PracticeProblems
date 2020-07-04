#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:42:12 2020

@author: adityadubey
"""
"""
Write a Python function that returns a list of keys in aDict with the value target. 
The list of keys you return should be sorted in increasing order. 
The keys and values in aDict are both integers. 
*(If aDict does not contain the value target, you should return an empty list.)
This function takes in a dictionary and an integer and returns a list.
"""


aDict = {1:7,2:8,5:9,4:8,6:8,3:9} #TestCase
target = 8 #TestCase


# Solution1: Using Iterative Loops
def keysWithValue(aDict, target):
    """
    aDict: a dictionary
    target: an integer
    """
    r = []
    for i in aDict:
        if aDict[i] == target:
            r.append(i)
    r.sort()
    return r


# Solution2: Using List Comprehenssion
def keysWithValue(aDict, target):
    """
    aDict: a dictionary
    target: an integer
    """
    
    return sorted([i for i in aDict if aDict[i] == target])


print(keysWithValue(aDict, target)) #OutputTestCase
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 17:10:15 2020

@author: adityadubey
"""

# then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
# If f(a, b) returns a > b
# d1 = {1:30, 2:20, 3:30}
# d2 = {1:40, 2:50, 3:60}
# then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})

d1 = {1:30, 2:20, 3:30, 5:80}  #TestCase1
d2 = {1:40, 2:50, 3:60, 4:70, 6:90} #TestCase1


def f(a,b):
    return a>b


def dict_interdiff(d1, d2):
    """
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    """
    d3 ={}
    d4 ={}
    for i in d1:
        if i in d2:
            d3[i] = f(d1[i],d2[i])
            del d2[i]
        else:
            d4[i] = d1[i]
    if len(d2)>0:
        for i in d2:
            d4[i]=d2[i]
    return (d3,d4)


print(dict_interdiff(d1, d2)) #TestCase1 Output
            
    

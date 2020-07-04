#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 16:10:24 2020

@author: adityadubey
"""


# For example, if L = [[1, 2], [3, 4], [5, 6, 7]] 
#then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]

L = [[1, 2], [3, 4,[5,6]], [7, 8, 9]]  #TestCase


def deep_reverse(L):
     """ assumes L is a list of lists whose elements are ints
     Mutates L such that it reverses its elements and also 
     reverses the order of the int elements in every element of L. 
     It does not return reversed list.
     """
     L.reverse()
     for i in L:
         if type(i) == list:
             deep_reverse(i)
     return L
    
    
print(L)  #OutputTestCase  
             
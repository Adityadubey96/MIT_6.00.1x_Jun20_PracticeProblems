#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:36:28 2020

@author: adityadubey
"""
listA = [1, 2, 3]
listB = [4, 5, 6]

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    x= 0
    for i in range(min(len(listA),len(listB))):
        x += listA[i]*listB[i]
    return x
    
print(dotProduct(listA, listB))
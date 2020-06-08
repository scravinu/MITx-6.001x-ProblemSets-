#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:03:41 2020

@author: Sharad
"""
#program to count the number of vowels
vcount = 0
vowels = ['a','e','i','o','u']
for eachS in s:
    if eachS in vowels:
        vcount +=1
print('Numer of vowels: '+ str(vcount))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:58:34 2020

@author: Sharad
"""
#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s. 
#For example, if s = 'azcbobobegghakl', then your program
# Paste your code into this box \
bobCount = 0
bobLen = len('bob')
for es in enumerate(s):
    if es[0] + bobLen <= len(s):
        nextThreeLetters = es[1]+s[(es[0]+1)]+s[(es[0]+2)] 
        if nextThreeLetters == 'bob':
            bobCount+=1
print("Number of times bob occurs is: "+str(bobCount))
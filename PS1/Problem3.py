#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:14:50 2020

@author: Sharad
"""

"""Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', 
then your program should print"""

s = 'zyxwvutsrqponmlkjihgfedcba'
index = 0
longst_string = ''
final_long_string = ''
for eachs in s:
    if index==0:
        index+=1
        final_long_string+=eachs
        continue
    if eachs >= s[index-1]:
        if not longst_string:#
            longst_string+=s[index-1]+eachs
        else:
            longst_string+=eachs
        if len(longst_string)>len(final_long_string):
            final_long_string=longst_string
            
        index+=1
    else:
        longst_string='' #chain broken longst string counter restarts
        index+=1

print (final_long_string)

# ctr = 0;
# os=''
# ns = ''
# flag=0
# for char in s:
#     if ctr == 0:
#         ns = ns + char
#         ctr = ctr + 1
#         continue
#     if ord(char)>ord(s[ctr-1]) or ord(char) == ord(s[ctr-1]) :
#         ns = ns + char
#         ctr = ctr + 1
#         continue
#     elif len(ns) > len(os) and len(ns) > 1:
#         os = ns
#         ns = s[ctr]
#         ctr = ctr + 1
#         flag = 1
#     else:
#         ns = s[ctr]    
#         ctr = ctr + 1
        
# if flag == 1:
#     print('Longest substring in alphabetical order is: ' + os) 
# else:
#     print('Longest substring in alphabetical order is: ' + ns) 
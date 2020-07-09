#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 18:21:56 2020

@author: Sharad
"""

# def count7(N):
#     if N == 0:
#         return 0
#     elif N % 10 == 7:
#         return 1 + count7(N//10)
#     else:
#         return 0 + count7(N//10)

def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            #PLACE A LINE OF CODE HERE
            return s2
            
        if s2 == '':
            #PLACE A LINE OF CODE HERE
            return s1
        else:
            #PLACE A LINE OF CODE HERE
            return s1[0] + helpLaceStrings(s2,s1[1:],'')
    return helpLaceStrings(s1, s2, '')

def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    #YOUR CODE HERE
    import string 
    superset = string.ascii_lowercase
    newWord = word.lower()
    letterScores = []
    ctr = -1
    for letter in newWord:
        ctr = ctr + 1
        letterScore = (superset.index(letter) + 1) * ctr
        letterScores.append(letterScore)
    highScore1 = max(letterScores)
    letterScores.pop(letterScores.index(highScore1))
    highScore2 = max(letterScores)
    return f(highScore1,highScore2)

def f(n1,n2):
    return n1 + n2


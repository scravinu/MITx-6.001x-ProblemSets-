#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:48:39 2020

@author: Sharad
"""

# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
 
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    ret_string=''
    for i in secretWord:
        if i in lettersGuessed:
            ret_string +=i
        else:
            ret_string +='_ '
    return ret_string 

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    super_string = (string.ascii_lowercase)
    for i in lettersGuessed:
            if i in super_string:
                l = super_string.index(i)
                super_string = super_string[:l]+super_string[l+1:]
    return super_string
def wincheck(secretWord,GuessedWord):
    '''
    returns true if both strings are the same , signalling victory
    '''
    return (secretWord == GuessedWord)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed=[]
    numofGuesses = 8
    avlblLetters = ''
    print('Welcome to the game Hangman!\n')
    print('The word I am thinking is '+str(len(secretWord))+' characters long\n')
    print('------------------------------------------------------------------\n')
    
    while numofGuesses > 0:
         print('You have '+str(numofGuesses)+' guesses left\n')
         avlblLetters = getAvailableLetters(lettersGuessed)
         print('Available Letters: '+ avlblLetters+'\n')
         guess = input (' Please guess a letter : ')
         guess_LC = guess.lower()
         if guess_LC not in lettersGuessed: 
            lettersGuessed.append(guess_LC)
            if guess_LC in secretWord:
                print('Good Guess: '+ getGuessedWord(secretWord, lettersGuessed)+'\n' )
                if isWordGuessed(secretWord,lettersGuessed):
                    print('Congratulations you won!\n')
                    break
                else:
                    continue
                
            else:
                print('Oops! that letter not in my word: ' + getGuessedWord(secretWord, lettersGuessed)+'\n')
                numofGuesses = numofGuesses - 1
                if numofGuesses == 0 :
                    print ('Sorry you ran out of Guesses, the word was : ' + secretWord + '\n')
                    break
            
                continue
            
         else :
            print('Oops! you have already guessed that letter : ' + getGuessedWord(secretWord, lettersGuessed)+'\n')
            continue
        
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
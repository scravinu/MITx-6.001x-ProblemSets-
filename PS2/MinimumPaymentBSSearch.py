#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 03:04:29 2020

@author: Sharad
"""

balance = 99999999
annualInterestRate = 0.18
#monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12
totalPayment = 0
fixMonthlyPayment = 0
cantPay = True
lowBoundFMP = balance/12
upBoundFMP = round(((balance * (1 + monthlyInterestRate)**12) / 12),2)
tol = 0.01

def cantPayOff(balance,fixMonthlyPayment):
    for month in range(1,13):
        #totalPayment += fixMonthlyPayment
        unpaidBalance = balance - fixMonthlyPayment
        if unpaidBalance <=0:
            return False
        balance = unpaidBalance + monthlyInterestRate * unpaidBalance
    return True

while round((upBoundFMP - lowBoundFMP),2) >= tol :
    midFMP = (lowBoundFMP + upBoundFMP)/2
    if  cantPayOff(balance,midFMP):
        lowBoundFMP = midFMP
    else:
        upBoundFMP = midFMP
            
    
        
        

#print('total payments made = '+str(round(totalPayment,2)))
print('Lowest Payment: ', str(round(midFMP,2)))
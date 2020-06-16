#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 03:04:29 2020

@author: Sharad
"""

balance = 3926
annualInterestRate = 0.2
#monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12
totalPayment = 0
fixMonthlyPayment = 0
cantPay = True

def payOff(balance,fixMonthlyPayment):
    for month in range(1,13):
        #totalPayment += fixMonthlyPayment
        unpaidBalance = balance - fixMonthlyPayment
        if unpaidBalance <=0:
            return False
        balance = unpaidBalance + monthlyInterestRate * unpaidBalance
    return True

while cantPay:
    fixMonthlyPayment+=10
    cantPay = payOff(balance,fixMonthlyPayment)
    
        
        

#print('total payments made = '+str(round(totalPayment,2)))
print('Lowest Payment: ', str(round(fixMonthlyPayment,2)))
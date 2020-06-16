#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 03:04:29 2020

@author: Sharad
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12
totalPayment = 0

for month in range(1,13):
    minMonthlyPayment = monthlyPaymentRate * balance
    totalPayment += minMonthlyPayment
    unpaidBalance = balance - minMonthlyPayment
    balance = unpaidBalance + monthlyInterestRate * unpaidBalance
   
#print('total payments made = '+str(round(totalPayment,2)))
print('Remaining balance: ', str(round(balance,2)))
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 05:48:33 2018

@author: Curtis Burkhalter
"""

#create a program that asks someone to enter their name and their age. Print
#out the message addressed to them that tells them the year they
#will turn 100 years old

from datetime import datetime

c_year = datetime.now().year

name = input("Give me your name: ")

age = input("What is your age: ")
#print("You will turn 100 in the year )

print("Your name is " + name + " and you are " + age)

print("You will be 100 years old in the year " + str(c_year + 100 - int(age)))

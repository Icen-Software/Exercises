# Chapter 11: Regular Expressions
# Exercise 1
#
# Assignment is to use regular expressions to find all numbers in a text file, convert them to integers and sum them

# Importing regular expressions module
import re
# Standard ask for input with default value for quick testing
fname = input("Enter file name:")
if len(fname) < 1:
    fname = "regex_sum_2423570.txt"
fhandle = open(fname)
# read() method to store text contents in a variable
text = fhandle.read()
# Using regex to find all numbers, from 0 through 9, of length 1 and above
numbers = re.findall('[0-9]+',text)
# Zero var followed by for loop that converts all strings into integers and summing it
total = 0
for n in numbers:
    total = total + int(n)
print(total)
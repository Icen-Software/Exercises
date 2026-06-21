# Chapter 3: Conditional Execution
# Exercise 2
#
# Assignment is to write a script that returns a letter grade for a score input, while also adding a 'try and except' to catch bad user input

score = input("Enter Score: ")
# Try to float user input, if not a valid number (i.e. string) then return error message
try:
    fscore = float(score)
except:
    print("Must be a number from 0.0 to 1.0")
# Grading number through descending elif conditions
if fscore >= float(0.9):
    print("A")
elif fscore >= float(0.8):
    print("B")
elif fscore >= float(0.7):
    print("C")
elif fscore >= float(0.6):
    print("D")
else:
    print("F")
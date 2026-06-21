# Chapter 2: Variables, expressions and statements
# Exercise 2
#
# Only the first line of code was given. Assignment was to write a script that can calculate gross pay.

# Collecting info from use input and storing in variables
hrs = input('Enter Hours:')
rate = input('Enter Rate of Pay:')

# Turning input from integer to floating point, multiplying them and storing result in new var
pay = float(hrs) * float(rate)

# Print result
print('Pay:', pay)
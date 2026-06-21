# Chapter 4: Functions
# Exercise 1
#
# Assignment is similar to exercise with gross pay with overtime, but this time using a function

# Defining function computepay
def computepay(h, r):
    p = 0
    # Overtime bonus condition
    if h > 40:
        p = p + 40 * r
        h = h - 40
        p = p + h * (r*1.5)
    else:
        p = p + (h * r)
    return p

# Collecting user input and floating it
hrs = input("Enter Hours:")
rate = input("Enter Rate of Pay:")
h = float(hrs)
r = float(rate)
p = computepay(h, r)

print("Pay", p)
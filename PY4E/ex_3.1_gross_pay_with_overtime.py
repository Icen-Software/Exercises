# Chapter 3: Conditional Execution
# Exercise 1
#
# Assignment is similar to previous one with computing gross pay
# but with the added condition of computing bonus pay for hours worked above 40

# Collecting input and converting to float
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

# Setting initial var
pay = 0

# Condition if hours worked is above 40 for extra pay
if h > 40 :
    # Calculate 40 hours of pay and store it
    pay = pay + (40 * r)
    # Remove 40 hours of work from var
    h = h - 40
    # Adjust pay rate for overtime
    r = r * float(1.5)
    # Add remaining hours times adjusted rate to pay var
    pay = pay + h * r
    print(pay)
# else condition if hours is less than 40
else:
    pay = h * r
    print(pay)
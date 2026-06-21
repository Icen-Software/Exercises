# Chapter 5: Loops and Iterations
# Exercise 1
#
# Assignment is to write a script that prompts for integers until the user inputs 'done'
# then finding the largest and smallest integers and printing them.

#Initial var setup
largest = None
smallest = None
# while loop to prompt for integers
while True:
    num = input("Enter a number: ")
    # Condition to check for breaking the loop by user input
    if num == "done":
        break
    # Converting string to integer, with except for bad input
    try:
        fnum = int(num)
    except:
        print("Invalid input")
        continue
    # If variables are empty then add first number seen since first number seen = smallest and largest number thus far
    if largest is None:
        largest = fnum
    if smallest is None:
        smallest = fnum
    # Check if number is larger than or smaller than current number in variable
    if largest < fnum:
        largest = fnum
    if smallest > fnum:
        smallest = fnum

print("Maximum is", largest)
print("Minimum is", smallest)
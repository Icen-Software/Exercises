# Chapter 7: Files
# Exercise 1
#
# Assignment is similar to previous one with finding desired value in a string but this time
# it's extracting from a .txt file, with multiple lines, and then calculating the average of all the float values

# Asking for file name, storing it and opening it
fname = input("Enter file name: ")
fh = open(fname)
# Initial var setup
count = 0
total = 0
# for loop to go line by line in opened file
for line in fh:
    # Ignoring lines that dont contain desired information by checking for starting text
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # Adding 1 to count variable for each value found
    count = count + 1
    # Finding colon position
    colpos = line.find(':')
    # Extracting value after colon position and converting to float
    value = float(line[colpos+1:])
    # Adding up values to total variable
    total = total + value
# Simple division to find average
avg = total / count
print('Average spam confidence:', avg)
# Chapter 8: Lists
# Exercise 2
#
# Assignment is to extract email addresses from a mailbox export file then print out a count of total email addresses seen

# Ask for user input with default file name if input is empty for quick testing
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
# Opening file and setting initial variable
fh = open(fname)
count = 0
for line in fh:
    # rstrip() method to remove all blank space from the right
    line = line.rstrip()
    # Ignoring lines that start with "From:" but not "From"
    if not line.startswith('From'): continue
    if line.startswith('From:'): continue
    # Splitting the string
    words = line.split()
    # Selecting second word (index starts at 0)
    print(words[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")

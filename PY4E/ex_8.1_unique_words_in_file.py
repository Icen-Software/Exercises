# Chapter 8: Lists
# Exercise 1
#
# Assignmet is to write a script that reads through a .txt file and compile a list of unique words

# User input and opening file
fname = input("Enter file name: ")
fh = open(fname)
# Using constructor function to make empty lists
words = list()
lst = list()
# for loop to read through lines
for line in fh:
    # Using split() method to automatically separate lines into individual words
    words = line.split()
    # Nested for loop
    for word in words:
        # Checks if word is new and if so, add it to the list via append() method
        if word not in lst:
            lst.append(word)
# sort() method to sort the list alphabetically
lst.sort()
print(lst)

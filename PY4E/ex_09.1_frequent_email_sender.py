# Chapter 9: Dictionaries
# Exercise 1
#
# Assignment is to read through mailbox export file, count the number of emails and figure out who has sent the most emails.

# User input, default file if empty input, open file
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
# dict() constructor to make empty dictionary
counts = dict()
for line in handle:
    # Skipping lines that aren't relevant
    if not line.startswith("From ") : continue
    # Splitting lines and grabbing emails
    line = line.split()
    emails = line[1]
    # Adding email to dictionary variable, using the get() method to check if it is missing from the dictionary, and if so, add it with a default value of 0. Then adds 1 to the value regardless if it's a new or already present item.
    counts[emails] = counts.get(emails, 0) + 1
# Variables for storing email counts and email senders
maxsender = None
maxcount = None
# for loop with two iteration variables looking through dictionary using items() method to return key and value pairs
for email,count in counts.items() :
    # Cleaner implementation of checking for None value
    if maxcount is None or count > maxcount:
        maxsender = email
        maxcount = count
print(maxsender, maxcount)
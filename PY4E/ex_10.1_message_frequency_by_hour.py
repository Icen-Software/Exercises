# Chapter 10: Tuples
# Exercise 1
#
# Assignment is to pull from mailbox export file and figure out the distribution by hour of the day for each message.

# Ask for input, default file for empty input and opening file
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
# dict() constructor for empty dictionary
counts = dict()
for line in handle:
    wds = line.split()
    # Ignoring lines that can't have emails in them by checking if their length is smaller than 5 words
    # and ignoring it if the first word isn't "From"
    if len(wds) < 5 : continue
    if wds[0] != "From": continue
    # Extracting timestamp
    time = wds[5]
    # Splitting timestamp by the colons
    hms = time.split(":")
    # Taking the first entry, aka hour value, from split timestamp
    hour = hms[0]
    # Counting how many messages received at each hour
    counts[hour] = counts.get(hour, 0) + 1
# Sorting the dictionary keys for ascending hours
lst = sorted(counts.items())
# for loop to grab both the key and value from dictionary
for key, val in lst:
    print(key, val)
        
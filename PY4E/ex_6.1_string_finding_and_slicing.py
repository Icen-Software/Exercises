# Chapter 6: Strings
# Exercise 1
#
# Assignment is to use string finding and slicing to extracted desired numeric value then cnverting it to float

# Text variable given by exercise
text = "X-DSPAM-Confidence:    0.8475"
# Finding the position of the colon character and storing it in a variable
colpos = text.find(':')
# Using string slicing to grab everything after the colon position and store
num = text[colpos+1:]
# Using strip() method to get rid of blank space
num = num.strip()
float(num)
print(num)
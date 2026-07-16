# Chapter 13: Web Services
# Exercise 1
#
# Assignment is to parse and extract values from XML

# Importing necessary modules
import urllib.request
import xml.etree.ElementTree as ET

# Ask for user URL input
url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2423574.xml'

# Opens URL, reads, store data in a string, then use method to extract XML from string
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

# Using findall method to find all nodes named count.
counts = tree.findall('.//count')
nums = list()

# Takes each result from findall, retrieves it as text, then converts to integer
for result in counts:
    nums.append(int(result.text))

print('Count:', len(nums))
print('Sum:', sum(nums))

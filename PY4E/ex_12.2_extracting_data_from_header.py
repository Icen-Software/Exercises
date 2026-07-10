# Chapter 12: Network Programming
# Exercise 2
#
# Assignment is to scrape values from HTML, adding them up and summing them as proof of success

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# Importing urlopen function from urllib.request, import beautifulsoup and ssl libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
# Creates the default secure context from the ssl library
ctx = ssl.create_default_context()

# Disable checking for hostname and sets verification mode to no certificate required
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# URL input and preparing
url = input('Enter - ')

# urlopen method to open url with the set context, using read method to get all text from page
html = urlopen(url, context=ctx).read()

# Using BeautifulSoup's html handler
soup = BeautifulSoup(html, "html.parser")

# Retrieves all tags marked 'span'
tags = soup('span')
# Defining variable
total = 0
for tag in tags:
    # Takes the span tag contents, converts to integer, adds to total variable
    total = total + int(tag.contents[0])
print(total)
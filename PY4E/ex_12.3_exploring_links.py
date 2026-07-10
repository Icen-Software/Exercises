# Chapter 12: Network Programming
# Exercise 3
#
# Assignment is to process a page full of links and go through the nth link an nth amount of times, reporting the last name found

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# or pip install beautifulsoup4 to ensure you have the latest version
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defaults to certificate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# URL input and preparing
url = input('Enter - ')
count = input('Enter position count - ')
repeat = input('Enter depth count - ')
count = int(count)
repeat = int(repeat)
# urlopen method to open url with the set context, using read method to get all text from page
html = urllib.request.urlopen(url, context=ctx).read()
# Using BeautifulSoup's html handler
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

# Creating empty list
href = list()

# Loop that keeps going until repeat (aka depth count) reaches 0
while repeat != 0:
    for tag in tags:
        # Takes href (hyperlinks) values and appends them to list
        href.append(tag.get('href', None))
    # Extracts desired count link from href and stores it
    url = href[count - 1]
    print(url)
    # Repeating process of opening and processing with the new url
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    # Emptying href list
    del href[:]
    # Advancing repeat counter
    repeat = repeat - 1

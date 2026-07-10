# Chapter 12: Network Programming
# Exercise 1
#
# Assignment is to write a script that connects to a specific URL and retrieves HTTP headers

# Import python's socket library for easy socket handling
import socket

# Creating handle for socket, using AF_INET address family, aka Internet Protocol v4, SOCK_STREAM for TCP port
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Using connect method to have the socket connect to url at port 80 (standard HTTP port)
mysock.connect(('data.pr4e.org', 80))

# Setting an HTTP GET command to obtain headers from intro-short.txt on the connected website
# Encode() takes the unicode text and converts it to UTF-8
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

# Sending command from previous line through the socket
mysock.send(cmd)

# Simple loop to receive requested data
while True:
    # recv method set to receive up to 512 characters and store in var data
    data = mysock.recv(512)
    # If received data is less than 1 character, then it's the end of the file, so it breaks the loop
    if len(data) < 1:
        break
    # Printing received data, decoding from UTF-8 to Unicode
    print(data.decode(),end='')

# Closing socket
mysock.close()
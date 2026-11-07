# Program Name: Assignment4.py
# Course: IT3883/Section 01
# Student Name: Jack Rivers
# Assignment Number: Lab#4
# Due Date: 10/6/2026
# Purpose: The client sends a message to the server, listens for a response, then prints out the response found.
# No specific resources used, other than Python functions.

import socket

# set up host and port
HOST = '127.0.0.1'
PORT = 48264

# set up client
client = socket.socket()
client.connect((HOST, PORT))

# send a message to server, then listen for a response
message = input("Message to send: ")
client.send(message.encode())
response = client.recv(1024).decode()

# print response
print("Response:", response)
client.close()

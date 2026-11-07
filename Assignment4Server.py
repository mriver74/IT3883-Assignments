# Program Name: Assignment4.py
# Course: IT3883/Section 01
# Student Name: Jack Rivers
# Assignment Number: Lab#4
# Due Date: 10/6/2026
# Purpose: The client sends a message to the server, listens for a response, then prints out the response found.
# No specific resources used, other than Python functions.

import socket

# set up local host and port
HOST = '127.0.0.1'
PORT = 48264

# set up server and listen for messages
server = socket.socket()
server.bind((HOST, PORT))
server.listen()
print("Listening...")

# once a message is received, covert to uppercase and send back
while True:
    connection, address = server.accept()
    message = connection.recv(1024).decode()
    response = message.upper()
    connection.send(response.encode())
    print("Received:", message)
    print("Sent:", response)
    connection.close()

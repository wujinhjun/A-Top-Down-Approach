# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
# Fill in start
serverName = "localhost"
serverPort = 8080
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
# Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    # Fill in start
    connectionSocket, addr = serverSocket.accept()
    # print(addr)
    # Fill in end
    try:
        # Fill in start
        message = connectionSocket.recv(1024).decode()
        # print(message)
        #Fill in end
        filename = message.split()[1]
        # print(filename)
        f = open(filename[1:])
        # Fill in start
        outputdata = f.read()
        # Fill in end
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.sendall("HTTP/1.1 200 ok\r\n".encode())
        connectionSocket.send("\r\n".encode())
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        print("false")
        # Send response message for file not found
        # Fill in start
        connectionSocket.sendall("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("\r\n".encode())
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data

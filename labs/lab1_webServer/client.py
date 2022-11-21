import sys
from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)


def main():
    if len(sys.argv) != 4:
        print("Error: invalid number for arguments")
    else:
        serverHost = sys.argv[1]
        serverPort = int(sys.argv[2])
        filename = sys.argv[3]
        # print(sys.argv)
        clientSocket.connect((serverHost, serverPort))
        clientSocket.sendall(f'GET /{filename} HTTP/1.1\r\n'.encode())
    while True:
        message = clientSocket.recv(1024).decode()
        if len(message) == 0:
            break
        print(message)
    clientSocket.close()


if __name__ == "__main__":
    main()

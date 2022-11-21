import socket
from numpy import *
import time

serverName = "localhost"
serverPort = 12000
socket.setdefaulttimeout(1)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
timeList = []

for i in range(10):
    print(i)
    startTime = time.time()
    message = f"Ping {i} {startTime}".encode()
    print(message)
    clientSocket.sendto(message, (serverName, serverPort))
    try:
        res, serverAddress = clientSocket.recvfrom(1024)
    except socket.timeout:
        print("Sorry, timeout, your packet is lost")
        continue
    endTime = time.time()
    print(f"RTT {i}: {(endTime - startTime) * 1000:.3f}ms")
    timeList.append(endTime - startTime)
timeList.sort()
maxRTT = timeList[-1]
minRTT = timeList[0]
print(f"max RTT: {maxRTT * 1000:.3f}ms")
print(f"min RTT: {minRTT * 1000:.3f}ms")
print(f"average RTT: {mean(timeList) * 1000:.3f}ms")
clientSocket.close()
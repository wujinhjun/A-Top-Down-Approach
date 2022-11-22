from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
# Fill in start
mailserver = ("smtp-mail.outlook.com", 587)
# Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
# Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO sjtu.edu.cn\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mailFromCommand = "MAIL FROM:<wujinhjun@sjtu.edu.cn>"
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
reptToCommand = "RCPT TO:<wujinhjun@outlook.com>"
clientSocket.send(reptToCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
clientSocket.send("DATA".encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')
# Fill in end

# Send message data.
# Fill in start
messageData = "Hello!\r\nDo you like ketchup?\r\nHow about pickles\r\n"
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(".".encode())
# Fill in end

# Send QUIT command and get server response.
# Fill in start
clientSocket.send("QUIT".encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != 221:
    print('221 reply not received from server.')
# Fill in end

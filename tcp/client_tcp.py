#!/usr/bin/python
# Based on: https://pymotw.com/2/socket/tcp.html

import socket
import sys
import server_info


from main import contador_de_letras


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (server_info.ip, server_info.port)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)
buffer_size = 32



#LE O ARQUIVO
f = open("modelo_entrada.txt", "r")
l = []
for line in f:
    if(len(line) >= 2):
        if line[0]+line[1] == '//':
            print(" ")
        elif line != '\n':
            line = line.replace('\n','')
            l.append(line)
    elif line != '\n':
        l.append(line)

runs = int(l[0])


'''
if len(sys.argv) > 1:
	runs = int(sys.argv[1])
else:
	runs = 1
'''



try:
    for i in range(runs):

        message = l[i]

        # Send data
        #message = 'Hello TCP Server {}'.format(i + 1)
        print(' Sending: "%s"' % message)
        sock.sendall(str.encode(message))

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(buffer_size)
            amount_received += len(data)
            print('Received: "%s"' % data)

finally:
    print('closing socket')
    sock.close()

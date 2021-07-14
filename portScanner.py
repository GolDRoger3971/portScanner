#!/usr/bin/python

import socket

ip = raw_input("Enter the ip:")

port = input("Enter the port no:")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

if s.connect_ex((ip,port)):
        print "Port",port,"is closed"
else:
        print "Port",port,"is open"

connect=s.connect(('192.168.233.129',23))

banner=s.recv(1024)
s.send('VRFY'+sys.argv[1]+'\r\n')
results=s.recv(1024)
print result
s.close()                   

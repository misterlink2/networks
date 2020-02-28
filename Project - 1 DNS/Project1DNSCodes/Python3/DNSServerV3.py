# Spring 2020 CSci4211: Introduction to Computer Networks
# This program serves as the server of DNS query.
# Written in Python v3.

import sys, threading, os, random
from socket import *
import csv

def main():
	host = "localhost" # Hostname. It can be changed to anything you desire.
	port = 9889 # Port number.

	#create a socket object, SOCK_STREAM for TCP
	serversocket = socket(AF_INET, SOCK_STREAM)
	print("socket created")

	#bind socket to the current address on port 5001
	serversocket.bind((host, port))

	print("socket bound")

	#Listen on the given socket maximum number of connections queued is 20
	serversocket.listen(20)

	print("socket listening")

	monitor = threading.Thread(target=monitorQuit, args=[])
	monitor.start()

	print("Server is listening...")

	while 1:
		#blocked until a remote machine connects to the local port 5001
		connectionSock, addr = serversocket.accept()
		server = threading.Thread(target=dnsQuery, args=[connectionSock, addr[0]])
		server.start()

def dnsQuery(connectionSock, srcAddress):

	file =  open("DNS_mapping.csv","a+")
	file.close()
	log = open("dns-server-log.csv","a+")
	log.close()

	data1 = connectionSock.recv(1024)
	data = data1.decode() # Receive from client ver.#py3 specific
	print("Received:", data) # Print out the result.
	ipaddress =""
	newstr = ""

	with open("DNS_mapping.csv","r+") as file:
		if data in file.read():
			print("srcAddress in file")
			new = dnsSelection(data)
			newstr = listToString(new)

		else:
			print("srcAddress not in file")
			try:
				ipaddress = gethostbyname(data)
			except Exception as e:
				ipaddress = "Could not resolve hostname"
			print("gethostbyname: ", ipaddress)
			log = open("dns-server-log.csv","a+")
			log.write(data)
			log.write(",")
			log.write(ipaddress)
			log.write("\n")
			log.close()
			file.write(data)
			file.write(",")
			file.write(ipaddress)
			file.write("\n")
			newstr = data +  ": " + ipaddress


	newerstr = "Source:" + newstr
	newerstr = newerstr.encode()

	#data = connectionSock.recv(1024)
	#serversocket.send("response	")
	print("while data: ")
	connectionSock.sendall(newerstr)
	#data = connectionSock.recv(1024)
	#Close the server socket.
	#serversocket.shutdown(SHUT_WR)
	connectionSock.close()

def dnsSelection(ipList):
	ip = ""
	with open("DNS_mapping.csv","rt") as f:
		reader = csv.reader(f, delimiter=',') # good point by @paco
		for row in reader:
			for field in row:
				if field == ipList:
					ip = row
					return row
				print("cell: ", field)
				print("row: ", row)
	print("out of loop ")
	return ip

def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    str1 = s[0] + ": " + s[1]

    # return string
    return str1

def monitorQuit():
	while 1:
		sentence = input()
		if sentence == "exit":
			os.kill(os.getpid(),9)

main()

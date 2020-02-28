# Spring 2020 CSci4211: Introduction to Computer Networks
# This program serves as the server of DNS query.
# Written in Python v3.
#written by Austin Basala 5035593 basal006
#on 2/28/20

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
		#blocked until a remote machine connects to the local port 9889
		connectionSock, addr = serversocket.accept()
		server = threading.Thread(target=dnsQuery, args=[connectionSock, addr[0]])
		server.start()

def dnsQuery(connectionSock, srcAddress):
	#open the log file and local cache
	#i thought it was easier to use a csv file for the cache,
	#so the output log and cache are identical.

	#here we open the file in case it does not exist.
	file =  open("DNS_mapping.csv","a+")
	file.close()


	#Receive the input from the client and convert it to socket byte message
	data1 = connectionSock.recv(1024)
	data = data1.decode()
	ipaddress =""
	newstr = ""


	with open("DNS_mapping.csv","r+") as file, open("dns-server-log.csv","a+") as log:
		if data in file.read():
			print("hostname in cache")
			new = dnsSelection(data)
			newstr = listToString(new)
			newerstr = "Cache:" + newstr

			#open the cache and if the request exists return it

		else:
			#if the request does not exist then try to resolve it
			print("hostname not in cache")
			try:
				ipaddress = gethostbyname(data)
			except Exception as e:
				ipaddress = "Could not resolve hostname"
			print("gethostbyname: ", ipaddress)
			log.write(data)
			log.write(",")
			log.write(ipaddress)
			log.write("\n")
			file.write(data)
			file.write(",")
			file.write(ipaddress)
			file.write("\n")
			newstr = data +  ": " + ipaddress
			newerstr = "Local DNS:" + newstr

			#write the resolved host to the logfile and cache

	#put the formatted response into byte messgae
	newerstr = newerstr.encode()
	#and return response to client
	connectionSock.sendall(newerstr)
	connectionSock.close()

def dnsSelection(ipList):
	#search the cache for the hostname
	#return the row where it exists
	#hostname : IP format
	ip = ""
	with open("DNS_mapping.csv","rt") as f:
		reader = csv.reader(f, delimiter=',') # good point by @paco
		for row in reader:
			for field in row:
				if field == ipList:
					ip = row
					return row

	return ip

def listToString(s):
	#converts csv list to formatted string
    str1 = ""
    str1 = s[0] + ": " + s[1]
    return str1

def monitorQuit():
	while 1:
		sentence = input()
		if sentence == "exit":
			os.kill(os.getpid(),9)

main()

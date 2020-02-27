# Spring 2020 CSci4211: Introduction to Computer Networks
# This program serves as the server of DNS query.
# Written in Python v3.

import sys, threading, os, random
from socket import *
import re

def main():
	host = "localhost" # Hostname. It can be changed to anything you desire.
	port = 5001 # Port number.

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
	#check the DNS_mapping.txt to see if the host name exists
	#set local file cache to predetermined file.
    #create file if it doesn't exist
			# file.close()
		#if it does exist, read the file line by line to look for a
		#match with the query sent from the client
		#If match, use the entry in cache.
	    #However, we may get multiple IP addresses in cache, so call dnsSelection to select one.
	file =  open("DNS_mapping.txt","a+")
	file.close()


	ipadress =""
	with open("DNS_mapping.txt","r") as file:
		if srcAddress in file.read():
			hostname = srcAddress
			ipaddress = dnsSelection(srcAddress)

		else:
			#If no lines match, query the local machine DNS lookup to get the IP resolution
			ipaddress = gethostbyname(srcAddress)
			print("ipaddress: ", ipaddress)
			with open("DNS_mapping.txt","a+") as file:
				#write the resposnse in DNS_mapping.txt
				file.write("\n")
				file.write(ipaddress)
				# file.close()

	#print response to the terminal
	print("hostname is: ", ipaddress)

	#send the response back to the client
	data = connectionSock.recv(1024)
	connectionSock.sendall(data)
	#Close the server socket.
	#serversocket.shutdown(SHUT_WR)
	connectionSock.close()

def dnsSelection(ipList):
	next = 0
	ip = "3"
	# with open("DNS_mapping.txt","a+") as file:
	# 	for line in file:
	# 		if ipList in file:
	# 			return "2"
	# 		else:
	# 			return "1"
	return ip
	#checking the number of IP addresses in the cache
	#if there is only one IP address, return the IP address
	#if there are multiple IP addresses, select one and return.
	##bonus project: return the IP address according to the Ping value for better performance (lower latency)

def monitorQuit():
	while 1:
		sentence = input()
		if sentence == "exit":
			os.kill(os.getpid(),9)

main()

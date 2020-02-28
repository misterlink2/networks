Simple client-server DNS host resolver.

written in python3 using sockets. the server opens a socket on a port, binds to it,
and listens for messages on it. the client sends a request with a hostname, and the server receives it.
If the hostname exists in the cache, the server finds the corresponding stored IP of the host.
If the hostname is not in the cache, the server calls a DNS API to try and resolve the hostname.
The resulting hostname , Ip pair is sent back to the client, and also written to the cache and log.

to run, set up a terminal window and run the DNSServerV3.py file with the command "python3 DNSServerV3.py"
open another terminal window and run the  DNSClientV3.py file with the command "python3 DNSClientV3.py"
type a hostname into the client and press enter to send the name to the server.
the response will the resolved IP address, if the server could find it.

Written by Austin Basala 5035593 basal006

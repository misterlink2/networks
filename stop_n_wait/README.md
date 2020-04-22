# CSCI4211_rdt_python
# austin basala 5035593 basal006
# 4211 p2

How to run:
1. install Python 3
2. go to the root folder
3. run `python3 main.py`
main.py will run, showing the exchange of 19 messages. go into pj2/simulation.py and change some variables to increase or decrease the number of messages to send(nsimmax), or to increase the chance of losing a packe(lossprob) as it is sent from A to B or to increase the chance of a message being corrupt as it sent from A to B or B to A (corrupt)

if nsimmax is 21, you can expect messages 'a'-'s' to be received in order. sometimes the final 1 or two messages are not delivered,as they are still in the buffer when the nsimmax is reached in the sim. if the sim is run a couple times,  'a'-'s' will appear.

in stop and wait, the goal of the protocol is to send messages one after another. the sim did not really allow for this to flow smoothly

A output
 i wanted to send a  message to B , and start a timer to send it again incase it wasnt delivered.

B input
 if the packet was corrupted I basically sent a NACK back to A input letting it know it had to resend the pkt, if the pkt.seqnum was the expected value, I sent an ACK back to A, and incremented the expected value.

A input
 if the nack or ack returned I updated the A.state from WAIT_ACK to WAIT_LAYER5, removed any timers, and updated the expected seq, if the value from B indicated a corrupt message, i left the state as is. 


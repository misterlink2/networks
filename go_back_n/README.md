# CSCI4211_rdt_python
# austin basala 5035593 basal006
# 4211 p2 go back n

How to run:
1. install Python 3
2. go to the root folder
3. run `python3 main.py`
main.py will run, showing the exchange of 19 messages. go into pj2/simulation.py and change some variables to increase or decrease the number of messages to send(nsimmax), or to increase the chance of losing a packe(lossprob) as it is sent from A to B or to increase the chance of a message being corrupt as it sent from A to B or B to A (corrupt)

if nsimmax is 21, you can expect messages 'a'-'s' to be received in order. sometimes the final 1 or two messages are not delivered,as they are still in the buffer when the nsimmax is reached in the sim. if the sim is run a couple times,  'a'-'s' will appear.

in go back n, the goal of the protocol is to send messages one after another in a window of size n, after a message in the window has been confirmed to be delivered, the window moves to the next bits

A output
  i wanted to send a  message to B , if the buffer is not full, the pkt is added to the buffer and sent to B, if the buffer is full the buffer is cleared, the pkt is pushed on to it, and pkt is sent to B, and start a timer to send it again incase it wasnt delivered.

B input
 if the packet was corrupted I basically sent a NACK back to A input letting it know it had to resend the pkt, if the pkt.seqnum was the expected value, I sent an ACK back to A, and incremented the expected value,  if the pkt seq was less than the B.seq , I sent a NACK back to A .

A input
 if the nack or ack returned I updated the A.state from WAIT_ACK to WAIT_LAYER5, removed any timers, and updated the expected seq, if the value from B indicated the pkt was corrupt or wrong, the buffer re-sent to B, unless the seq was lower than expected, then the head of the queue was removed

clean_buf()
clears out the buffer of all packets

buf_read()
reads the data and seqnum of every pkt in the buffer

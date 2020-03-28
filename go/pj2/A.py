from pj2.simulator import sim
from pj2.simulator import to_layer_three
from pj2.event_list import evl
from pj2.packet import *
from pj2.circular_buffer import circular_buffer

class A:
    def __init__(self):
        self.seq = 0
        self.buf = circular_buffer(8)
        self.estimated_rtt = 30
        self.received = 0
        # go back n, the initialization of A
        # Initialize the initial sequence number to 0.
        # You need to initialize the circular buffer, using "circular_buffer(max)". max is the number of the packets that the buffer can hold
        # You can set the estimated_rtt to be 30, which is used as a parameter when you call start_timer
    
    def A_output(self, m):
        #print("-----------------")
        #print("A OUTPUT")
        pkt = packet(seqnum = self.seq,payload = m)
        #print("pkt created: ", pkt.payload.data[0],pkt.seqnum)
        if(self.buf.isfull()==False):
            self.buf.push(pkt)
            to_layer_three("A",pkt)
            self.seq+=1
            #print("sending packet")
        else:
            #print("buffer full")
            #print("seq:",self.seq)
            #print("received: ",self.received)
            #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            self.clean_buf()
            #for i in self.buf.read_all():
                #self.buf.pop()
            self.buf.push(pkt)
                #to_layer_three("A",i)

        #to_layer_three("A",pkt)
        evl.start_timer("A",self.estimated_rtt)
        #self.buf_read()

        # go back n, A_output
        # If the buffer is full, just drop the packet
        # Construct the packet based on the message. Make sure that the sequence number is correct
        # Send the packet and save it to the circular buffer using "push()" of circular_buffer
        # Set the timer using "evl.start_timer(entity, time)", and the time should be set to estimated_rtt. Make sure that there is only one timer started in the event list

    def A_input(self, pkt):
        #print("A INPUT")
        #print("received ack:",pkt.acknum)
        #print("self.received:",self.received)
        #if(pkt.acknum ==  -1):
            #self.seq+=1
            #print("NACK received, self.seq+1 =",self.seq)

        if (pkt.acknum == self.received):
            #self.buf_read()
            #print("buf.pop")
            self.buf.pop()
            #self.buf_read()
            self.received+=1
            #print("A.received :",self.received)
            self.clean_buf()
            try:
                #print("removing timer")
                evl.remove_timer()
            except AttributeError:
                pass
               #print("caught error")
        elif (pkt.acknum == -20):
            #self.buf_read()
            #print("buf.pop")
            self.buf.pop()
        else:
            #print("wrong ack, resending buffer")
            #self.buf_read()
            for i in self.buf.read_all():
                to_layer_three("A",i)
            return

        # go back n, A_input
        # Verify that the packet is not corrupted
        # Update the circular buffer according to the acknowledgement number using "pop()"


    def A_handle_timer(self):
        #print("-----------------")
        #print("TIMER")
        #print("resending buffer:")
        #self.buf_read()
        for i in self.buf.read_all():
            to_layer_three("A",i)

    def clean_buf(self):
        #print("BUFFER:")
        #print("????????")
        for i in self.buf.read_all():
            if i.seqnum < self.received:
                self.buf.pop()
        #print("????????")

    def buf_read(self):
        print("BUFFER:")
        print("$$$$$$")
        for i in self.buf.read_all():
            print(i.payload.data[0],i.seqnum)
        print("$$$$$$")
        #self.buf.read_all()
        # go back n, A_handle_timer
        # Read all the sent packet that it is not acknowledged using "read_all()" of the circular buffer and resend them
        # If you need to resend packets, set a timer after that


a = A()

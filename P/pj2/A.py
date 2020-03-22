from pj2.simulator import sim
from pj2.simulator import to_layer_three
from pj2.event_list import evl
from pj2.packet import *
from pj2.circular_buffer import circular_buffer

class A:
    def __init__(self):
        # TODO: initialization of the state of A
        # self.estimated_rtt
        # ...
        self.seq=0
        self.state = "WAIT_LAYER5"
        return

    def A_input(self, pkt):
        # TODO: recive data from the other side
        # process the ACK, NACK from B
        if(pkt.acknum==(self.seq+1)):
            self.seq+=1
            self.state = "WAIT_LAYER5" 
            #print("a input correct ack")
            #sim.ntolayer3 += 1
        #else: 
            #print("a input wrong ack")
        return

    def A_output(self, m):
        # TODO: called from layer 5, pass the data to the other side
        #print("a output seq: ",self.seq)
        pkt = packet(seqnum=self.seq, payload=m)
        to_layer_three("A", pkt)
        self.state ="WAIT_ACK"

    def A_handle_timer(self):
        # TODO: handler for time interrupt
        # resend the packet as needed
        return


a = A()

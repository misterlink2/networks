from pj2.simulator import sim
from pj2.simulator import to_layer_three
from pj2.event_list import evl
from pj2.packet import *
from pj2.circular_buffer import circular_buffer
from pj2.msg import *

class A:
    def __init__(self):
        # TODO: initialization of the state of A
        # self.estimated_rtt
        self.state = "WAIT_ACK"
        self.seq=0
        m = msg('a')
        self.pkt = packet(seqnum=0,payload = m)
        return

    def A_input(self, pkt):
        # TODO: recive data from the other side
        # process the ACK, NACK from B
        if (pkt.acknum == (self.seq+1)):
            self.seq+=1
            self.state = "WAIT_LAYER5"
        #elif (pkt.acknum == -1):
            #self.seq+=1

        else:
            print("B->A pkt.ack",pkt.acknum,"A.seq",self.seq)
        return

    def A_output(self, m):
        # TODO: called from layer 5, pass the data to the other side
        if (self.state == "WAIT_LAYER5"):
            pkt = packet(seqnum=self.seq, payload=m)
            self.pkt = pkt
        else:
            print("waiting on ack")
        evl.start_timer("A",30)
        self.state = "WAIT_ACK"
        to_layer_three("A", self.pkt)

    def A_handle_timer(self):
        print("resending pkt ",self.pkt.payload.data[0])
        to_layer_three("A",self.pkt)
        # TODO: handler for time interrupt
        # resend the packet as needed
        return


a = A()

from pj2.simulator import sim
from pj2.simulator import to_layer_three
from pj2.event_list import evl
from pj2.packet import *
from pj2.circular_buffer import circular_buffer
from pj2.msg import *

class A:
    def __init__(self):
        self.estimated_rtt = 200
        self.state = "WAIT_LAYER5"
        self.seq=0
        m = msg('a')
        self.pkt = packet(seqnum=0,payload = m)
        return

    def A_input(self, pkt):
        if(pkt.acknum == -20):
            pass

        if (pkt.acknum == (self.seq+1) or pkt.acknum == -1):
            self.seq+=1
            self.state = "WAIT_LAYER5"
            try:
                evl.remove_timer()
            except AttributeError:
                pass

        return

    def A_output(self, m):
        if (sim.nsim >(self.seq+1)):
            sim.nsim -=1
        if (self.state == "WAIT_LAYER5"):
            pkt = packet(seqnum=self.seq, payload=m)
            self.pkt = pkt
        evl.start_timer("A",self.estimated_rtt)
        self.state = "WAIT_ACK"
        to_layer_three("A", self.pkt)

    def A_handle_timer(self):
        to_layer_three("A",self.pkt)
        return


a = A()

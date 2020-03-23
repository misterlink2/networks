from pj2.simulator import sim
from pj2.simulator import to_layer_three
from pj2.event_list import evl
from pj2.packet import *
from pj2.circular_buffer import circular_buffer
from pj2.B import b

class A:
    def __init__(self):
        # TODO: initialization of the state of A
        self.estimated_rtt = 5
        self.seq=0 
        self.pkt= packet(seqnum=self.seq)
        self.state = "WAIT_LAYER5"
        return

    def A_input(self, pkt):
        # TODO: recive data from the other side
        # process the ACK, NACK from B
        if(pkt.acknum==(self.seq+1)):
            self.seq+=1
            self.state = "WAIT_LAYER5" 
            print("a input correct ack")
            #sim.ntolayer3 += 1
        elif(pkt.acknum==-1):
            print("NACK")
        else:
            print("a input wrong ack")
        return

    def A_output(self, m):
        # TODO: called from layer 5, pass the data to the other side
        print("a output seq: ",self.seq)
        pkt = packet(seqnum=self.seq, payload=m)
        self.pkt = pkt
        to_layer_three("A", pkt)
        evl.start_timer("A",self.estimated_rtt)
        self.state ="WAIT_ACK"

    def A_handle_timer(self):
        print("resending pkt: ", self.pkt.payload.data[0]) 
         
        #print("timer seq: ",self.seq)
        #to_layer_three("A", self.pkt)
        # b.seq=self.seq
        #evl.remove_timer()
        # TODO: handler for time interrupt
        # resend the packet as needed
        return


a = A()

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
    
    def A_output(self, m):
        pkt = packet(seqnum = self.seq,payload = m)
        if(self.buf.isfull()==False):
            self.buf.push(pkt)
            to_layer_three("A",pkt)
            self.seq+=1
        else:
            self.clean_buf()
            self.buf.push(pkt)
        evl.start_timer("A",self.estimated_rtt)

    def A_input(self, pkt):

        if (pkt.acknum == self.received):
            self.buf.pop()
            self.received+=1
            self.clean_buf()
            try:
                evl.remove_timer()
            except AttributeError:
                pass
        elif (pkt.acknum == -20):
            self.buf.pop()
        else:
            for i in self.buf.read_all():
                to_layer_three("A",i)
            return


    def A_handle_timer(self):
        for i in self.buf.read_all():
            to_layer_three("A",i)

    def clean_buf(self):
        for i in self.buf.read_all():
            if i.seqnum < self.received:
                self.buf.pop()

    def buf_read(self):
        print("BUFFER:")
        print("$$$$$$")
        for i in self.buf.read_all():
            print(i.payload.data[0],i.seqnum)
        print("$$$$$$")

a = A()

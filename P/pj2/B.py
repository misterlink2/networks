from pj2.simulator import to_layer_five
from pj2.packet import send_ack
from pj2.simulator import sim

class B:
    def __init__(self):
        # TODO: initialization of the state of B
        self.seq= 0
        # ...
        return

    def B_input(self, pkt):
        # TODO: process the packet recieved from the layer 3
        # verify checksum
        # send ACK
        #if (pkt.payload.data[-1]!='*'):#check corruption
        if (pkt.seqnum == self.seq):   
            to_layer_five("B", pkt.payload.data)
            send_ack("B",(pkt.seqnum+1))
            self.seq+=1
        elif (pkt.seqnum<self.seq):
            #send_NACK
            self.seq-=1
            send_ack("B",-1)
        else:
            print("wrong seq no")
            print("Pkt.seq: ", pkt.seqnum, "self.seq", self.seq)
        
        return

    def B_output(self, m):
        return

    def B_handle_timer(self):
        return


b = B()

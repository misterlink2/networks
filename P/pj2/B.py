from pj2.simulator import to_layer_five
from pj2.packet import send_ack
from pj2.simulator import sim

class B:
    def __init__(self):
        # TODO: initialization of the state of B
        # self.seq
        # ...
        return

    def B_input(self, pkt):
        # TODO: process the packet recieved from the layer 3
        # verify checksum
        # send ACK
        if (pkt.payload.data[-1]!='*'):
            to_layer_five("B", pkt.payload.data)
            send_ack("B",(pkt.seqnum+1))
        #else:
            #print("Corrupted")
            #print("Pkt.seq: ", pkt.seqnum, "sim.nsim", sim.nsim)
        
        return

    def B_output(self, m):
        return

    def B_handle_timer(self):
        return


b = B()

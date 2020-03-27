from pj2.simulator import to_layer_five, sim
from pj2.packet import send_ack
from pj2.event_list import evl

class B:
    def __init__(self):
        # TODO: initialization of the state of B
        self.seq = 0
        # ...
        return

    def B_input(self, pkt):
        # TODO: process the packet recieved from the layer 3
        # verify checksum
        # send ACK
        print("B INPUT")
        #print("pkt.seq",pkt.seqnum,"B.seq",self.seq)
        #print("checksum:", pkt.get_checksum())
        #if (pkt.get_checksum() !=sim.ncorrupt):
            #print("CORRUPT")
            #print("pkt.checksum: ",pkt.get_checksum(),"A checksum: ",sim.ncorrupt)
            #dif = pkt.get_checksum()-sim.ncorrupt
            #print("difference: ", dif)

        if (pkt.payload.data[-1]=='*'):
            print("corrupt, sending NACK*")
            send_ack("B",-20)

        elif (pkt.seqnum == self.seq):
            self.seq +=1
            send_ack("B",self.seq)
            to_layer_five("B", pkt.payload.data);
            #evl.remove_timer()
            #evl.start_timer("B",30)
        else:
            print("Send NACK")
            send_ack("B",-1)
        return

    def B_output(self, m):
        return

    def B_handle_timer(self):
        print("B TIMER")
        return


b = B()

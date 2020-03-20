from pj2.simulator import to_layer_five
from pj2.packet import send_ack

class B:
    def __init__(self):
        # TODO: initialization of the state of B
        # self.seq
        # ...
        return

    def B_input(self, pkt):
        chek = pkt.get_checksum()
        print("")
        print("")
        print("---------------------")
        print("B")
        print("seqnum:", pkt.seqnum)
        print("acknum:", pkt.acknum)
        #print("payload:", pkt.payload)
        print("checksum: ", pkt.checksum)
        print("checksum: ", pkt.get_checksum())
        print("---------------------")
        print("")
        print("")
        #if (chek = 0):#verify checksum is what??
            #to_layer_five("B", pkt.payload.data)
            #update seqno??
        #send_ack("B",pkt.seqno)
       
       # TODO: process the packet recieved from the layer 3
        # verify checksum
        # send ACK
        to_layer_five("B", pkt.payload.data);
        return

    def B_output(self, m):
        return

    def B_handle_timer(self):
        return


b = B()

from pj2.simulator import to_layer_five
from pj2.packet import send_ack
from pj2.simulator import sim
from pj2.event_list import evl

class B:
    def __init__(self):
        # TODO: initialization of the state of B
        self.seq = 0 
        # ...
        return

    def B_input(self, pkt):
        chek = pkt.get_checksum()
        #print("")
        #print("")
        #print("---------------------")
        #print("B")
        #print("seqnum:", pkt.seqnum)
        #print("acknum:", pkt.acknum)
        #print("checksum: ", pkt.checksum)
        #print("checksum: ", pkt.get_checksum())
        #print("---------------------")
        #print("")
        #print("")
        #if (chek = 0):#verify checksum is what??
            #to_layer_five("B", pkt.payload.data)
            #update seqno?
        
        print("--------b input-------------")
        
        #print("B evl before")
        #evl.print_self()
        if (pkt.payload.data[-1]=='*'):
            print("B corrupted")
            print(pkt.payload.data)
        else:

            print("B not corrupted")
            if(pkt.seqnum == self.seq):
                print("B pkt.seq: ",pkt.seqnum,"B self.seq:  ", self.seq)
                to_layer_five("B", pkt.payload.data);
                self.seq +=1 
                print("ACK SENT") 
                print("B self.seq+1")
                send_ack("B",self.seq)
            else:
                sim.nsim-=1
                print("nsim: ", sim.nsim)
                print("B pkt.seq: ",pkt.seqnum, "self.seq: ", self.seq)
                print(pkt.payload.data[0])
            #print("B evl after")
            #evl.print_self()
        
        # TODO: process the packet recieved from the layer 3
        # verify checksum
        # send ACK
        #to_layer_five("B", pkt.payload.data);
        return

    def B_output(self, m):
        return

    def B_handle_timer(self):
        return


b = B()

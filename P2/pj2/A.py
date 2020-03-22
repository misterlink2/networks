from pj2.simulator import sim
from pj2.simulator import to_layer_three
from pj2.event_list import evl
from pj2.packet import *
from pj2.circular_buffer import circular_buffer

class A:
    def __init__(self):
        # TODO: initialization of the state of A
        self.estimated_rtt = 30
        self.seq=0
        self.state="WAIT_LAYER5"
        return

    def A_input(self, pkt):
        sum = pkt.get_checksum()
        #print("A input") 
        #print("")
        #print("")
        print("---------a input----------")
        #print("A INPUT")
        print("a pkt.seqnum:", pkt.seqnum)
        print("acknum:", pkt.acknum)
        print("self seq: ", self.seq) 
        #print("checksum: ", pkt.get_checksum())
        
        #if(pkt.payload!=0):
            #print("PACKET: ", pkt.payload.data[0])
            #if (pkt.payload.data[-1]=='*'):
                #print("CORRUPT")
                #to_layer_three("A",pkt)#we might not wanna do this
            #else:   
        
        #print("A input evl before")
        #evl.print_self()
        if(pkt.acknum == (self.seq+1)):# i think we want if pkt.acknum == self.seq
            print("ACKNUM MATCHES")
            self.state = "WAIT_LAYER5"#as we increment seq + 1, and ack should be seq + 1
            print("A self.seq+1")
            self.seq+=1
        else:
            print("WRONG ACK")#try resending correct packet? not the same wrong one
            to_layer_three("A",pkt)
        
        #print("A input evl after")
        #evl.print_self()
        #else:
            #print("pkt payload == 0")

        #print("-------a input------------")
        #print("")
        #print("") 
        
        # TODO: recive data from the other side
        # process the ACK, NACK from B
        return

    def A_output(self, m):
        # TODO: called from layer 5, pass the data to the other side
        
        print("--------A output----------")
        print("A output") 
        print("A seqnum:", self.seq)
        #print("A output evl before")
        #evl.print_self()
        pkt = packet(seqnum=self.seq, payload=m)
        to_layer_three("A", pkt)
        evl.start_timer("A",self.estimated_rtt) 
        #print("A output evl after")
        #evl.print_self()
        #print("")
        #print("")
        #print("-------------------")
        #print("A")
        #print("seqnum:", pkt.seqnum)
        #print("acknum:", pkt.acknum)
        #print("self seq: ", self.seq) 
        #print("checksum: ", pkt.get_checksum())
        #print("-------------------")
        #print("")
        #print("") 

        # evl.remove_timer()
        self.state="WAIT_ACK"
    
    def A_handle_timer(self):
        #if the most recent acknum != self.seq, ie: A is not receiving b's correct ACK,
        #then we change B's expected seq (and maybe A.seq)
        # so that we can continue to send msgs
        from pj2.A import a
        from pj2.B import b
        b.seq=a.seq
        #sim.nsim-=1
        print("B SEQ CHANGED TO A SEQ B.seq: ", b.seq," A.seq: ", a.seq)
        #evl.remove_timer()
        #to_layer_three("A", pkt) how do I grab packet
        #evl.start_timer("A",self.estimated_rtt)
        
        # TODO: handler for time interrupt
        # resend the packet as needed
        return


a = A()

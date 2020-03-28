from pj2.simulator import to_layer_five, sim
from pj2.packet import send_ack
from pj2.event_list import evl

class B:
    def __init__(self):
        self.seq = 0
        return

    def B_input(self, pkt):

        if (pkt.payload.data[-1]=='*'):
            send_ack("B",-1)
        elif (pkt.seqnum < self.seq):
            send_ack("B",-20)

        elif (pkt.seqnum == self.seq):
            send_ack("B",pkt.seqnum)
            self.seq +=1
            to_layer_five("B", pkt.payload.data);
        else:
            send_ack("B",-1)
        return

    def B_output(self, m):
        return

    def B_handle_timer(self):
        return


b = B()

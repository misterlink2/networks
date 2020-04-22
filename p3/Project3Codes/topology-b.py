#!/usr/bin/env python

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.node import RemoteController

class AssignmentNetworks(Topo):
    def __init__(self, **opts):
        Topo.__init__(self, **opts)
        
	# switch performance parameters based on level
	lvl1_bw = 100
        lvl2_bw = 40
        lvl3_bw = 10

        lvl1_delay = '30ms'
        lvl2_delay = '20ms'
        lvl3_delay = '10ms'

        #Start to build the topology here

       
 
        
if __name__ == '__main__':
    setLogLevel( 'info' )

    topo = AssignmentNetworks()
    net = Mininet(topo=topo, link=TCLink, autoSetMacs=True,autoStaticArp=True)
    #net = Mininet(controller=RemoteController, topo=topo, link=TCLink, autoSetMacs=True,autoStaticArp=True)

    # Run network
    net.start()
    CLI( net )
    net.stop()


from pox.core import core
import pox.openflow.libopenflow_01 as of


log = core.getLogger()

# the table maps the switchID, which we construct, and a packet source
table = {}



# Handle messages the switch has sent us because it has no
# matching rule.
def _handle_PacketIn (event):

  # get the port the packet came in on for the switch contacting the controller
  packetInPort = event.port

  # use POX to parse the packet
  packet = event.parsed

  # get src and dst mac addresses
  src_mac = str(packet.src)
  dst_mac = str(packet.dst)

  # get switch ID
  switchID = str(event.connection.dpid) + str(event.connection.ID)
  
  log.info('Packet has arrived: SRCMAC:{} DSTMAC:{} from switch:{} in-port:{}'.format(src_mac, dst_mac, switchID, packetInPort))

  # Learn the source
  table[(switchID,packet.src)] = packetInPort

  log.debug("table: ", table)
  destination = table.get((switchID,packet.dst))

  if destination is None:
    #the destination is not in the table yet so we flood the rest of the 
    # switches in order to find it with of.OFPP_ALL
    msg = of.ofp_packet_out(data = event.ofp)
    msg.actions.append(of.ofp_action_output(port = of.OFPP_ALL))
    event.connection.send(msg)
  else:
    #we put rules in the table for source and destination as they can be used both ways
    msg = of.ofp_flow_mod()
    msg.match.dl_dst = packet.src
    msg.match.dl_src = packet.dst
    msg.actions.append(of.ofp_action_output(port = packetInPort))
    event.connection.send(msg)
    #now we add the destination
    msg = of.ofp_flow_mod()
    msg.data = event.ofp # Forward the incoming packet
    msg.match.dl_src = packet.src
    msg.match.dl_dst = packet.dst
    msg.actions.append(of.ofp_action_output(port = destination))
    event.connection.send(msg)

    log.debug("mapping src: %s, to dst: %s" % (packet.src, packet.dst))


def launch ():

  core.openflow.addListenerByName("PacketIn", _handle_PacketIn)

  log.info("Pair-Learning switch running.")

from scapy.all import *
import sys
from consts import _sport, host, port

_seq = int(sys.argv[1])
_ack = int(sys.argv[2])

print _seq

ACK = IP(dst=host)/TCP(sport=_sport, dport=port, flags="FA", ack=_ack, seq=_seq)
send(ACK)


from scapy.all import *
import sys
from consts import _sport, host, port, d

_seq = int(sys.argv[1])
_ack = int(sys.argv[2])

print _seq

SENDDATA = IP(dst=host)/TCP(sport=_sport, dport=port, flags="PA", ack=_ack, seq=_seq)
R = send(SENDDATA/d)


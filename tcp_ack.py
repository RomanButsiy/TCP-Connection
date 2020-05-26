from scapy.all import *
import sys
from consts import _sport, host, port
from helpers import *

_seq = int(sys.argv[1])
_ack = int(sys.argv[2])

print _seq

ACK = IP(dst=host)/TCP(sport=_sport, dport=port, flags="A", ack=_ack, seq=_seq)
send(ACK)



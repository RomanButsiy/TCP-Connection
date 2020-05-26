from scapy.all import *
import sys, os
from consts import _sport, host, port
from helpers import *

_seq = int(sys.argv[1])
SYN = IP(dst=host)/TCP(sport=_sport, dport=port, flags="S", seq=_seq)
ACK = sr1(SYN)

saveSEQ(ACK.seq)


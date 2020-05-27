from scapy.all import *

sniff(filter="host 85.143.216.55", prn=lambda x: x.sprintf("%IP.src% %TCP.sport% seq=%TCP.seq% ack=%TCP.ack% %TCP.flags% %Raw.load%"))


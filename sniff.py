from scapy.all import *

sniff(filter="host 91.198.10.2", prn=lambda x: x.sprintf("%IP.src% %TCP.sport% seq=%TCP.seq% ack=%TCP.ack% %TCP.flags% %Raw.load%"))


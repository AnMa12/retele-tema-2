from scapy.all import *
import sys

dst = '198.13.0.14'
dport = int(sys.argv[1])

seq = 12345

# 3 way handshake
ip = IP(dst=dst)
synack = sr1(IP(dst=dst)/TCP(dport=dport, flags='S', seq=seq))
send(IP(dst=dst)/TCP(dport=dport, flags='A', seq=synack.ack, ack=synack.seq+1), count=1)

seq = synack.ack
ack = synack.seq + 1
ip = IP(dst=dst, tos=int('011110' + '11', 2))
for i in range(3):
    send(ip/TCP(dport=dport, flags='PAEC', seq=seq, ack=ack)/'H')
    seq = seq + 1
    ans, unans = sniff(filter='tcp and host ' + dst, count=2)
    pkt = ans[0]
    ack = pkt.seq + len(pkt[Raw])
data = sr1(ip/TCP(dport=dport, flags='PAEC', seq=seq, ack=ack)/'asd')
seq += 3

send(ip/TCP(dport=dport, flags='R', seq=seq, ack=ack))

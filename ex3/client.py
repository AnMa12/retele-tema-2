from scapy.all import *

dst = '198.13.0.14'
dport = 10000

# 3 way handshake
ip = IP(dst=dst)
syn = TCP(dport=dport, flags='S', seq=1234)
synack = sr1(ip/syn)
print(synack.show())
ack = ip/TCP(dport=dport, flags='A', seq=synack.ack, ack=synack.seq+1)
print(ack.show())
send(ack)

#ip = IP(dst=dst, tos=int('011110' + '11', 2))
#tcp = TCP(dport=dport, flags='EC')
#
#for i in range(2):
#    ans = sr1(ip/tcp/b'a', timeout=2)
#    print(ans)
#ans = sr1(ip/tcp/b'asd')
#print(ans)
#
# connection close

#ip = IP(dst=dst)
#fin = TCP(dport=dport, flags='F', seq=1234)
#finack = sr(ip/fin, timeout=2)[1]
#print(finack)
#ack = TCP(dport=dport, flags='A', seq=finack.ack, ack=finack.seq+1)
#send(ip/finack)

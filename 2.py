from scapy.all import *

answered, unanswered = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst='198.13.13.0/16'), timeout=1)

for x in answered:
    print(x[1].psrc, ' : ', x[1].hwsrc)


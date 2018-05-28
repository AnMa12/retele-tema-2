from scapy.all import *

ans, unans = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst='198.13.13.0/16'), timeout=1)
for pkt in ans:
    print(pkt[1].psrc, '---', pkt[1].hwsrc)


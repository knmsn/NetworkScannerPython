from scapy.all import ARP, Ether, srp

ipuser = input("=> Digite seu ipv4:")

network_victim = (ipuser+"/24")

arp = ARP(pdst=network_victim)

ether = Ether(dst="ff:ff:ff:ff:ff:ff")

packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

users = []

for sent, received in result:
    users.append({'ip': received.psrc, 'mac': received.hwsrc})

print("IP" + " "*18+"MAC")

for client in users:
    print("{:16}    {}".format(client['ip'], client['mac']))
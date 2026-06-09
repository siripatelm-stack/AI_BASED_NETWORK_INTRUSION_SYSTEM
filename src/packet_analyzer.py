from scapy.all import sniff, IP, TCP, UDP, conf

# Force Scapy to use standard network capture drivers on Windows
conf.use_pcap = True

def analyze_packet(packet):
    # Check if the packet contains network data (IP Layer)
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
        # Monitor TCP Traffic
        if packet.haslayer(TCP):
            port = packet[TCP].dport
            
            # Safely extract and check payload text data for malicious keywords
            try:
                payload = bytes(packet[TCP].payload).decode('utf-8', errors='ignore').lower()
            except Exception:
                payload = ""

            # Trigger condition: Specific port or keyword signature detected
            if port == 4444 or "exploit" in payload or "attack" in payload:
                print("\n" + "!" * 60)
                print(f"[!] ALERT: CRITICAL SECURITY THREAT DETECTED!")
                print(f"[!] MALICIOUS PACKET: {src_ip} -> {dst_ip} ON PORT {port}")
                print("[!] MESSAGE: YOU WILL GET HACKED!")
                print("!" * 60 + "\n")
            else:
                # Displays standard ongoing system traffic
                print(f"[+] TCP Packet: {src_ip} -> {dst_ip}:{port}")
                
        # Monitor UDP Traffic
        elif packet.haslayer(UDP):
            print(f"[+] UDP Packet: {src_ip} -> {dst_ip}:{packet[UDP].dport}")

def start_monitor():
    print("[*] Analyzer active. Sniffing all system traffic moving to and fro...")
    print("[*] Press Ctrl+C to stop scanning.\n")
    
    # sniff() runs indefinitely, catching all raw live traffic
    sniff(prn=analyze_packet, store=False)

if __name__ == "__main__":
    start_monitor()

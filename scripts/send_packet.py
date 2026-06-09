import socket
from scapy.all import Ether, IP, TCP, sendp

def get_current_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def send_trigger_packet():
    TARGET_IP = get_current_ip()
    print(f"[*] Local System IP detected: {TARGET_IP}")
    print(f"[*] Injecting malicious pattern packet to target...")

    # Ether() wraps the packet in a local Layer-2 broadcast frame.
    # This forces Windows to read it on the network interface card.
    packet = Ether(dst="ff:ff:ff:ff:ff:ff")/IP(dst=TARGET_IP)/TCP(dport=4444)/"WARNING: EXPLOIT ATTACK DETECTED"
    
    # sendp() sends raw Layer-2 packets
    sendp(packet, verbose=False)
    print("[+] Malicious pattern sent successfully once.")

if __name__ == "__main__":
    send_trigger_packet()
from scapy.all import send, ARP, Ether
import time

# --- CONFIGURATION ---
# This must match an IP in your 'known_devices' dictionary
TARGET_IP = ""
# This is the "fake" MAC address that will trigger the alert
FAKE_MAC = "aa:bb:cc:dd:ee:ff" 
# ---------------------

def simulate_spoof():
    print(f"[*] Sending fake ARP response: {TARGET_IP} is at {FAKE_MAC}")
    
    # op=2 makes it an ARP Reply (is-at)
    # psrc is the IP we are pretending to be
    # hwsrc is the fake MAC address
    packet = ARP(op=2, psrc=TARGET_IP, hwsrc=FAKE_MAC)
    
    # Send the packet
    send(packet, verbose=False)
    print("[+] Packet sent! Check your Detector terminal and system notifications.")

if __name__ == "__main__":
    simulate_spoof()
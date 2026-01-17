from scapy.all import sniff, ARP
import hashlib
from collections import Counter
import threading
import time

# 1: "ARP Spoofing Detector"
def detect_arp_spoof(pkt):
    if pkt.haslayer(ARP) and pkt[ARP].op == 2: # ARP Is-At (Response)
        try:
            real_mac = "" # Example: Your Router's REAL MAC
            response_mac = pkt[ARP].hwsrc
            if real_mac != response_mac:
                print(f"[!] INCIDENT: ARP Poisoning Detected! IP {pkt[ARP].psrc} is being spoofed by {response_mac}")
        except IndexError:
            pass

# 2: The "Traffic Analyst" (Port Scan Detector)
connection_attempts = Counter()

def detect_port_scan(pkt):
    if pkt.haslayer('TCP') and pkt['TCP'].flags == 'S': # SYN Packet
        src_ip = pkt['IP'].src
        connection_attempts[src_ip] += 1
        if connection_attempts[src_ip] > 50:
            print(f"[!] ALERT: Potential Port Scan from {src_ip} (Threshold Exceeded)")

# 3: "Credential Guardian" (Cleartext Sniffer)
def sniff_credentials(pkt):
    if pkt.haslayer('Raw'):
        payload = str(pkt['Raw'].load).lower()
        keywords = ["user", "pass", "login", "password"]
        if any(word in payload for word in keywords):
            print(f"[!] WARNING: Unencrypted sensitive data detected from {pkt['IP'].src}")

# 4: The "Asset Watchdog" (File Integrity)
def check_file_integrity(filename, original_hash):
    # We add a loop here so it keeps checking in its own thread
    while True:
        sha256_hash = hashlib.sha256()
        try:
            with open(filename, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            
            if sha256_hash.hexdigest() != original_hash:
                print(f"[!] CRITICAL: File {filename} has been TAMPERED with!")
        except FileNotFoundError:
            print(f"[-] Error: {filename} not found.")
        
        time.sleep(5) # Wait 5 seconds before checking again

# Role: Security Orchestrator
def master_monitor(pkt):
    if pkt.haslayer('IP'):
        detect_arp_spoof(pkt)
        detect_port_scan(pkt)
        sniff_credentials(pkt)

def start_incident_response():
    print("[*] Initializing Network Incident Response Suite...")
    
    # SETUP FILE INTEGRITY THREAD
    # Replace with your actual file and hash
    filename = ""
    original_hash = ""
    
    # Create and start the thread for Module 4
    file_thread = threading.Thread(target=check_file_integrity, args=(filename, original_hash))
    file_thread.daemon = True # This ensures the thread dies when the main program stops
    file_thread.start()

    print("[*] Monitoring Assets and Network Layers...")
    # This runs in the main thread
    sniff(filter="ip", prn=master_monitor, store=0)

if __name__ == "__main__":
    start_incident_response()

# "I built each function targets a different stage of the Cyber Kill Chain (Reconnaissance, Exploitation, Actions on Objectives)."

# "By using Python and Scapy, I can automate the 'Sound the Alarm' process from my Google Certificate training, reducing the time to detect an intruder from minutes to milliseconds."

# Real-world Impact: "In a professional environment , this logic could be used to monitor specific critical subnets for unauthorized ARP changes or unencrypted traffic."

from scapy.all import sniff, ARP
import os
import platform

# Use colons for standard Scapy formatting
known_devices = {
    "10.237.252.32": "32:67:2c:f3:b5:7d", 
}

def send_alert(message):
    """Sends a system notification based on the Operating System"""
    print(f"[!] ALERT: {message}")
    current_os = platform.system()

    if current_os == "Linux":
        # Requires libnotify-bin
        os.system(f'notify-send "Security Incident" "{message}"')
    
    elif current_os == "Darwin":  # macOS
        # Uses AppleScript for a system toast
        t = "Security Incident"
        os.system(f"osascript -e 'display notification \"{message}\" with title \"{t}\"'")
    
    elif current_os == "Windows":
        # Simple PowerShell command for a balloon notification
        # Note: You can also use 'pip install win10toast' for a cleaner look
        ps_script = f'Add-Type -AssemblyName System.Windows.Forms; ' \
                    f'$notify = New-Object System.Windows.Forms.NotifyIcon; ' \
                    f'$notify.Icon = [System.Drawing.SystemIcons]::Exclamation; ' \
                    f'$notify.Visible = $true; ' \
                    f'$notify.ShowBalloonTip(5000, "Security Incident", "{message}", [System.Windows.Forms.ToolTipIcon]::Warning)'
        os.system(f'powershell -Command "{ps_script}"')

def process_packet(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:  # op=2 is 'is-at' (response)
        ip = packet[ARP].psrc
        # Normalize MAC to lowercase and use colons for consistency
        mac = packet[ARP].hwsrc.lower().replace("-", ":")
        
        if ip in known_devices:
            real_mac = known_devices[ip].lower().replace("-", ":")
            if real_mac != mac:
                alert_msg = f"ARP Spoofing Detected! IP {ip} is being claimed by MAC {mac}"
                send_alert(alert_msg)

print(f"[*] Monitoring on {platform.system()} for ARP anomalies...")
# Note: On Windows/macOS, you may need to specify an interface: sniff(iface="Wi-Fi", ...)
sniff(filter="arp", prn=process_packet, store=0)
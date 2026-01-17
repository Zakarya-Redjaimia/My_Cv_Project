from scapy.all import *
from scapy.all import sniff
from colorama import Back ,Fore,Style
info = '''
+===============================+
+
+    Script Get Network Info    +
+      By Zakarya               +
+
+===============================+
'''
print(info)
def network(pkt):
    if (pkt.haslayer(TCP)):
        print('   PACKETS IS SEND......!',Fore.RED,'+TCP_PROTOCOL+')
        print('',Fore.WHITE,'--------------------')
        s_ip = pkt[IP].src
        d_ip = pkt[IP].dst
        print('',Fore.RED,'\tSOURCE_IP \t= \t',Fore.GREEN,'', s_ip)
        print('',Fore.RED,'\tDEST_IP \t= \t',Fore.GREEN,'',  d_ip)
        s_port = pkt.sport
        d_port = pkt.dport
        print('',Fore.RED,'\tSOURCE_PORT \t= \t',Fore.RED,'', str(s_port))
        print('',Fore.RED,'\tDEST_PORT \t= \t',Fore.GREEN,'', str(d_port))
        if pkt.haslayer(Raw) :
            print('',Fore.BLUE,'DATA : ',Fore.YELLOW,'', pkt[Raw].load)
        print('',Fore.BLUE,'SIZE DATA :',Fore.YELLOW,'' + str(len(pkt[TCP])))
        print('',Style.BRIGHT,'--------------------------------')
sniff(iface ='Wi-Fi', prn = network)

import socket
import colorama
from colorama import Back,Fore
colorama.init(autoreset=True)

print ("======================================")
print ("1]- Get Ip\n2]- Get server")
print ("======================================")
choose = input(Fore.RED + "[Select Options :")

if choose == "1" :
    host = input(Fore.RED+"Enter site or hostname :")
    ip = socket.gethostbyname(host)
    print (Fore.GREEN + "\n                       ",ip)

#Get server
if choose == "2" :
    port = int(input("\033[32mEnter the port to server:"))
    server = socket.getservbyport(port)
    print (Fore.GREEN + "\n                        ",server)
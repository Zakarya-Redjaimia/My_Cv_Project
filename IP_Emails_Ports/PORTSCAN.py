from socket import socket , AF_INET , SOCK_STREAM , getservbyport
from optparse import OptionParser

info = '''
==============================

PORT\tSTATE\tSERVICES

==============================
'''
print(info)
parser = OptionParser()
parser.add_option('-t' , '--target',dest='ip',help='SET IP[PC] or IP[site]')
(options, args) = parser.parse_args()

for ports in range(1,100):
    so = socket(AF_INET , SOCK_STREAM)
    so.settimeout(0.2)
    try:
        con = so.connect((ip,ports))
        if con == None :
            print (ports,"\tOPEN\t")
    except Exception:
        print(ports,"\tCLOSED\t")
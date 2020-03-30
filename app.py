import socket
import ipapi


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

ipapi.location(
    ip=hostname, key='03ced33cda2d18dec5db6cc954efd92e', field='city')

print("Your PC Name is:" + hostname)
print("Your PC IP Address is: " + IPAddr)


print(ipapi.location(field='city'))

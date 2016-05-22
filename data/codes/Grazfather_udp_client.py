import socket
target_host = "127.0.0.1"target_port = 80
# create a socket objectclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# send some dataclient.sendto("AAABBBCCC", (target_host, target_port))
# receive some datadata, addr = client.recvfrom(4096)
print data
import socket
target_host = "www.google.com"target_port = 80
# create a socket objectclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the clientclient.connect((target_host, target_port))
# send some dataclient.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
# receive some dataresponse = client.recv(4096)
print response
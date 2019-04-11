import socket 
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # For UDP 
udp_host = socket.gethostname() # Host IP 
udp_port = 5005 # specified port to connect 
msg = "Hello this is client !".encode() 
print ("UDP target IP:", udp_host) 
print ("UDP target Port:", udp_port) 
sock.sendto(msg,(udp_host,udp_port))

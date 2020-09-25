import socket
import sys

while True:
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host_name = str(sys.argv[1])
    port_name = int(sys.argv[2])
    
    #Send Message to Server
    msg = input("Input Message to {}:{} = ".format(host_name,port_name))
    if ( msg == "bye"):
        break
    client.connect((host_name,port_name))
    client.send(msg.encode())
    
    #Receive Reply from Server
    data = client.recv(1024)
    print("Server                        = {}" .format(data.decode()))
    client.close()
    
print("Goodbye!")
client.close()
# Reference from PowerPoint
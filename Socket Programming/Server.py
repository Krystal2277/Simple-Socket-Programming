import socket
import threading

def handler(client,addr):
    data = client.recv(1024)
    print("{}:[{}] = {} ".format(addr[0],addr[1],data.decode()))

print("Waiting For Message From Client... ")
while True:
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host_name = "localhost"
    port_name = 80
    
    server.bind((host_name,port_name))
    server.listen(10)

    client , addr = server.accept()
    
    handlers = threading.Thread(target=handler,args=(client,addr,))
    handlers.start()
    
    #Reply for Client
    msg = input("Input Reply       = ")
    client.send(msg.encode())
    client.close()
    
    print("Waiting For Reply ... ")
    server.close()
# Reference from PowerPoint    
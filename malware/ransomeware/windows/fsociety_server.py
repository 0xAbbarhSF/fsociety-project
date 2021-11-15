import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("IP to listen on: ")

port = int(input("Port to listenon : "))

serversocket.bind((host, port))

serversocket.listen(2)

print("Fsociety Is up! on "+str(port))

while True:
     
     clientsocket,address = serversocket.accept()
     
    # print(clientsocket.recv(2048).decode())

     print("[+] Recevied Connection From %s " % str(address))
     print("[+] private key:\n")
     print(clientsocket.recv(2048).decode())
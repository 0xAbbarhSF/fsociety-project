import socket
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = sys.argv[1]

port = int(sys.argv[2])

serversocket.bind((host, port))

serversocket.listen(2)

print("Fsociety Is up! on "+str(port))

while True:
     
     clientsocket,address = serversocket.accept()
     
    # print(clientsocket.recv(2048).decode())

     print("[+] Recevied Connection From %s " % str(address[1]))
     print("[+] private key:\n")
     print(clientsocket.recv(2048).decode())
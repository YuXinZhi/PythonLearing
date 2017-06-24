from socket import *

myhost=''
myport=8080
sockobj=socket(AF_INET , SOCK_STREAM)
sockobj.bind((myhost , myport))
sockobj.listen(64)
while True:
    connection,address=sockobj.accept()
    print("connect by:",address)
    while True:
        data = connection.recv(1024)
        if not data:
            break
        connection.send("echo:".encode()+data)
    connection.close()
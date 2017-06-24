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
        data=connection.recv(1024)
        print(data)
        e = 'echo' + data
        e = e.encode()
        print(type(e))
        if not data:
            break
        connection.send(e)
    connection.close()
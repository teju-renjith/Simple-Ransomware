import os
from cryptography.fernet import Fernet

files=[]

for file in os.listdir():
	if file == "Danger.py":
		continue
	if file == "decrypt.py":
		continue
	if file == "recv_encryptionkey.key":
		continue
	files.append(file)
	
with open("recv_encryptionkey.key","rb") as K:
	key = K.read()
	
for file in files:
	with open(file,"rb") as f:
		contents = f.read()
	decrypted_contents = Fernet(key).decrypt(contents)
	with open(file,"wb") as f:
		f.write(decrypted_contents)

import os
from socket import *
from operator import xor

# DECRYPTION using OTP
def decryptKey(cipherkey):
        k = -4
        character=0
        key = ""
        for character in cipherkey:
                c = (ord(character) + k)% 127 
                key += chr(c) 
        return key

# character to binary
def Xor(c1,c2):
    c = chr(ord(c1)^ord(c2)) # convert characters to ASCII values 
    return c

# Decrypts ciphertext into plaintext using the OTP
def decrypt(ciphertext, key):
    plaintext = ""

    for i in range(len(ciphertext)):
        plaintext+=Xor(ciphertext[i], key[i])
    return plaintext
   
# MAIN CODE
ipAddr = "127.0.0.1"

# Socket Port = 2500 for transmission of key
keyPort = 2500

# Socket Port = 2501 for transmission of data
serverPort = 2501

print("-- Program B --\n\n")

# RECEIVING KEY
serverKey = socket(AF_INET, SOCK_STREAM)
serverKey.bind((ipAddr,keyPort))
serverKey.listen(1)
connectionSocket, addr = serverKey.accept()

# Get OTP
cipherKey = connectionSocket.recv(1024).decode("utf-8") 
key = decryptKey(cipherKey)

# New connection
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((ipAddr,serverPort)) # using port for data communication
serverSocket.listen(1)
connectionSocket, addr = serverSocket.accept()

# Receiving data file
Biden = connectionSocket.recv(1024).decode("utf-8")  
file = open('Biden.dat', "w")
file.write(Biden)
file.close()

# Decryption Process
data = decrypt(Biden,key)
print(data)
connectionSocket.close()

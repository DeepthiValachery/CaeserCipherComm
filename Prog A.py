import os.path
from socket import *
import random
from operator import xor


# ENCRYPTION using OTP
def createKey(len):
    key = ""
    i = 0
    for i in range(len):
        c = random.randint(0,127) 
        key += chr(c) 
    return key # pad generated

# Caesar cipher for key encryption
def encryptKey(key):
    k = 4
    character=0
    cipheredKey = ""
    for character in key:
        c = (ord(character) + k)% 127 
        cipheredKey += chr(c) 
    return cipheredKey

# character to binary
def Xor(c1,c2):
    c = chr(ord(c1)^ord(c2)) # convert characters to ASCII values
    return c

# Encrypts plaintext into ciphertext using the OTP
def encrypt(plaintext, key):
    ciphertext = ""
   
    for i in range(len(plaintext)):
        ciphertext+=Xor(plaintext[i], key[i])
    return ciphertext
 

# MAIN CODE
serverName = "localhost"

# Socket Port = 2500 for transmission of key
keyPort = 2500

# Socket Port = 2501 for transmission of data
serverPort = 2501

print("-- Program A --")

# READING FILE
filename = ('SleepyBiden.dat')
if (os.path.isfile(filename)==True):
    file = open(filename, 'r')
    plaintext = file.read()
    print("Reading File...")
    file.close()
   
    # Generate OTP and encrypt it 
    key = createKey(len(plaintext))
    cipherKey = encryptKey(key)

    # Connection
    clientKey = socket(AF_INET, SOCK_STREAM)
    clientKey.connect((serverName, keyPort))
   
    # TRANSMIT encrypted KEY
    clientKey.send(bytes(cipherKey, "utf-8"))    
    clientKey.close()


    # New connection
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
   
    # Encrypt, save & send  text
    print("Encrypting file...")
    Biden = encrypt(plaintext, key)
   
    file = open('Biden.dat', "w")
    file.write(Biden)
   
    clientSocket.send(bytes(Biden, "utf-8"))
    print("Connection closed.\n\n")
    clientKey.close()
   
else:
    print ("File does not exist!")

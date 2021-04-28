from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from tkinter import*



def keys(password):
    hash_obj=SHA256.new(password.encode('utf-8'))
    global hkey
    hkey=hash_obj.digest()
    print(hkey)
    len(hkey)
    return hkey


    


def encryptaes(info,passkey):
    msg=info
    BLOCK_SIZE=16
    PAD="{"
    padding=lambda s: s +(BLOCK_SIZE-len(s)% BLOCK_SIZE)* PAD
    cipher =AES.new(passkey,AES.MODE_ECB)
    result=cipher.encrypt(padding(msg).encode('utf-8'))
    return result
#msg="Hello"
#cipher_text=encrypt(msg,hkey)
#print(cipher_text)

def decryptaes(info,passkey):
    msg=info
    PAD="{"
    decipher=AES.new(passkey,AES.MODE_ECB)
    pt=decipher.decrypt(msg).decode('utf-8')
    pad_index=pt.find(PAD)
    result=pt[:pad_index]
    return result
#print(cipher_text)
#plaintext=decrypt(cipher_text,hkey)
#print(plaintext)



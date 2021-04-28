#from Crypto.Cipher import DES3
from Crypto.Cipher import DES
from Crypto import Random
from tkinter import*



    

def keydes(password):
    key=password
    if (len(key)!= 8):
        messagebox.showinfo("Information","Key Length Must be of 8 Byte")
        
    else:
        key=bytes(password,'utf-8')
        print (key)
        len(key)
        print(key)
        return key
    
        
    

def encryptdes(info,passkey):
    msg=info
    BLOCK_SIZE=8
    PAD="{"
    padding=lambda s: s +(BLOCK_SIZE-len(s)% BLOCK_SIZE)* PAD
    cipher =DES.new(passkey,DES.MODE_ECB)
    result=cipher.encrypt(padding(msg).encode('latin-1'))
    print(passkey)
    print(passkey)
    return result

def decryptdes(info,passkey):
    msg=info
    PAD="{"
    print(passkey)

    decipher=DES.new(passkey,DES.MODE_ECB)
    pt=decipher.decrypt(msg).decode('latin-1')
    pad_index=pt.find(PAD)
    result=pt[:pad_index]
    return result





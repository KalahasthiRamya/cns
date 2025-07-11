from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad
import os

key = b'8bytekey'
block_size = 8

def DES_enc(ptext):
    cipher = DES.new(key,DES.MODE_ECB)
    paddedtxt = pad(ptext.encode(),block_size)
    encrypted = cipher.encrypt(paddedtxt)
    return encrypted

def DES_dec(ctext):
    cipher = DES.new(key,DES.MODE_ECB)
    unpaddedtxt = cipher.decrypt(ctext)
    decrypted = unpad(unpaddedtxt,block_size)
    return decrypted.decode()

plaintext = "hello"

print("Encrypted : ",DES_enc(plaintext))
print("Decrypted : ",DES_dec(DES_enc(plaintext)))

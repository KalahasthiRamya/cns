import string
import random

def gen_key():
    letters = list(string.ascii_lowercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    return dict(zip(letters,shuffled))

def mono_enc(ptext,key):
    ctext = ""

    for char in ptext:
        if char.isalpha():
            lowerchar = char.lower()
            substituted = key[lowerchar]

            ctext += sustituted.upper() if char.isupper() else substituted
            
        else :
            ctext += char

    return ctext

def mono_dec(ctext,key):
    ptext = ""
    rev_key = {v:k for k,v in key.items()}

    for char in ctext:
        if char.isalpha():
            lowerchar = char.lower()
            original = rev_key[lowerchar]

            ptext += original.upper if char.isupper() else original

        else :
            ptext += char

    return ptext


key = gen_key()
plaintext = "hello"

print("Encrypted : ",mono_enc(plaintext,key))
print("Decrypted : ",mono_dec(mono_enc(plaintext,key),key))

        

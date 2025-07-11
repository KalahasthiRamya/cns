def vigenere_enc(ptext,key):
    ptext = ptext.upper().replace(" ","")
    key = key.upper()
    encrypted = ""

    for i in range(len(ptext)):
        p = ord(ptext[i]) - ord('A')
        k = ord(key[i%len(key)]) - ord('A')
        c = (p+k)%26
        encrypted += chr(c+ord('A'))

    return encrypted

def vigenere_dec(ctext,key):
    ctext = ctext.upper()
    key = key.upper()
    decrypted = ""

    for i in range(len(ctext)):
        c = ord(ctext[i]) - ord('A')
        k = ord(key[i % len(key)]) - ord('A')
        p = (c-k+26)%26
        decrypted += chr(p+ord('A'))

    return decrypted

plaintext = "hello"
key = "key"

c = vigenere_enc(plaintext,key)
print("Encrypted : ",c)

print("Decrypted : ",vigenere_dec(c,key))

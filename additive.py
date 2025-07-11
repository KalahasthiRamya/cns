def additive_enc(ptext,shift):
    result = ""

    for char in ptext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char)-shift_base+shift)%26+shift_base)

        else:
            result += char
    return result

def additive_dec(ctext,shift):
    return additive_enc(ctext,-shift)

plaintext = "hello"
key = 10

print("Encrypted : ",additive_enc(plaintext,key))
print("Decrypted : ",additive_dec(additive_enc(plaintext,key),key))

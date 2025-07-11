def caesar_enc(ptext,shift):
    result = ""

    for char in ptext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')

            result += chr((ord(char)-shift_base+shift)%26+shift_base)

        else:
            result += char

    return result

def caesar_dec(ctext,shift):
    return caesar_enc(ctext,-shift)

plain_text = "hello"
key = 3

print("Encrypted : ",caesar_enc(plain_text,key))
print("Decrypted : ",caesar_dec(caesar_enc(plain_text,key),key))


def encrypt(text,k):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if(char.isupper()):
            result += chr((ord(char) + k-65) % 26 + 65)

        else:
            result += chr((ord(char) + k-97) % 26 + 97)

    return result



def decrypt(result,k):
    plaintext = ""

    for i in range(len(result)):
        char = result[i]

        if(char.isupper()):
            plaintext += chr((ord(char) - k-65) % 26 + 65)

        else:
            plaintext += chr((ord(char) - k-97) % 26 + 97)

    return plaintext


text = "CRYPTOGRAPHY"
k = 3

print("Plain Text : "+text)
print("Key : "+str(k))

print("\nEncryption : ")
print("Cipher Text : "+encrypt(text,k))

print("\nDecryption : ")
print("Plain Text : "+decrypt(encrypt(text,k),k))
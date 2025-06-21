import random
import string

def generate_key():
    alphabet = list(string.ascii_uppercase)
    shuffled_alphabet = list(string.ascii_uppercase)
    random.shuffle(shuffled_alphabet)
    key = dict(zip(alphabet,shuffled_alphabet))
    return key


def encrypt(plaintext,key):
    ciphertext = []

    for char in plaintext.upper():
        if char in key:
            ciphertext.append(key[char])

        else:
            ciphertext.append(char)

    return "".join(ciphertext)




def decrypt(ciphertext,key):
    decrypted_txt = []

    inverse_key = {v: k for k, v in key.items()}

    for char in ciphertext.upper():
        if char in inverse_key:
            decrypted_txt.append(inverse_key[char])

        else:
            decrypted_txt.append(char)

    return "".join(decrypted_txt)


gen_keys = generate_key()
print(f"Generated Key : {gen_keys}")

msg = "HELLO WORLD"
print(f"Plain Text : {msg}")

encrypted = encrypt(msg,gen_keys)
print(f"Encrypted Message : {encrypted}")

decrypted = decrypt(encrypted,gen_keys)
print(f"Decrypted Message : {decrypted}")
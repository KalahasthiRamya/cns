import numpy as np
from math import gcd

def char_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_char(n):
    return chr((n%26)+ord('A'))

def text_to_vector(text):
    return [char_to_num(c) for c in text]

def vector_to_text(vec):
    return ''.join([num_to_char(n) for n in vec])

def is_invertible_mod26(matrix):
    det = int(round(np.linalg.det(matrix)))%26
    return gcd(det,26) == 1

def modinv(a,m):
    for i in range(1,m):
        if(a*i)%m == 1:
            return i

    raise ValueError(f"No modular inverse for {a} mod {m}")

def matrix_mod_inv(matrix,mod):
    n = matrix.shape[0]
    det = int(round(np.linalg.det(matrix)))%mod
    det_inv = modinv(det,mod)

    matrix_inv = (det_inv * np.round(det*np.linalg.inv(matrix)).astype(int))% mod
    return matrix_inv

def hill_enc(ptext,key_matrix):
    n = key_matrix.shape[0]
    if not is_invertible_mod26(key_matrix):
        raise ValueError("Key matrix is not invertible mod 26!")

    ptext = ptext.replace(" ","").upper()

    while len(ptext)%n != 0:
        ptext += 'X'

    result = ""

    for i in range(0,len(ptext),n):
        block = text_to_vector(ptext[i:i+n])
        vec = np.dot(key_matrix,block) % 26
        result += vector_to_text(vec)
    return result

def hill_dec(ctext,key_matrix):
    n = key_matrix.shape[0]
    inv_matrix = matrix_mod_inv(key_matrix,26)

    result = ""
    for i in range(0,len(ctext),n):
        block = text_to_vector(ctext[i:i+n])
        vec = np.dot(inv_matrix,block)%26
        result += vector_to_text(vec)

    return result


key = np.array([
    [6,24,1],
    [13,16,10],
    [20,17,15]
    ])

plaintext = "ACT"
cipher = hill_enc(plaintext,key)

print("Encrypted : ",cipher)
print("Decrypted : ",hill_dec(cipher,key))

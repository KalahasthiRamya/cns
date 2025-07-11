from math import gcd

p = 61
q = 53

n = p * q
phi = (p-1) * (q-1)

e = 17

def modinv(a,m):
    for i in range(1,m):
        if(a*i)%m == 1:
            return i

    raise Exception("No modular inverse found")

d = modinv(e,phi)

def RSA_enc(m):
    return pow(m,e,n)

def RSA_dec(c):
    return pow(c,d,n)

msg = 42
cipher = RSA_enc(msg)

print("Encrypted : ",cipher)
print("Decrypted : ",RSA_dec(cipher))

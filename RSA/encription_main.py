import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = mod_inverse(e, phi)

    return (e, n), (d, n)

def encrypt(plaintext, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return " ".join(map(str, cipher))

def decrypt(ciphertext, private_key):
    d, n = private_key
    cipher_numbers = map(int, ciphertext.split())
    plaintext = "".join(chr(pow(num, d, n)) for num in cipher_numbers)
    return plaintext

# Alice will send message to Bob
def main():
    # ===============================
    # Bob generates RSA keys
    # ===============================
    p = 61  
    q = 53
    bob_public_key, bob_private_key = generate_keypair(p, q)

    print("Bob's Public Key:", bob_public_key)
    print("Bob's Private Key:", bob_private_key)

    # ===============================
    # Alice reads plaintext
    # ===============================
    with open("plaintext_sender.txt", "r", encoding="utf-8") as f:
        plaintext = f.read()

    # Alice encrypts using Bob's public key
    ciphertext = encrypt(plaintext, bob_public_key)

    with open("ciphertext.txt", "w", encoding="utf-8") as f:
        f.write(ciphertext)

    # ===============================
    # Bob decrypts using his private key
    # ===============================
    decrypted_text = decrypt(ciphertext, bob_private_key)

    with open("plaintext_receiver.txt", "w", encoding="utf-8") as f:
        f.write(decrypted_text)


if __name__ == "__main__":
    main()


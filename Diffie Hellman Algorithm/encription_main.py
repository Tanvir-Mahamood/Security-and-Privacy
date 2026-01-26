import random

def diffie_hellman(p: int, g: int):
    private_key = random.randint(1, p-1)
    public_key = pow(g, private_key, p)
    return public_key, private_key


def encrypt(plaintext, key):
    encrypted = ""
    for char in plaintext:
        encrypted += chr((ord(char) + key) % 256)
    return encrypted

def decrypt(ciphertext, key):
    decrypted = ""
    for char in ciphertext:
        decrypted += chr((ord(char) - key) % 256)
    return decrypted

def main():
    # ===============================
    # Diffie–Hellman Key Exchange
    # ===============================
    p = 23  # A prime number
    g = 5   # A primitive root modulo p
    alice_public_key, alice_private_key = diffie_hellman(p, g)
    bob_public_key, bob_private_key = diffie_hellman(p, g)

    # Private key should be kept secret by both parties

    print("Alice Public Key:", alice_public_key)
    print("Alice Private Key:", alice_private_key)
    print("Bob Public Key:", bob_public_key)
    print("Bob Private Key:", bob_private_key)

    alice_secret_key = pow(bob_public_key, alice_private_key, p)
    bob_secret_key = pow(alice_public_key, bob_private_key, p)

    print("Alice Secret Key:", alice_secret_key)
    print("Bob Secret Key:", bob_secret_key)

    # ===============================
    # Alice sends message to Bob
    # ===============================
    with open("plaintext_sender.txt", "r", encoding="utf-8") as f:
        plaintext = f.read()

    ciphertext = encrypt(plaintext, alice_secret_key)

    with open("ciphertext.txt", "w", encoding="utf-8") as f:
        f.write(ciphertext)

    # ===============================
    # Bob receives & decrypts
    # ===============================
    decrypted_text = decrypt(ciphertext, bob_secret_key)

    with open("plaintext_receiver.txt", "w", encoding="utf-8") as f:
        f.write(decrypted_text)


if __name__ == "__main__":
    main()

import sha1
import rsa

def generate_rsa_keypair():
    return rsa.generate_keypair(61, 53) 


def sign_with_private_key(message: str, private_key) -> bytes:
    message_hash = sha1.SHA1(message)
    return rsa.RSAencrypt(message_hash, private_key)


def verify_with_public_key(message: str, signature: bytes, public_key) -> bool:
    message_hash = sha1.SHA1(message)
    decrypted_hash = rsa.RSAdecrypt(signature, public_key)
    return message_hash == decrypted_hash


def build_packet(message: str, signature: bytes) -> bytes:
    return f"{message}||{signature}".encode('utf-8')


def split_packet(packet: bytes):
    message, signature = packet.decode('utf-8').split("||")
    return message, signature


def main():
    with open("sender_inbox.txt", "r", encoding="utf-8") as f:
        sender_message = f.read().strip()

    private_key, public_key = generate_rsa_keypair()

    # Sender side
    signature = sign_with_private_key(sender_message, private_key)
    packet = build_packet(sender_message, signature)

    # Receiver side
    received_message, received_signature = split_packet(packet)
    is_valid = verify_with_public_key(received_message, received_signature, public_key)

    if is_valid:
        with open("receiver_inbox.txt", "w", encoding="utf-8") as f:
            f.write(received_message)
        print("Signature is valid. Message stored in receiver_inbox.txt")
    else:
        print("Signature is NOT valid. Message rejected.")


if __name__ == "__main__":
    main()
import hashlib

try:
    from cryptography.hazmat.primitives.asymmetric import rsa
except ImportError:
    raise SystemExit(
        "Missing dependency: cryptography\n"
        "Install it with: pip install cryptography"
    )

HEADER_SIZE = 20  # 10 chars for message length + 10 chars for signature length


def generate_rsa_keypair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key


def sha1_digest(data: bytes) -> bytes:
    return hashlib.sha1(data).digest()


def sign_with_private_key(message: str, private_key) -> bytes:
    msg_hash = sha1_digest(message.encode("utf-8"))
    numbers = private_key.private_numbers()
    n = numbers.public_numbers.n
    d = numbers.d

    hash_int = int.from_bytes(msg_hash, byteorder="big")
    sig_int = pow(hash_int, d, n)
    sig_len = (n.bit_length() + 7) // 8
    return sig_int.to_bytes(sig_len, byteorder="big")


def verify_with_public_key(message: str, signature: bytes, public_key) -> bool:
    local_hash = sha1_digest(message.encode("utf-8"))
    local_hash_int = int.from_bytes(local_hash, byteorder="big")

    numbers = public_key.public_numbers()
    n = numbers.n
    e = numbers.e

    sig_int = int.from_bytes(signature, byteorder="big")
    recovered_hash_int = pow(sig_int, e, n)
    return recovered_hash_int == local_hash_int


def build_packet(message: str, signature: bytes) -> bytes:
    msg_bytes = message.encode("utf-8")
    sig_bytes = signature

    msg_len = f"{len(msg_bytes):010d}".encode("ascii")
    sig_len = f"{len(sig_bytes):010d}".encode("ascii")
    return msg_len + sig_len + msg_bytes + sig_bytes


def split_packet(packet: bytes):
    msg_len = int(packet[:10].decode("ascii"))
    sig_len = int(packet[10:20].decode("ascii"))

    msg_start = HEADER_SIZE
    msg_end = msg_start + msg_len
    sig_end = msg_end + sig_len

    message = packet[msg_start:msg_end].decode("utf-8")
    signature = packet[msg_end:sig_end]
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
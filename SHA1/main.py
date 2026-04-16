def text_to_binary(plaintext):
    binary_string = ''.join(format(ord(char), '08b') for char in plaintext)
    return binary_string

def binary_to_hex(binary_string):
    hex_string = ''
    for i in range(0, len(binary_string), 4):
        four_bits = binary_string[i:i+4]
        hex_digit = format(int(four_bits, 2), 'x')
        hex_string += hex_digit
    return hex_string

def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def Round(i, hash_values, w_i):
    A, B, C, D, E = [int(hash_values[j*32:(j+1)*32], 2) for j in range(5)]

    if 0 <= i <= 19:
        f = (B & C) | ((~B) & D)
        k = 0x5A827999
    elif 20 <= i <= 39:
        f = B ^ C ^ D
        k = 0x6ED9EBA1
    elif 40 <= i <= 59:
        f = (B & C) | (B & D) | (C & D)
        k = 0x8F1BBCDC
    else:
        f = B ^ C ^ D
        k = 0xCA62C1D6

    temp = left_rotate(A, 5) + f + E + k + w_i
    temp = temp & 0xFFFFFFFF

    E = D
    D = C  
    C = left_rotate(B, 30)
    B = A
    A = temp
    
    return ''.join(format(value, '032b') for value in [A, B, C, D, E])

def MSA(block, initial_hash_binary):
    w = [0] * 80
    for i in range(16):
        w[i] = int(block[i*32:(i+1)*32], 2)

    for i in range(16, 80):
        w[i] = (w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16])

    hash_binary_new = initial_hash_binary
    for i in range(0, 80):
        hash_binary_new = Round(i, hash_binary_new, w[i])

    return str(hash_binary_new)


def SHA1(message):
    message_binary = text_to_binary(message)
    length = len(message_binary)
    block_size = 512

    if length > 2**64 - 1:
        raise ValueError("Message is too long to be processed by SHA-1.")
    elif length == 0:
        return ""

    initial_hash_values = [
        0x67452301,
        0xEFCDAB89,
        0x98BADCFE,
        0x10325476,
        0xC3D2E1F0
    ]
    initial_hash_binary = ''.join(format(hash_value, '032b') for hash_value in initial_hash_values)

    length_binary64 = format(length, '064b') 
    remaining_length = len(message_binary) % block_size + 64
    padding_length = (block_size - remaining_length) % block_size
    padding = '1' + '0' * (padding_length - 1)
    message_binary += padding + length_binary64

    blocks = [message_binary[i : i + block_size] for i in range(0, len(message_binary), block_size)]

    for block in blocks:
        hash_value = MSA(block, initial_hash_binary)
        initial_hash_binary = hash_value

    return initial_hash_binary

def main():
    with open("message.txt", "r", encoding="utf-8") as f:
        message = f.read()
    
    hash_value = SHA1(message)

    with open("hash.txt", "w", encoding="utf-8") as f:
        f.write(binary_to_hex(hash_value))
    

if __name__ == "__main__":
    main()

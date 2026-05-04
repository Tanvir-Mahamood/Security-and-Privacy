def text_to_binary(plaintext):
    return ''.join(format(byte, '08b') for byte in plaintext.encode('utf-8'))

def binary_to_hex(binary_string):
    hex_string = ''
    for i in range(0, len(binary_string), 4):
        four_bits = binary_string[i:i+4]
        hex_digit = format(int(four_bits, 2), 'x')
        hex_string += hex_digit
    return hex_string

def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def Round(i, A, B, C, D, E, w_i):
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

    temp = (left_rotate(A, 5) + f + E + k + w_i) & 0xFFFFFFFF

    E = D
    D = C  
    C = left_rotate(B, 30)
    B = A
    A = temp
    
    return A, B, C, D, E

def MSA(block, H):
    w = [0] * 80
    
    for i in range(16):
        w[i] = int(block[i*32:(i+1)*32], 2)

    for i in range(16, 80):
        w[i] = left_rotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1) # Added the left_rotate by 1 (The difference between SHA-0 and SHA-1)

    A, B, C, D, E = H

    for i in range(80):
        A, B, C, D, E = Round(i, A, B, C, D, E, w[i])

    # Add the compressed chunk to the current hash value (modulo 2^32)
    H[0] = (H[0] + A) & 0xFFFFFFFF
    H[1] = (H[1] + B) & 0xFFFFFFFF
    H[2] = (H[2] + C) & 0xFFFFFFFF
    H[3] = (H[3] + D) & 0xFFFFFFFF
    H[4] = (H[4] + E) & 0xFFFFFFFF

    return H

def SHA1(message):
    message_binary = text_to_binary(message)
    length = len(message_binary)
    block_size = 512

    if length > 2**64 - 1:
        raise ValueError("Message is too long to be processed by SHA-1.")

    initial_hash_values = [
        0x67452301,
        0xEFCDAB89,
        0x98BADCFE,
        0x10325476,
        0xC3D2E1F0
    ]

    length_binary64 = format(length, '064b') 
    
    padding_length = (448 - (length + 1) % 512) % 512
    padding = '1' + '0' * padding_length
    message_binary += padding + length_binary64

    blocks = [message_binary[i : i + block_size] for i in range(0, len(message_binary), block_size)]

    H = initial_hash_values[:]
    for block in blocks:
        H = MSA(block, H)

    # Convert the final integer hash values back to your binary string format
    return ''.join(format(h, '032b') for h in H)


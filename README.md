# Cryptography Algorithms Implementation

A comprehensive collection of cryptographic algorithms implemented in Python, featuring encryption, decryption, and hashing workflows with file-based input/output and visualization.

## 📚 Table of Contents

- [Overview](#overview)
- [Algorithms Implemented](#algorithms-implemented)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithms Description](#algorithms-description)
- [License](#license)

## 🔐 Overview

This repository contains implementations of various classical and modern cryptographic algorithms. It includes encryption/decryption workflows and hashing demonstrations through file-based operations, making it easy to understand how these algorithms work in practice.

## 🛠️ Algorithms Implemented

1. **CryptoBasics** - Classical Cryptography
   - 1.1. Caesar Cipher
   - 1.2. Mono Alphabetic Substitution Cipher
   - 1.3. Columnar Transposition Cipher

2. **DES** - Data Encryption Standard

3. **Triple DES** - Triple Data Encryption Standard

4. **AES** - Advanced Encryption Standard

5. **RSA** - Rivest–Shamir–Adleman Public-Key Cryptosystem

6. **Diffie-Hellman Algorithm** - Key Exchange Protocol

7. **Man in the Middle Attack** - Demonstration on Diffie-Hellman Key Exchange

8. **SHA1** - Secure Hash Algorithm 1 (Hashing)

## ✨ Features

- ✅ **File-based I/O**: Read plaintext from input files and write ciphertext to output files
- ✅ **Encryption & Decryption**: Complete implementation of both processes
- ✅ **Hashing Support**: Includes one-way hash generation with SHA1
- ✅ **Visualization**: Clear demonstration of cryptographic processes
- ✅ **Educational**: Well-structured code suitable for learning purposes
- ✅ **Multiple Algorithms**: Classical to modern cryptographic techniques

## 📁 Project Structure

```
Security and Privacy Sessional/
│
├── CryptoBasics/
│   ├── encription_main.py
│   ├── plaintext_sender.txt
│   ├── plaintext_receiver.txt
│   └── ciphertext.txt
│
├── DES Data Encryption Standard/
│   ├── encription_main.py
│   ├── plaintext_sender.txt
│   ├── plaintext_receiver.txt
│   └── ciphertext.txt
│
├── Triple DES/
│   ├── encription_main.py
│   ├── plaintext_sender.txt
│   ├── plaintext_receiver.txt
│   └── ciphertext.txt
│
├── AES Advanced Encryption Standard/
│   ├── encription_main.py
│   ├── plaintext_sender.txt
│   ├── plaintext_receiver.txt
│   ├── ciphertext.txt
│   └── aes_debug_log.txt
│
├── RSA/
│   ├── encription_main.py
│   ├── plaintext_sender.txt
│   ├── plaintext_receiver.txt
│   └── ciphertext.txt
│
├── Diffie Hellman Algorithm/
│   ├── encription_main.py
│   ├── plaintext_sender.txt
│   ├── plaintext_receiver.txt
│   └── ciphertext.txt
│
├── Man in the Middle Attack/
│   ├── encription_main.py
│   ├── Alice_Inbox.txt
│   ├── Bob_Inbox.txt
│   ├── Darth_Receiving.txt
│   └── Darth_Sending.txt
│
└── SHA1/
    ├── main.py
    ├── message.txt
    ├── hash.txt
    └── test.py
```

## 🔧 Installation

### Prerequisites

- Python 3.x
- Required Python packages (install using pip):

```bash
pip install pycryptodome
```

### Clone the Repository

```bash
git clone https://github.com/yourusername/cryptography-algorithms.git
cd cryptography-algorithms
```

## 🚀 Usage

Each algorithm is contained in its own directory with a main Python file and associated text files for input/output.

Most modules use `encription_main.py`, while the SHA1 module uses `main.py`.

### General Steps:

1. Navigate to the desired algorithm directory
2. Edit the input message file (for example, `plaintext_sender.txt` or `message.txt`)
3. Run the module script (commonly `encription_main.py`, or `main.py` for SHA1):

```bash
python encription_main.py
```

4. View the results in the output files

### Example: Running Caesar Cipher

```bash
cd "CryptoBasics"
python encription_main.py
```

The program will:
- Read plaintext from `plaintext_sender.txt`
- Encrypt the message
- Write ciphertext to `ciphertext.txt`
- Decrypt the ciphertext
- Write decrypted text to `plaintext_receiver.txt`

## 📖 Algorithms Description

### 1. CryptoBasics

**Classical Cryptography Techniques:**

- **Caesar Cipher**: Substitution cipher that shifts letters by a fixed number
- **Mono Alphabetic Substitution**: Each letter is replaced by another letter according to a key
- **Columnar Transposition**: Characters are rearranged based on a columnar pattern

### 2. DES (Data Encryption Standard)

A symmetric-key algorithm that uses a 56-bit key to encrypt 64-bit blocks of data through 16 rounds of permutation and substitution.

### 3. Triple DES (3DES)

An enhancement of DES that applies the DES cipher algorithm three times to each data block, providing stronger encryption.

### 4. AES (Advanced Encryption Standard)

Modern symmetric encryption standard using key sizes of 128, 192, or 256 bits. Considered highly secure and widely used today.

### 5. RSA

An asymmetric cryptographic algorithm using public and private keys. Based on the mathematical difficulty of factoring large prime numbers.

### 6. Diffie-Hellman Algorithm

A key exchange protocol that allows two parties to establish a shared secret key over an insecure channel.

### 7. Man in the Middle Attack

A demonstration of security vulnerabilities in the Diffie-Hellman key exchange, showing how an attacker (Darth) can intercept communications between Alice and Bob.

### 8. SHA1 (Secure Hash Algorithm 1)

A one-way cryptographic hash function that converts an input message into a fixed-length digest. This module demonstrates hash generation and verification-oriented workflow using file input/output.

## 📝 License

This project is open-source and available for educational purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

## 📧 Contact

For questions or suggestions, please open an issue in this repository.

---

**⚠️ Disclaimer**: This repository is intended for educational purposes only. Use these implementations to learn about cryptography, but rely on established cryptographic libraries for production systems.


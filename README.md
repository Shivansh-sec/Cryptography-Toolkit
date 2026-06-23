# Cryptography Toolkit

## Overview

Cryptography Toolkit is a Python-based application developed to demonstrate the implementation of fundamental cryptographic algorithms, including AES-256 encryption, RSA encryption/decryption, and SHA-256 hashing.

The project provides an interactive graphical interface that allows users to explore encryption, decryption, key generation, and hashing concepts through practical implementation.

---

## Objective

The objective of this project is to implement and demonstrate commonly used cryptographic algorithms in order to understand:

* Symmetric encryption
* Asymmetric encryption
* Hashing techniques
* Secure communication principles
* Cryptographic key management

---

## Features

### AES-256 Encryption

* Encrypt plaintext using AES-256
* Password-based key derivation
* Secure ciphertext generation

### AES-256 Decryption

* Decrypt ciphertext using the original password
* Recover the original plaintext

### RSA Cryptography

* Generate RSA public and private key pairs
* Encrypt messages using a public key
* Decrypt messages using a private key

### SHA-256 Hashing

* Generate SHA-256 hashes
* Demonstrate one-way hashing
* Verify data integrity

### Graphical User Interface

* Built using Tkinter
* Simple algorithm selection
* Interactive encryption and hashing operations

---

## Technologies Used

* Python
* Tkinter
* PyCryptodome
* Hashlib

---

## Project Structure

```text
Cryptography-Toolkit/
│
├── src/
│   ├── aes_module.py
│   ├── rsa_module.py
│   ├── sha_module.py
│   ├── gui.py
│   ├── main.py
│   └── __init__.py
│
├── docs/
├── screenshots/
├── tests/
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python -m src.main
```

---

## Algorithms Implemented

### AES (Advanced Encryption Standard)

AES is a symmetric encryption algorithm that uses the same key for both encryption and decryption.

### RSA (Rivest-Shamir-Adleman)

RSA is an asymmetric encryption algorithm that uses a public key for encryption and a private key for decryption.

### SHA-256

SHA-256 is a cryptographic hashing algorithm used to generate a fixed-length hash value for integrity verification.

---

## Learning Outcomes

This project helped in understanding:

* Cryptography fundamentals
* Symmetric and asymmetric encryption
* Hashing algorithms
* Secure communication concepts
* Practical implementation of cryptographic techniques

---

## Future Enhancements

* File encryption and decryption
* Additional cryptographic algorithms
* Digital signature implementation
* Enhanced key management features

---

## Author

Shivansh

B.Tech Computer Science Engineering Student

---

## License

This project is licensed under the MIT License.

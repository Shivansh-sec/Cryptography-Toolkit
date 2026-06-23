"""
aes_module.py
-------------

AES-256 Encryption and Decryption Module

Features:
- AES-256 Encryption
- AES-256 Decryption
- Secure key derivation using SHA-256
- Random IV generation
- Base64 encoded output

Author: Shivansh
"""

import base64
import hashlib

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class AESModule:

    BLOCK_SIZE = AES.block_size

    @staticmethod
    def derive_key(password: str) -> bytes:
        """
        Generate a 32-byte AES-256 key
        from a password using SHA-256.
        """

        return hashlib.sha256(
            password.encode("utf-8")
        ).digest()

    @staticmethod
    def pad(data: bytes) -> bytes:
        """
        PKCS7 Padding
        """

        padding_length = (
            AESModule.BLOCK_SIZE
            - len(data) % AESModule.BLOCK_SIZE
        )

        return (
            data +
            bytes([padding_length])
            * padding_length
        )

    @staticmethod
    def unpad(data: bytes) -> bytes:
        """
        Remove PKCS7 Padding
        """

        padding_length = data[-1]

        return data[:-padding_length]

    @staticmethod
    def encrypt(
        plaintext: str,
        password: str
    ) -> str:
        """
        Encrypt text using AES-256.
        """

        key = AESModule.derive_key(password)

        iv = get_random_bytes(
            AES.block_size
        )

        cipher = AES.new(
            key,
            AES.MODE_CBC,
            iv
        )

        encrypted_data = cipher.encrypt(
            AESModule.pad(
                plaintext.encode("utf-8")
            )
        )

        final_data = (
            iv +
            encrypted_data
        )

        return base64.b64encode(
            final_data
        ).decode("utf-8")

    @staticmethod
    def decrypt(
        ciphertext: str,
        password: str
    ) -> str:
        """
        Decrypt AES-256 ciphertext.
        """

        key = AESModule.derive_key(password)

        raw_data = base64.b64decode(
            ciphertext
        )

        iv = raw_data[:AES.block_size]

        encrypted_data = raw_data[
            AES.block_size:
        ]

        cipher = AES.new(
            key,
            AES.MODE_CBC,
            iv
        )

        decrypted_data = cipher.decrypt(
            encrypted_data
        )

        return AESModule.unpad(
            decrypted_data
        ).decode("utf-8")
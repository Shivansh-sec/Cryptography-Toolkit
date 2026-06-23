from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


class RSAModule:

    @staticmethod
    def generate_keys():

        key = RSA.generate(2048)

        private_key = key.export_key().decode()

        public_key = (
            key.publickey()
            .export_key()
            .decode()
        )

        return private_key, public_key

    @staticmethod
    def encrypt(
        plaintext,
        public_key
    ):

        key = RSA.import_key(public_key)

        cipher = PKCS1_OAEP.new(key)

        encrypted = cipher.encrypt(
            plaintext.encode()
        )

        return base64.b64encode(
            encrypted
        ).decode()

    @staticmethod
    def decrypt(
        ciphertext,
        private_key
    ):

        key = RSA.import_key(private_key)

        cipher = PKCS1_OAEP.new(key)

        decrypted = cipher.decrypt(
            base64.b64decode(ciphertext)
        )

        return decrypted.decode()
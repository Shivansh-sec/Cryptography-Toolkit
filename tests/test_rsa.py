import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from src.rsa_module import RSAModule


private_key, public_key = (
    RSAModule.generate_keys()
)

message = "Hello RSA"

encrypted = RSAModule.encrypt(
    message,
    public_key
)

print("Encrypted:")
print(encrypted)

decrypted = RSAModule.decrypt(
    encrypted,
    private_key
)

print("\nDecrypted:")
print(decrypted)
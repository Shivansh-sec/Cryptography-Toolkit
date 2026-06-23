from src.aes_module import AESModule


message = "Hello Cryptography"

password = "mysecurepassword"

encrypted = AESModule.encrypt(
    message,
    password
)

print("Encrypted:")
print(encrypted)

decrypted = AESModule.decrypt(
    encrypted,
    password
)

print("\nDecrypted:")
print(decrypted)
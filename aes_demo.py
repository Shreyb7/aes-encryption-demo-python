"""
AES Encryption Demo

Description:
A simple Python program demonstrating AES encryption and decryption
using the PyCryptodome library.

"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def aes_encrypt_decrypt():
    key = b'16byteaeskey1234'   # 16-byte AES key
    cipher = AES.new(key, AES.MODE_ECB)

    text = input("Enter plaintext: ").encode()

    ciphertext = cipher.encrypt(pad(text, AES.block_size))
    print("\nEncrypted (AES):", ciphertext)

    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    print("Decrypted (AES):", decrypted.decode())


if __name__ == "__main__":
    aes_encrypt_decrypt()

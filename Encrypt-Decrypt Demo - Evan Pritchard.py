from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

message = b"Alan Turing"

# Symmetric Encryption
key = Fernet.generate_key()
cipher = Fernet(key)

encrypted = cipher.encrypt(message)
decrypted = cipher.decrypt(encrypted)


print("\n\033[1;36mSymmetric Encryption\033[0m\n")
print("\033[1;36mKey:\033[0m", key, "\n")
print("\033[1;36mOriginal:\033[0m", message.decode(), "\n")
print("\033[1;36mEncrypted:\033[0m", encrypted.hex(), "\n")
print("\033[1;36mDecrypted:\033[0m", decrypted.decode(), "\n")



# Asymmetric Encryption
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)


print("\n\033[1;36mAsymmetric Encryption\033[0m\n")
print("\033[1;36mPublic Key:\033[0m", public_key.public_numbers(), "\n")
print("\033[1;36mPrivate Key (d):\033[0m", private_key.private_numbers().d, "\n")
print("\033[1;36mOriginal:\033[0m", message.decode(), "\n")
print("\033[1;36mEncrypted:\033[0m", encrypted.hex(), "\n")
print("\033[1;36mDecrypted:\033[0m", decrypted.decode(), "\n")


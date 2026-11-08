# SDEV245---Encrypt-Decrypt-Demo
Module 2 Assignment


# Encryption Demo

  This program uses Python to show how symmetric and asymmetric encryption work. I used the cryptography library to encrypt and decrypt a short message using both methods.

## Symmetric Encryption

  For symmetric encryption, I used Fernet, which uses AES encryption. The program generates a single key that is used to both encrypt and decrypt the message. Symmetric encryption is generally faster, but both sides need access to the same key. This can be a security risk if someone else gets access to it.

## Asymmetric Encryption

  For asymmetric encryption, I used RSA, which generates a public and private key. The public key is used to encrypt the message, while the private key is used to decrypt it. I used RSA for this part instead of AES because AES uses a single secret key, while RSA demonstrates how two different keys work together. RSA is generally slower than symmetric encryption, but it allows information to be encrypted without having to share the private key.

## Program Output

  I used "Alan Turing" as the message because I thought it would be a funny nod to his mastery of cryptography. The program displays the keys, original message, encrypted message, and decrypted message for both methods. For symmetric encryption, the program displays the shared secret key. For asymmetric encryption, it displays the RSA public key and the private exponent (d), which is part of the private key. The encrypted messages are displayed in hexadecimal format, making the output easier to read than raw bytes. Both methods successfully decrypt the message back to "Alan Turing." The keys and encrypted results change each time the program runs because new keys are generated and the encryption methods use randomness.

## Conclusion

Both methods are used to protect information, but they handle encryption differently. Symmetric encryption is faster and works better for larger amounts of data, while asymmetric encryption allows information to be encrypted using a public key without sharing the private key. I know that both applications are usually used in conjunction as well.

You will first need to install the cryptography library:

python -m pip install cryptography

Then run the Python file:

python "Encrypt-Decrypt Demo - Evan Pritchard.py"

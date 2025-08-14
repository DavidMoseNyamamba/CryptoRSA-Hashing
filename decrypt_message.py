from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# Load private key
private_key = RSA.import_key(open('private.pem').read())

# Create a cipher object using the private key
decipher = PKCS1_OAEP.new(private_key)

# Read the encrypted message from the file
with open("encrypted_message.bin", "rb") as f:
    ciphertext = f.read()

# Decrypt the message
plaintext = decipher.decrypt(ciphertext)

print("Decrypted:", plaintext.decode())
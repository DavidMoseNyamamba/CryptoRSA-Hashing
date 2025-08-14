from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# Message to encrypt
message = b'This is a secret message.'

# Load public key
public_key = RSA.import_key(open('public.pem').read())

# Create a cipher object using the public key
cipher = PKCS1_OAEP.new(public_key)

# Encrypt the message
ciphertext = cipher.encrypt(message)

# Save the encrypted message to a file
with open("encrypted_message.bin", "wb") as f:
    f.write(ciphertext)

print("Message encrypted and saved to 'encrypted_message.bin'")
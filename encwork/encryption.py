# Created by MysteryBlokHed on 13/12/2019.
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key

def gen_fernet_key():
    """Generate a key to use with cryptography's Fernet."""
    key = Fernet.generate_key()
    return (key, Fernet(key))

def gen_rsa_private_key():
    """Generate an RSA cryptography private key object."""
    return rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

def get_rsa_public_key(private_key):
    """Get the public key from a cryptography private key object."""
    return private_key.public_key()

def get_rsa_public_key_text(public_key):
    """Get the text version of a public key from a cryptography public key object."""
    return public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

def encrypt_rsa(message, public_key):
    """Encrypt a message with a public key (text)."""
    key = load_pem_public_key(public_key, default_backend())
    return key.encrypt(message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

def decrypt_rsa(message, private_key):
    """Decrypt a message with a cryptography private key object."""
    return private_key.decrypt(message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

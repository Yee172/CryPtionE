from __init__ import PRIVATES_KEY_PATH, SPLITER
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


__all__ = ['decrypt']


with open(PRIVATES_KEY_PATH, 'rb') as f:
    decryptor = PKCS1_OAEP.new(RSA.importKey(f.read()))


def decrypt(ciphertext):
    return b''.join(map(decryptor.decrypt, ciphertext.split(SPLITER)))

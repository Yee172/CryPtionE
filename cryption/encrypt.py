from __init__ import PUBLIC_KEY_PATH, SECTION, SPLITER
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


__all__ = ['encrypt']


with open(PUBLIC_KEY_PATH, 'rb') as f:
    encryptor = PKCS1_OAEP.new(RSA.importKey(f.read()))


def encrypt(message):
    if isinstance(message, str):
        message = bytes(message, encoding='utf-8')
    elif not isinstance(message, bytes):
        message = bytes(str(message), encoding='utf-8')
    return SPLITER.join(map(encryptor.encrypt, [message[i * SECTION:(i + 1) * SECTION] for i in range((len(message) - 1) // SECTION + 1)]))

from __init__ import RSA_CONTROL, PUBLIC_KEY_PATH, PRIVATES_KEY_PATH
from Crypto.PublicKey import RSA


key = RSA.generate(RSA_CONTROL)
with open(PUBLIC_KEY_PATH, 'wb') as f:
    f.write(key.publickey().exportKey('PEM'))

with open(PRIVATES_KEY_PATH, 'wb') as f:
    f.write(key.exportKey('PEM'))

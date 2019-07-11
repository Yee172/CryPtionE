import os
import sys
__all__ = ['key_generator', 'encrypt', 'decrypt']


sys.path.append(os.path.dirname(os.path.abspath(__file__)))


PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC_KEY_PATH = PATH + '/public_key.pem'
PRIVATES_KEY_PATH = PATH + '/private_key.pem'
RSA_CONTROL = 2048
SECTION = 200
SPLITER = b'|--|'

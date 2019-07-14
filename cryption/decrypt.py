#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from header import PRIVATE_KEY_PATH
from header import PE_PATH
from header import PE_ORIGIN_PATH
from header import SPLITER
from header import solution_spliter
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


__all__ = ['decryPtE_for_solution']
__author__ = 'Yee_172'
__date__ = '2019/07/12'


with open(PRIVATE_KEY_PATH, 'rb') as f:
    decryptor = PKCS1_OAEP.new(RSA.importKey(f.read()))


def decrypt(ciphertext):
    return b''.join(map(decryptor.decrypt, ciphertext.split(SPLITER)))


def reverse_beautify(context):
    return ''.join(context.split('\n'))


def decryPtE(mixed_ciphertext):
    '''decryPtE
    
    decrytion in special way
    
    Arguments:
        mixed_ciphertext {str} -- mixed ciohertext
    
    Returns:
        str -- message hidden in the ciphertext
    '''
    head, body = solution_spliter(mixed_ciphertext)
    body = bytes.fromhex(reverse_beautify(body))
    return head + decrypt(body).decode()


def decryPtE_for_solution(solution_file_name):
    try:
        with open(PE_PATH + solution_file_name, 'r') as f:
            encrypted_solution = f.read()
    except:
        raise Exception
    with open(PE_ORIGIN_PATH + solution_file_name, 'w') as f:
        f.write(decryPtE(encrypted_solution))

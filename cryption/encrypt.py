#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from header import PUBLIC_KEY_PATH
from header import PE_PATH
from header import PE_ORIGIN_PATH
from header import SECTION
from header import SPLITER
from header import solution_spliter
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


__all__ = ['encryPtE_for_solution']
__author__ = 'Yee_172'
__date__ = '2019/07/12'


with open(PUBLIC_KEY_PATH, 'rb') as f:
    encryptor = PKCS1_OAEP.new(RSA.importKey(f.read()))


def encrypt(message, encoding='utf-8'):
    if isinstance(message, str):
        message = bytes(message, encoding=encoding)
    elif not isinstance(message, bytes):
        message = bytes(str(message), encoding=encoding)
    return SPLITER.join(map(encryptor.encrypt, [message[i * SECTION:(i + 1) * SECTION] for i in range((len(message) - 1) // SECTION + 1)]))


def encryPtE(all_message_in_file):
    '''encryPtE
    
    encryption in special way
    
    Arguments:
        all_message_in_file {str} -- message needed to be encrypted
    
    Returns:
        str -- mixed ciphertext
    '''
    head, body = solution_spliter(all_message_in_file)
    return head + encrypt(body).hex() + '\n'


def encryPtE_for_solution(solution_file_name):
    try:
        with open(PE_ORIGIN_PATH + solution_file_name, 'r') as f:
            solution = f.read()
    except:
        raise Exception
    with open(PE_PATH + solution_file_name, 'w') as f:
        f.write(encryPtE(solution))

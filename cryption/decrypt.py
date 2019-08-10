#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from header import ENCODING
from header import PRIVATE_KEY_PATH
from header import PE_PATH
from header import PE_ORIGIN_PATH
from header import SPLITER
from header import solution_spliter
from header import error_shower
from header import decryptor
from header import os


__all__ = ['decryPtE_for_solution']
__author__ = 'Yee_172'
__date__ = '2019/07/12'


def decrypt(ciphertext):
    return b''.join(map(decryptor.decrypt, ciphertext.split(SPLITER)))


def reverse_beautify(context):
    return ''.join(context.split('\n'))


def decryPtE(mixed_ciphertext, encoding=ENCODING):
    '''decryPtE
    
    decrytion in special way
    
    Arguments:
        mixed_ciphertext {str} -- mixed ciohertext
    
    Returns:
        str -- message hidden in the ciphertext
    '''
    head, body = solution_spliter(mixed_ciphertext)
    body = bytes.fromhex(reverse_beautify(body))
    return head + decrypt(body).decode(encoding=encoding)


def decryPtE_for_solution(solution_file_name, encoding=ENCODING):
    try:
        with open(os.path.join(PE_PATH, solution_file_name), 'r', encoding=encoding) as f:
            encrypted_solution = f.read()
        with open(os.path.join(PE_ORIGIN_PATH, solution_file_name), 'w', encoding=encoding) as f:
            f.write(decryPtE(encrypted_solution, encoding=encoding))
    except Exception as exception:
        raise Exception(exception.__class__.__name__)

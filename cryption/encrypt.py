#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from header import ENCODING
from header import PUBLIC_KEY_PATH
from header import PE_PATH
from header import PE_ORIGIN_PATH
from header import SECTION
from header import BLOCK
from header import SPLITER
from header import solution_spliter
from header import error_shower
from header import encryptor
import os


__all__ = ['encryPtE_for_solution']
__author__ = 'Yee_172'
__date__ = '2019/07/12'


def encrypt(message, encoding=ENCODING):
    if not isinstance(message, bytes):
        if not isinstance(message, str):
            message = str(message)
        message = bytes(message, encoding=encoding)
    return SPLITER.join(map(encryptor.encrypt, [message[i * SECTION:(i + 1) * SECTION] for i in range((len(message) - 1) // SECTION + 1)]))


def beautify(context):
    return '\n'.join(context[i * BLOCK:(i + 1) * BLOCK] for i in range((len(context) - 1) // BLOCK + 1))


def encryPtE(all_message_in_file, encoding=ENCODING):
    '''encryPtE
    
    encryption in special way
    
    Arguments:
        all_message_in_file {str} -- message needed to be encrypted
    
    Keyword Arguments:
        encoding {str} -- encoding (default: {header.ENCODING})
    
    Returns:
        str -- mixed ciphertext
    '''
    head, body = solution_spliter(all_message_in_file)
    return head + beautify(encrypt(body, encoding=encoding).hex()) + '\n'


def encryPtE_for_solution(solution_file_name, encoding=ENCODING):
    try:
        with open(os.path.join(PE_ORIGIN_PATH, solution_file_name), 'r', encoding=encoding) as f:
            solution = f.read()
        with open(os.path.join(PE_PATH, solution_file_name), 'w', encoding=encoding) as f:
            f.write(encryPtE(solution, encoding=encoding))
    except:
        raise Exception

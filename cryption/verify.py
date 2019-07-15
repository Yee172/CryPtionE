#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from header import ENCODING
from header import PUBLIC_KEY_PATH
from header import SIGNATURE_PATH
from header import PE_ORIGIN_PATH
from header import SIGNATURE_FILE_FAIL
from header import SIGNATURE_CONTEXT_FAIL
from header import SOLUTION_FILE_FAIL
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15


__all__ = ['verify_for_single_solution']
__author__ = 'Yee_172'
__date__ = '2019/07/14'


with open(PUBLIC_KEY_PATH, 'rb') as f:
    verifier = pkcs1_15.new(RSA.importKey(f.read()))


def verify(message, signature, encoding=ENCODING):
    if not isinstance(message, bytes):
        if not isinstance(message, str):
            message = str(message)
        message = bytes(message, encoding=encoding)
    if isinstance(signature, str):
        signature = bytes.fromhex(signature)
    try:
        verifier.verify(SHA256.new(message), signature)
        return True
    except:
        return False


def verify_for_single_solution(solution_file_name, encoding=ENCODING):
    try:
        with open(SIGNATURE_PATH, 'r', encoding=encoding) as f:
            raw_signatures = f.read().strip().split('\n')
    except:
        return SIGNATURE_FILE_FAIL
    try:
        with open(PE_ORIGIN_PATH + solution_file_name, 'r', encoding=encoding) as f:
            message = f.read()
    except:
        return SOLUTION_FILE_FAIL
    for each_raw_signature in raw_signatures[1:]:
        file_name, signature = each_raw_signature.split(',')
        if file_name == solution_file_name:
            break
        if file_name > solution_file_name:
            return SIGNATURE_CONTEXT_FAIL
    else:
        return SIGNATURE_CONTEXT_FAIL
    return verify(message, signature, encoding=encoding)

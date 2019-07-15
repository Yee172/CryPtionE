#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from header import ENCODING
from header import PRIVATE_KEY_PATH
from header import SIGNATURE_PATH
from header import PE_ORIGIN_PATH
from header import SOLUTION_FILE_HEADER
from header import signature_file_insurance
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import os


__all__ = ['sign_for_single_solution', 'sign_for_all_solutions']
__author__ = 'Yee_172'
__date__ = '2019/07/14'


with open(PRIVATE_KEY_PATH, 'rb') as f:
    signer = pkcs1_15.new(RSA.importKey(f.read()))


def sign(message, encoding=ENCODING):
    if not isinstance(message, bytes):
        if not isinstance(message, str):
            message = str(message)
        message = bytes(message, encoding=encoding)
    return signer.sign(SHA256.new(message)).hex()


def sign_for_single_solution(solution_file_name, encoding=ENCODING):
    signature_file_insurance()
    with open(SIGNATURE_PATH, 'r', encoding=encoding) as f:
        raw_signatures = f.read().strip().split('\n')
    with open(PE_ORIGIN_PATH + solution_file_name, 'r', encoding=encoding) as f:
        new_raw_signature = solution_file_name + ',' + sign(f.read(), encoding=encoding)
    i = 0
    for i, each_raw_signature in enumerate(raw_signatures[1:]):
        file_name, signature = each_raw_signature.split(',')
        if file_name > solution_file_name:
            break
    else:
        i += 1
    if raw_signatures[i].startswith(solution_file_name):
        file_name, signature = raw_signatures[i].split(',')
        raw_signatures[i] = new_raw_signature
    else:
        raw_signatures.insert(i + 1, new_raw_signature)
    with open(SIGNATURE_PATH, 'w') as f:
        f.write('\n'.join(raw_signatures) + '\n')


def sign_for_all_solutions(encoding=ENCODING):
    with open(SIGNATURE_PATH, 'w', encoding=encoding) as f:
        f.write('Filename,Signature\n')
        for solution_file_name in sorted(['/' + each_file_name for each_file_name in os.listdir(PE_ORIGIN_PATH) if each_file_name.startswith(SOLUTION_FILE_HEADER[1:]) and each_file_name.endswith('.py')]):
            with open(PE_ORIGIN_PATH + solution_file_name, 'r', encoding=encoding) as _f:
                f.write(solution_file_name + ',' + sign(_f.read(), encoding=encoding) + '\n')

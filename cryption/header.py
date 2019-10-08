#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import os


__author__ = 'Yee_172'
__date__ = '2019/07/12'


PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENCODING = 'utf-8'
PUBLIC_KEY_PATH = os.path.join(PATH, 'public_key.pem')
PRIVATE_KEY_PATH = os.path.join(PATH, 'private_key.pem')
SIGNATURE_PATH = os.path.join(PATH, 'signature.csv')
PE_PATH = os.path.join(PATH, 'PE')
PE_ORIGIN_PATH = os.path.join(PE_PATH, 'origin')
SOLUTION_FILE_HEADER = 'Problem_'
RSA_CONTROL = 2048
SECTION = 200
BLOCK = 100
SPLITER = b'|--|'
SHOW_LENGTH = 40


SIGNATURE_FILE_FAIL = 'Signature file not found'
SIGNATURE_CONTEXT_FAIL = 'Corresponding signature not found'
SOLUTION_FILE_FAIL = 'Solution file not found'


def hyphen_shower(info):
    print('-' * SHOW_LENGTH)
    if isinstance(info, str):
        print(info.center(SHOW_LENGTH))
    else:
        for each_info in info:
            print(each_info.center(SHOW_LENGTH))
    print('-' * SHOW_LENGTH)


def red_print(info):
    print('\033[31m' + info + '\033[0m')


def green_print(info):
    print('\033[32m' + info + '\033[0m')


def error_shower(info, exist_after_show=True):
    print('\033[31m')
    hyphen_shower(info)
    print('\033[0m')
    if exist_after_show:
        exit()


def success_shower(info):
    print('\033[32m')
    hyphen_shower(info)
    print('\033[0m')


def initialization():
    encryptor = ''
    decryptor = ''
    signer = ''
    verifier = ''
    load_error = []
    if os.path.exists(PUBLIC_KEY_PATH):
        try:
            with open(PUBLIC_KEY_PATH, 'rb') as f:
                public_key = RSA.importKey(f.read())
                encryptor = PKCS1_OAEP.new(public_key)
                verifier = pkcs1_15.new(public_key)
        except:
            load_error.append('Warning: Public key not valid'.ljust(SHOW_LENGTH))
    else:
        load_error.append('Warning: Public key not found'.ljust(SHOW_LENGTH))


    if os.path.exists(PRIVATE_KEY_PATH):
        try:
            with open(PRIVATE_KEY_PATH, 'rb') as f:
                private_key = RSA.importKey(f.read())
                decryptor = PKCS1_OAEP.new(private_key)
                signer = pkcs1_15.new(private_key)
        except:
            load_error.append('Warning: Private key not valid'.ljust(SHOW_LENGTH))
    else:
        load_error.append('Warning: Private key not found'.ljust(SHOW_LENGTH))


    if load_error:
        error_shower(load_error, False)

    return encryptor, decryptor, signer, verifier


def solution_spliter(all_message_in_file):
    hash_number, new_line_number = 0, 0
    for i, char in enumerate(all_message_in_file):
        if new_line_number > hash_number:
            break
        if char == '#' and all_message_in_file[i + 1] == ' ' and (i == 0 or all_message_in_file[i - 1] == '\n'):
            hash_number += 1
        if char == '\n':
            new_line_number += 1
    return all_message_in_file[:i], all_message_in_file[i:]


def signature_file_insurance(encoding=ENCODING):
    if not os.path.exists(SIGNATURE_PATH):
        with open(SIGNATURE_PATH, 'w', encoding=encoding) as f:
            f.write('Filename,Signature\n')


def global_path_insurance():
    if not os.path.exists(PE_PATH):
        os.makedirs(PE_PATH)
    if not os.path.exists(PE_ORIGIN_PATH):
        os.makedirs(PE_ORIGIN_PATH)


encryptor, decryptor, signer, verifier = initialization()


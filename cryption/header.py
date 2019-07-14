#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


__author__ = 'Yee_172'
__date__ = '2019/07/12'


PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC_KEY_PATH = PATH + '/public_key.pem'
PRIVATE_KEY_PATH = PATH + '/private_key.pem'
PE_PATH = PATH + '/PE'
PE_ORIGIN_PATH = PE_PATH + '/origin'
SOLUTION_FILE_HEADER = '/Problem_'
RSA_CONTROL = 2048
SECTION = 200
BLOCK = 100
SPLITER = b'|--|'
SHOW_LENGTH = 40


def solution_spliter(all_message_in_file):
    hash_number, new_line_number = 0, 0
    for i, char in enumerate(all_message_in_file):
        if new_line_number > hash_number:
            break
        if char == '#':
            hash_number += 1
        if char == '\n':
            new_line_number += 1
    return all_message_in_file[:i], all_message_in_file[i:]

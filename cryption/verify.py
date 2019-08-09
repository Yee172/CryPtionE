#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from header import ENCODING
from header import PUBLIC_KEY_PATH
from header import SIGNATURE_PATH
from header import PE_ORIGIN_PATH
from header import SOLUTION_FILE_HEADER
from header import SIGNATURE_FILE_FAIL
from header import SIGNATURE_CONTEXT_FAIL
from header import SOLUTION_FILE_FAIL
from header import error_shower
from header import verifier
from header import SHA256
from header import os


__all__ = ['verify_for_single_solution', 'verify_for_all_solutions']
__author__ = 'Yee_172'
__date__ = '2019/07/14'


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
        with open(os.path.join(PE_ORIGIN_PATH, solution_file_name), 'r', encoding=encoding) as f:
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


def verify_for_all_solutions(encoding=ENCODING):
    try:
        with open(SIGNATURE_PATH, 'r', encoding=encoding) as f:
            raw_signatures = f.read().strip().split('\n')[1:]
    except:
        return SIGNATURE_FILE_FAIL
    solution_without_signature = []
    signature_without_solution = []
    invalid_solution = []
    signature_index = 0
    signature_file_name, signature = raw_signatures[signature_index].split(',')
    signature_index += 1
    for solution_file_name in sorted([each_file_name for each_file_name in os.listdir(PE_ORIGIN_PATH) if each_file_name.startswith(SOLUTION_FILE_HEADER) and each_file_name.endswith('.py')]):
        if solution_file_name < signature_file_name:
            solution_without_signature.append(solution_file_name)
            continue
        while signature_file_name < solution_file_name:
            signature_without_solution.append(signature_file_name)
            if signature_index < len(raw_signatures):
                signature_file_name, signature = raw_signatures[signature_index].split(',')
                signature_index += 1
            else:
                signature_file_name = SOLUTION_FILE_HEADER + '9999.py'
                break
        if signature_file_name != solution_file_name:
            continue
        with open(os.path.join(PE_ORIGIN_PATH, solution_file_name), 'r', encoding=encoding) as f:
            message = f.read()
        if not verify(message, signature, encoding=ENCODING):
            invalid_solution.append(solution_file_name)
        if signature_index < len(raw_signatures):
            signature_file_name, signature = raw_signatures[signature_index].split(',')
            signature_index += 1
        else:
            signature_file_name = SOLUTION_FILE_HEADER + '9999.py'
    return solution_without_signature, signature_without_solution, invalid_solution

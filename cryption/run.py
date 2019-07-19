#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from header import PE_PATH
from header import PE_ORIGIN_PATH
from header import SOLUTION_FILE_HEADER
from header import SHOW_LENGTH
from header import hyphen_shower
from header import error_shower
from header import success_shower
from header import encryptor
from header import decryptor
from header import signer
from header import verifier
from key_generator import generate
from encrypt import encryPtE_for_solution
from decrypt import decryPtE_for_solution
from sign import sign_for_single_solution
from sign import sign_for_all_solutions
from verify import verify_for_single_solution
from verify import verify_for_all_solutions
import os


__all__ = []
__author__ = 'Yee_172'
__date__ = '2019/07/12'


def get_solution_file_name():
    n = input('Input the index of problem: ')
    try:
        n = int(n)
    except:
        error_shower('Invalid input!')
    return SOLUTION_FILE_HEADER + ('%04d' % n) + '.py'


if __name__ == '__main__':
    hyphen_shower('Welcome to CryPtionE')
    print('Only \033[32mgreen options\033[0m are available')
    print()

    print('\033[32m[1] Generate a new pair of key\033[0m')

    print('\033[32m' if encryptor else '\033[31m', end='')
    print('[2] Encrypt  single  solution')
    print('[3] Encrypt  all     solutions\033[0m')

    print('\033[32m' if decryptor else '\033[31m', end='')
    print('[4] Decrypt  single  solution')
    print('[5] Decrypt  all     solutions\033[0m')

    print('\033[32m' if signer else '\033[31m', end='')
    print('[6] Sign     single  solution')
    print('[7] Sign     all     solutions\033[0m')

    print('\033[32m' if verifier else '\033[31m', end='')
    print('[8] Verify   single  solution')
    print('[9] Verify   all     solutions\033[0m')
    n = input('Input a number to choose [1 - 9]: ')
    try:
        n = int(n)
    except:
        error_shower('Invalid input!')
    if not 0 < n < 10:
        error_shower('Input not in the range!')
    if n == 1:
        generate()
        success_shower('A new pair of key created')
    if n == 2:
        if not encryptor:
            error_shower('Public key unavailable')
        solution_file_name = get_solution_file_name()
        try:
            encryPtE_for_solution(solution_file_name)
        except:
            error_shower('Solution not exist!')
        sign_for_single_solution(solution_file_name)
        success_shower(solution_file_name + ' has been encrypted')
    if n == 3:
        if not encryptor:
            error_shower('Public key unavailable')
        for file_name in os.listdir(PE_ORIGIN_PATH):
            if file_name.startswith(SOLUTION_FILE_HEADER) and file_name.endswith('.py'):
                solution_file_name = file_name
                encryPtE_for_solution(solution_file_name)
        sign_for_all_solutions()
        success_shower('all solutions have been encrypted')
    if n == 4:
        if not decryptor:
            error_shower('Private key unavailable')
        solution_file_name = get_solution_file_name()
        try:
            decryPtE_for_solution(solution_file_name)
        except:
            error_shower('Solution not exist!')
        success_shower(solution_file_name + ' has been decrypted')
    if n == 5:
        if not decryptor:
            error_shower('Private key unavailable')
        for file_name in os.listdir(PE_PATH):
            if file_name.startswith(SOLUTION_FILE_HEADER) and file_name.endswith('.py'):
                solution_file_name = file_name
                decryPtE_for_solution(solution_file_name)
        success_shower('all solutions have been decrypted')
    if n == 6:
        if not signer:
            error_shower('Private key unavailable')
        solution_file_name = get_solution_file_name()
        sign_for_single_solution(solution_file_name)
        success_shower(solution_file_name + ' has been signed')
    if n == 7:
        if not signer:
            error_shower('Private key unavailable')
        sign_for_all_solutions()
        success_shower('all solutions have been signed')
    if n == 8:
        if not verifier:
            error_shower('Public key unavailable')
        solution_file_name = get_solution_file_name()
        result = verify_for_single_solution(solution_file_name)
        if isinstance(result, str):
            error_shower(result)
        else:
            if not result:
                error_shower(solution_file_name + ' is invalid')
            success_shower(solution_file_name + ' is valid')
    if n == 9:
        if not verifier:
            error_shower('Public key unavailable')
        result = verify_for_all_solutions()
        if isinstance(result, str):
            error_shower(result)
        solution_without_signature, signature_without_solution, invalid_solution = result
        if any(result):
            need_to_show = []
            if solution_without_signature:
                need_to_show.append('Solution without signature:'.ljust(SHOW_LENGTH))
                need_to_show += solution_without_signature
            if signature_without_solution:
                need_to_show.append('Signature without solution:'.ljust(SHOW_LENGTH))
                need_to_show += signature_without_solution
            if invalid_solution:
                need_to_show.append('Invalid solution:'.ljust(SHOW_LENGTH))
                need_to_show += invalid_solution
            error_shower(need_to_show)
        success_shower('all solutions are valid')

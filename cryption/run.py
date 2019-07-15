#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from header import PE_PATH
from header import PE_ORIGIN_PATH
from header import SOLUTION_FILE_HEADER
from header import SHOW_LENGTH
from key_generator import generate
from encrypt import encryPtE_for_solution
from decrypt import decryPtE_for_solution
from sign import sign_for_single_solution
from sign import sign_for_all_solutions
from verify import verify_for_single_solution
import os


__all__ = []
__author__ = 'Yee_172'
__date__ = '2019/07/12'


def hyphen_shower(info):
    print('-' * SHOW_LENGTH)
    if isinstance(info, str):
        print(info.center(SHOW_LENGTH))
    else:
        for each_info in info:
            print(each_info.center(SHOW_LENGTH))
    print('-' * SHOW_LENGTH)


def error_shower(info):
    print('\033[31m')
    hyphen_shower(info)
    print('\033[0m')
    exit()


def success_shower(info):
    print('\033[32m')
    hyphen_shower(info)
    print('\033[0m')


def get_solution_file_name():
    n = input('Input the index of problem: ')
    try:
        n = int(n)
    except:
        error_shower('Invalid input!')
    return SOLUTION_FILE_HEADER + ('%04d' % n) + '.py'


if __name__ == '__main__':
    hyphen_shower('Welcome to CryPtionE')
    print()
    print('[1] Generate a new pair of key')
    print('[2] Encrypt single solution')
    print('[3] Encrypt all solutions')
    print('[4] Decrypt single solution')
    print('[5] Decrypt all solutions')
    print('[6] Sign single solution')
    print('[7] Sign all solutions')
    print('[8] Verify single solution')
    n = input('Input a number to choose [1 - 8]: ')
    try:
        n = int(n)
    except:
        error_shower('Invalid input!')
    if not 0 < n < 9:
        error_shower('Input not in the range!')
    if n == 1:
        generate()
        success_shower('A new pair of key created')
    if n == 2:
        solution_file_name = get_solution_file_name()
        try:
            encryPtE_for_solution(solution_file_name)
        except:
            error_shower('Solution not exist!')
        success_shower(solution_file_name[1:] + ' has been encrypted')
    if n == 3:
        for file_name in os.listdir(PE_ORIGIN_PATH):
            file_name = '/' + file_name
            if file_name.startswith(SOLUTION_FILE_HEADER) and file_name.endswith('.py'):
                solution_file_name = file_name
                encryPtE_for_solution(solution_file_name)
        success_shower('all solutions have been encrypted')
    if n == 4:
        solution_file_name = get_solution_file_name()
        try:
            decryPtE_for_solution(solution_file_name)
        except:
            error_shower('Solution not exist!')
        success_shower(solution_file_name[1:] + ' has been decrypted')
    if n == 5:
        for file_name in os.listdir(PE_PATH):
            file_name = '/' + file_name
            if file_name.startswith(SOLUTION_FILE_HEADER) and file_name.endswith('.py'):
                solution_file_name = file_name
                decryPtE_for_solution(solution_file_name)
        success_shower('all solutions have been decrypted')
    if n == 6:
        solution_file_name = get_solution_file_name()
        sign_for_single_solution(solution_file_name)
        success_shower(solution_file_name[1:] + ' has been signed')
    if n == 7:
        sign_for_all_solutions()
        success_shower('all solutions have been signed')
    if n == 8:
        solution_file_name = get_solution_file_name()
        result = verify_for_single_solution(solution_file_name)
        if isinstance(result, str):
            error_shower(result)
        else:
            if result:
                success_shower(solution_file_name[1:] + ' is valid')
            else:
                error_shower(solution_file_name[1:] + ' is invalid')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from header import RSA_CONTROL
from header import PUBLIC_KEY_PATH
from header import PRIVATE_KEY_PATH
from Crypto.PublicKey import RSA


__all__ = ['generate']
__author__ = 'Yee_172'
__date__ = '2019/07/12'


def generate():
    key = RSA.generate(RSA_CONTROL)
    with open(PUBLIC_KEY_PATH, 'wb') as f:
        f.write(key.publickey().exportKey('PEM'))

    with open(PRIVATE_KEY_PATH, 'wb') as f:
        f.write(key.exportKey('PEM'))

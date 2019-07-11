"""A library for nb.njit

This library is set for nb.njit, where nb is the short name for numba
"""

import numba as nb

@nb.njit
def pow(base, exponent, module):
    res = 1
    while exponent:
        if exponent & 1:
            res = res * base % module
        exponent >>= 1
        base = base * base % module
    return res

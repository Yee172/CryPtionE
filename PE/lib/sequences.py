"""A library of sequences

This library is set for various of sequences
"""

from linear_recursion import LinearRecursion


def Fibonacci(**kwargs):
    sequence = LinearRecursion([0, 1], modulo=kwargs.get('modulo', 0))
    if kwargs.get('get_summation', False):
        sequence.initial_values = [0, 1, 2]
        sequence.recursion = [2, 0, -1]
    else:
        sequence.recursion = [1, 1]
    return sequence


def Tribonacci(**kwargs):
    sequence = LinearRecursion([0, 0, 1], modulo=kwargs.get('modulo', 0))
    if kwargs.get('get_summation', False):
        sequence.initial_values = [0, 0, 1, 2]
        sequence.recursion = [2, 0, 0, -1]
    else:
        sequence.recursion = [1, 1, 1]
    return sequence


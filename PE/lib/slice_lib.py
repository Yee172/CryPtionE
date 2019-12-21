"""A library for slice

This library is set for slice
"""


def rearrange_slice_for_infinite_sequence(s):
    # [minimum, maximum)
    minimum = s.start
    maximum = s.stop
    step = s.step or 1
    reverse_flag = False
    if step < 0:
        reverse_flag = True
        step = -step
        if minimum is None:
            raise ArithmeticError('could not deal with an infinite sequence')
        else:
            maximum = maximum or -1
            minimum, maximum = minimum - (minimum - maximum - 1) // step * step, minimum + 1
    minimum = minimum or 0
    if maximum is None:
        raise ArithmeticError('could not deal with an infinite sequence')
    if minimum < 0 or maximum < 0:
        raise ArithmeticError('could not deal with negative index')
    return reverse_flag, minimum, maximum, step

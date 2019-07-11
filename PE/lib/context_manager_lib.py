"""A library for context manager

This library is for storing context managers
"""

import contextlib
import datetime


@contextlib.contextmanager
def timer():
    __start__ = datetime.datetime.now()
    yield
    __end__ = datetime.datetime.now()
    print('Running time: %f s' % (__end__ - __start__).total_seconds())

"""A library for decorator

This library is for storing decorators
"""

from functools import wraps

__all__ = ['memorize', 'track']


def memorize(function):
    """memory wrapper
    
    Set up a memorized function
    Notice that this operation only memorizes the args, kwargs would be ignored at memory

    Usage:
        @memorize
        def f(...):
            pass
    
    Decorators:
        wraps
    
    Arguments:
        function {function} -- function needs to be memorized
    
    Returns:
        function -- memorized function
    """
    __memory__ = dict()
    @wraps(function)
    def wrapper(*args, **kwargs):
        if args in __memory__:
            return __memory__[args]
        else:
            result = function(*args, **kwargs)
            __memory__[args] = result
            return result
    wrapper.__name__ = 'memorized_' + function.__name__
    return wrapper


def __track_print(function_name, string_parameters, __space__=0, header='', tail=''):
    print(' ' * __space__, end='')
    print(header, end=' ' if header else '')
    print('%s(%s)' % (function_name, string_parameters), end=' ' if tail else '')
    print(tail)


def track(*t_args, **t_kwargs):
    """tracking wrapper
    
    Track a function, usually a recursive one

    Usage:
        # default tracker
        @track
        def f(...):
            pass

        # tracker with user-defined indent
        @track(4)
        def f(...):
            pass
    
    Decorators:
        wraps
    
    Arguments:
        *t_args {[type]} -- [description]
        **t_kwargs {[type]} -- [description]
    
    Returns:
        function -- tracked function or tracking wrapper
    """
    __ratio__ = 4
    __get_function__ = False
    if hasattr(t_args[0], '__call__'):
        function = t_args[0]
        __get_function__ = True
    else:
        __ratio__ = t_args[0]
        assert(__ratio__ > -1)
    def __track__(function):
        """tracking wrapper
        
        Track a function, usually a recursive one
        
        Decorators:
            wraps
        
        Arguments:
            function {function} -- function needs to be tracked
        
        Returns:
            function -- tracked function
        """
        __space__ = [0]
        @wraps(function)
        def wrapper(*args, **kwargs):
            string_parameters = ', '.join(map(repr, args))
            string_kwargs = ', '.join(map(lambda x: x + ' = ' + '%r' % kwargs[x], kwargs))
            if string_kwargs:
                string_parameters += ', ' + string_kwargs
            
            __track_print(function.__name__, string_parameters, __space__[0] * __ratio__, header='Entering')
            __space__[0] += 1
            result = function(*args, **kwargs)
            __space__[0] -= 1
            __track_print(function.__name__, string_parameters, __space__[0] * __ratio__, tail='-> %r' % result)
            __track_print(function.__name__, string_parameters, __space__[0] * __ratio__, header='Leaving')
            return result
        wrapper.__name__ = 'tracked_' + function.__name__
        return wrapper
    if __get_function__:
        return __track__(function)
    return __track__

def adaptive_Simpson_integral(f, left, right, eps=1e-6):
    """integral a function from left to right with eps
    
    adaptive Simpson integral
    
    Arguments:
        f {function} -- integral function
        left {number} -- integral lower bound
        right {number} -- integral upper bound
    
    Keyword Arguments:
        eps {number} -- eps (default: {1e-6})
    
    Returns:
        number -- the result of the corresponding integral
    """

    from queue import Queue


    def Simpson_integral_formula(left, right):
        """Simpson integral formula
        
        Simpson integral formula
        
        Arguments:
            left {number} -- lower bound
            right {number} -- upper bound
        """
        middle = (left + right) / 2
        return (f(left) + 4 * f(middle) + f(right)) * (right - left) / 6


    res = 0
    q = Queue()
    # left, right, S_total, eps
    q.put((left, right, Simpson_integral_formula(left, right), eps))
    while not q.empty():
        l, r, S_total, precision = q.get()
        m = (l + r) / 2
        S_left = Simpson_integral_formula(l, m)
        S_right = Simpson_integral_formula(m, r)
        S_delta = S_left + S_right - S_total
        if abs(S_delta) <= 15 * precision:
            res += S_left + S_right + S_delta / 15
        else:
            q.put((l, m, S_left, precision / 2))
            q.put((m, r, S_right, precision / 2))
    return res

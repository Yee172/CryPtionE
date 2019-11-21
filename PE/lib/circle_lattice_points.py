from integer_operation import integer_sqrt

def circle_lattice_points(radium_square):
    """Circle lattice points counter
    
    Calculate lattice points inside circle x^{2} + y^{2} <= radium_square
        with O((1 - 1 / sqrt(2)) sqrt(radium_square)) time complexity

    see alternative methods at https://oeis.org/A057655
    
    Arguments:
        radium_square {number} -- radium square

    Returns:
        int -- number of lattice points inside the circle
    """
    lower_n = integer_sqrt(radium_square // 2)
    upper_n = integer_sqrt(radium_square)
    delta_n = upper_n - lower_n
    return (2 * lower_n + 1) ** 2 + sum(integer_sqrt(radium_square - (lower_n + k) ** 2) for k in range(1, delta_n + 1)) * 8 + 4 * delta_n

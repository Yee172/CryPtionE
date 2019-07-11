def partition_number(MAXN=10 ** 7, info=True, **kwargs):
    """Return a list of partition number with index up to MAXN
    
    Use the connection between pentagon number and partition number
    
    Arguments:
        **kwargs {[type]} -- [description]
            modulo {int} -- modulo number (default: {0})
    
    Keyword Arguments:
        MAXN {int} -- upper bound (default: {10 ** 7})
        info {bool} -- need info or not (default: {True})
    
    Returns:
        list -- a list of partition number with index up to MAXN
    """
    modulo = kwargs.get('modulo', 0)

    def pentagon_number(n):
        return 3 * n * n - n >> 1

    if info:
        print('Generating partition number...')
    
    pentagon = [0] * MAXN;
    dp_add = [False] * MAXN;
    partition_number = [0] * MAXN;
    pentagon[0] = 0
    dp_add[0] = False
    i, j, k = 1, 1, 2
    while True:
        pentagon[j] = pentagon_number(i)
        pentagon[k] = pentagon[j] + i;
        dp_add[k] = dp_add[j] = i & 1;
        if pentagon[k] > MAXN:
            break
        i += 1
        j += 2
        k += 2
    partition_number[0] = 1
    for i in range(1, MAXN):
        j = 1
        while True:
            if pentagon[j] > i:
                break
            if dp_add[j]:
                partition_number[i] += partition_number[i - pentagon[j]]
            else:
                partition_number[i] -= partition_number[i - pentagon[j]]
            if modulo:
                partition_number[i] %= modulo
            j += 1

    if info:
        print('Partition number generated successfully.')

    return partition_number

# Let y_{0}, y_{1}, y_{2}, ... be a sequence of random
# unsigned 32 bit integers.
# For the sequence xi the following recursion is given:
#    1. x_{0} = 0 and
#    2. x_{i} = x_{i - 1} | y_{i - 1}, for i > 0.
# It can be seen that eventually there will be an index
# N such that x_{i} = 2^{32} -1 for all i \geq N.
# Find the expected value of N.
# Give your answer rounded to 10 digits after the decimal point.
# ----------------------------------------------------
# Analysis: brute force
#           E = \frac{1}{2}^{32} * \sum_{i = 1}^{\infty} i * ((1 + \frac{2^{i - 1} - 1}{2^{i - 1}})^{32} - (1 + \frac{2^{i - 2} - 1}{2^{i - 2}})^{32})
#             = \sum_{i = 0}^{\infty} (1 - (1 - \frac{1}{2^{i}})^{32})

03d3e3a76bd08e2eb5c2af9f7a735d43d19d233f946e9dae5c46914585748bdbbb72211850778cdf387c8a4ee71e5e13e626
05f7a697ffc3e8bd132a92f7fc8c5604a714ecba702516ae438e92df2006945e430a03dcbef226523982ed90109a3dfbd0a5
eb676a96ce5a5cb42bec91158825faed2a6b0afae70f64b96a996c6e1cb9d03609248989b503d430e722608b913a7f8bc4d9
4b02b1009044050b205f7467e91063802908db7d271d63759ed1c5ab1bce437cc45cd78bcd474f83d8a81faf93f3fad46fe8
ab24ad74ae0c9b8cbb689176a4d9a408f6fc7093ce2f038ccc9d20f947c04cc9d661a02222bd370b8a4a165bbbe7a918def0
738a7d2cc485

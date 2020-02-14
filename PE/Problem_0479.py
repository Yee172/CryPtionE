# Let a_{k} represent the three solutions (real or complex numbers)
# to the equation \frac{1}{x} = (\frac{k}{x})^{2} (k + x^{2}) − k x.
# Let S(n) = \sum_{p = 1}^{n} \sum_{k = 1}^{n} (a_{k} + b_{k})^{p} (b_{k} + c_{k})^{p} (c_{k} + a_{k})^{p}.
# Interestingly, S(n) is always an integer.
# Find S(10^{6}) modulo 1000000007.
# ----------------------------------------------------
# Analysis: brute force
#           Hint:   (a_{k} + b_{k}) (b_{k} + c_{k}) (c_{k} + a_{k})
#                 = (a_{k} b_{k} + b_{k} c_{k} + c_{k} a_{k}) (a_{k} + b_{k} + c_{k}) - a_{k} b_{k} c_{k}
#                 = 1 - k^{2}

4ee34ba9fe1966fff0b53891b19ee8b56e2744e7e899a4acd597838e31abb0ac9432c652fe7ca8bf82bea7caa53c22bf2082
92e65c7a2e7f5f8edff3dba4b2cf8c822d37e029990afb32d312ac1410ad6b65d3e4c4010f59a028681035da615f0381f850
a7d5d560a32c7a55a7e9c935bd8a3f7c66b94f33ecdbe8b5c89909cbf0a4434d05ac71800470c6ceecf42b39be06177b7143
4e952fb76afe055471c98ff6ef9019e652546d8d1d40cd9c94cdc8372f632a3c44cf69b4d511298b3b9de1daeddf2cf7c0ce
21e3a4947e611ad3ac296cabd2e114b2bf612e77f2fe7b9db2a7aa5fc862cb3964fba614a5fb48df32582b60a9cffed5329a
42bff6b7d5c4

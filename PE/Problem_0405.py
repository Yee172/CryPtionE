# We wish to tile a rectangle whose length is twice its width.
# Let T(0) be the tiling consisting of a single rectangle.
# For n > 0, let T(n) be obtained from T(n - 1) by replacing
# all tiles in the following manner:
#     -------           -------
#    |       |         |       |
#    |       |         |-------|
#    |       |         |   |   |
#    |       |   ==>   |   |   |
#    |       |         |   |   |
#    |       |         |-------|
#    |       |         |       |
#     -------           -------
# Let f(n) be the number of points where four tiles meet in T(n).
# Find f(10^{k}) for k = 10^{18}, give your answer modulo 17^{7}.
# ----------------------------------------------------
# Analysis: brute force
#           Hint: After drawing and calculation, we can find the following linear recursion:
#                    f(n) = 6 f(n - 1) - 7 f(n - 2) - 6 f(n - 3) + 8 f(n - 4),
#                 which leads to
#                    f(n) = - \frac{1}{15} (-1)^{n} + 1 - \frac{4}{3} 2^{n} + \frac{2}{5} 4^{n}

3ff6af180755882081a88fca9bedc3c3a317dcc16ac0f2634a9f2fd3548a5f4f77df9b2f07e2350fd0cf570375ecc8111574
30212bdd0d2d89aabae353501199f5f3429d20e05848dccac9379657f66a427ab48d70bc1154c7d0bb26993dee94f21f7eb4
66e9b406dc527e94020decba61883d0cd84040b2c356a975fe7cb5af93c81e7e4234d9b8cc2be0a01041425b7c4bfc22782f
6449592003f59be7c15e8551ae716f40c02a23c1307bad6be8e5c6fbea5a1b74837668a73a71e3f738935142c41385061261
c5a61bd2daa33186b26290576cfdc80bbee370f638bcbe56c3fc42c15530a6c9fad1b951ab9c3aeda57d08403507ac0ee1d2
4a45d4cea30c7c2d2d7c9dcba349c2c7d13295850580c3a6b2e0d6f4c60b13ab300e2ec740594af083769ef85c1cae572781
f7fc07d0b4ec02ac28022f806c1ab63b158445ae8765a8992e06af9375e0fcc12ee246cf1144170ad2f340581f2e47a2bfa9
998d76e23f42766672664bf59aed55fb5e6df6f180871e57b71c610ca8bf813019e36897eb9da829f90658d190d0f23886d3
ba5e6ac4fd612d41df3142edcd5fb870dcafff410494344dc08aa19262a5cddeca7c3cf015baac53c1af3c9c25970e63ac67
357c717d43d6c0c288a79ebd17cc7856e5f921d302475dfa2070dcf6c2518a58032e098741f3edc36fbb0f0b8164ed4442a2
7dad69c054f57fb5c314c202101227657c2d2d7ca12660e2416c34900df5deaf8bbdfac2685b206973e6b2b955f3239ceea6
9bd36aefb6f98177ad106ae7e1718765b8e6dadbfedad185b5a692074c01faf22d2a9920ac5020c90690c6e7b77e90e1382e
d1fbaf2fabcefdbe5b0854d539e3133ba9f3852c4b9e12049520be6d1b69e3504029887f224b2adf7f8647876bd9a8f1ed24
826e325c34aa95bf1b288bba8562be7a9fb27779839ae2ea4a05b669f96074ef8f0c65fbf9a21f639466e3476de16d690db6
958f7bb953a0f517669a21ca831ba85a19c6446d0555a37ec9ce3eb1ea5c10b82a5a60cb889d2ba6b72bf04302950c30d72f
1d4131849e8bf1da82b87c3e46931594b1163d5304c222d440bd

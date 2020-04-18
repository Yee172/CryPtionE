# Oscar and Eric play the following game. First, they agree
# on a positive integer n, and they begin by writing its
# binary representation on a blackboard. They then take
# turns, with Oscar going first, to write a number on the
# blackboard in binary representation, such that the sum
# of all written numbers does not exceed 2 n.
# The game ends when there are no valid moves left. Oscar
# wins if the number of 1s on the blackboard is odd, and
# Eric wins if it is even.
# Let S(N) be the sum of all n \leq 2^{N} for which Eric
# can guarantee winning, assuming optimal play.
# Find S(12345678). Give your answer modulo 1000000007.
# ----------------------------------------------------
# Analysis: brute force
#           Hint: 0 |   1
#                 1 | 
#                 2 |   3   4
#                 3 |   7
#                 4 |  15  16
#                 5 |  19  20  31
#                 6 |  63  64
#                 7 |  67  68  79  80  83  84 127
#                 8 | 255 256
#                 9 | 259 260 271 272 275 276 319 320 323 324 335 336 339 340 511
#                 ...
#                 find the pattern, then you can see this is just simple dynamic programming with parity discussion,
#                 the summation of the current layer is only related to the accumulation of the previous layers,
#                 brute force the first few values to get the linear recursion

98fbcb01f8fc9d948a20c3e15f5525b26357c07c6c0610b62731f8138c2b779675fc868dc87f7da6462de6c2d43e65a30c6e
c11ae6a7e068427d701e56576ee39e65283a164bd2ad1f26f09490f9d1363b6400f883c752a765eb336dc592530c0b2106c1
239976a96757298739e5aa8779def32e4315d24db04430a206a64f474ce9a6081acec0dd18976114976aab13096a69c009ac
fec1fc2efef7e73c1bd1b7ceb0ae88e6e464cf0e970ace4c57f8e509c5d7ff6429fe1911749f33c03a1bcd556e7c2a601f38
1ddf05731ffa51e8a07b5d5a618c00dd64372e824a0f9320d435c044ef94821282512dd6d5b967194ff5606ec72990874a4a
6bab88fa85777c2d2d7c23d1c4e26f8802a99d399f90a1a79190f57b967b49efe4adbf2a0eca49771673292332d90c07986c
afc1b04a2449d47bcf4e807b5b0195cca2815df52bb2379c55bc6604f74072a3558e137c83da741294f86b31ddeed99eec1f
a47b93328a656290c21c4d757e6af44d0dcd33ab04b51d2facd2dd34d39bc06e06a82778c061a0d844a503a5b8488d0bf3e9
eac4da676e9a7365ffa3be6069d22b4643a855faf91be94f28cd9b9dc99e7a541ac1a2d23972b8fc330124f05a250fb1c76f
c1f0386f1cf0d736f066cb8a1f3f394357eee25c85d3c717a8fd6bac36ae60e4a7059f17acce6f06130a171e8bb752215eb4
43f41933dedc334f971d60599edc535e

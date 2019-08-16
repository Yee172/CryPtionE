# If (n_{1}, n_{2}, n_{3}) indicates a Nim position
# consisting of heaps of size n_{1}, n_{2} and n_{3}
# then there is a simple function X(n_{1}, n_{2}, n_{3})
# — that you may look up or attempt to deduce for yourself
# — that returns:
#    zero if, with perfect strategy, the player about to move will eventually lose; or
#    non-zero if, with perfect strategy, the player about to move will eventually win.
# For how many positive integers n \leq 2^{30} does
# X(n, 2 n, 3 n) = 0?
# ----------------------------------------------------
# Analysis: Nim game
#           We get that X(n, 2 n, 3 n) = 0 <=> n ^ (2 n) ^ (3 ^ n) = 0
#           Notice that n ^ (2 n) ^ (3 ^ n) = 0 iff there are at least one 0 between every two 1's the binary form of n
#           Then we could find that
#              for n \in [2^{k}, 2^{k + 1}), the number of n satisfies X(n, 2 n, 3 n) = 0
#              follows the Fibonacci sequence corresponding to k
#                 Hint: think this question from the perspective of dynamic programming

c07a21d50978d1d59d38e97d35f30ef70556cfcf2afb1f6b137e64ce4cb19eccc6d00a49b0a4083471597e33a8dc24550a71
1c47f030e89cc554610259fce80a44b8a4f068722aa054da7489ae471a24c1da73c5156a9e808dc215ffc2e851d4d41bed91
1b1b938ab64df70df95223e71180358f05b7ee8d7da2c6b7860757e61ac9c68fc596e13517efce10ba03a7b7b802e84c6618
665950bcd4a346aa1286318935aa23c7783a37cb8b851477d98bf7bf8b112ef0810ceeb8f1ea26de9acab3c32cf24a61fe63
0f670e27d3fe0ad9209ecef7da7ab2bfd68166f387f1d7614e963c977d97ed3f86e793ab0897d66bb5ecac6c245e34373a20
8a0a81e7ee81

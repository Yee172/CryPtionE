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

22cc0ba57f4ad40f1e1ffe2c0b2e947e3a9edd427817cebb8b6c9cf11a51b8151894188cfd0705cb5fb72118891cf99d8aba
76219c9dba9cfec20760c1033c23d85cdcb3f28a3796cf4f53a093545fd2809bc56c502dcbc8647914415e1f4f1dc364c11f
3f2f6e5747a682a8aee0ed5a04dfd89da9946cb02e352aa2e5bf6629859aef83c7692b714ae52e8f6f5c481aca8a732acfa5
7eae2c91f0a69c95b3c0cec3c4cf699a6dfb5125a65cc36411c2b0fc0b13a4766990e14cd10779399a2b0895b86ac1c6863f
759aa5b737a121cceb97c0dd2403fa72f3421f8ec893f66fd177abdc9be9802fb9d2261adc2f925e36a9705471c473f63ce9
355ca126c35f

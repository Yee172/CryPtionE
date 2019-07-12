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

b5860969c4d86f2fa3839ff5140bf9bc157a2f6bfe4f10feeed10b8a1d0f34bfd12a715340202b575ef1e5380f28a83ceac8c09033858e1ef81a12132a5d33bbb9806b938fad9fcbeb4b69148ef8106237da1be67a338ef4eaaf7785948af93ffa75d7928f9e6004a660a9c247609ef2cec9abbf4dc7a62655786e850a4ee700c8a3a49ed0746a581c4416f1fda07abe74b38abdefeb25ad6671254e04349a27b8ebe93beb54fc788c81b84df5d0b6b39c0b29deb453efdb0cac70e222fd3b12ac2d14da5dd5e526c87fcd529b34754cd8505a41df9b03f9f20dd72bc0b35b07a65f7840e1fdf0f12e3c54640176e21861bea29379b7349627f7c3433d049446

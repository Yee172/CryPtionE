# Using only a six-sided fair dice and a five-sided fair
# dice, we would like to emulate an n-sided fair dice.
# For example, one way to emulate a 28-sided dice is to
# follow this procedure:
#     1. Roll both dice, obtaining integers 1 \leq p \leq 6
#        and 1 \leq q \leq 5.
#     2. Combine them using r = 5(p - 1) + q to obtain an
#        integer 1 \leq r \leq 30.
#     3. If r \leq 28, return the value r and stop.
#     4. Otherwise (r being 29 or 30), roll both dice again,
#        obtaining integers 1 \leq s \leq 6 and 1 \leq t \leq 5.
#     5. Compute u = 30(r - 29) + 5(s - 1) + t to obtain an
#        integer 1 \leq u \leq 60.
#     6. If u > 4, return the value ((u - 5) mod 28) + 1 and stop.
#     7. Otherwise (with 1 \leq u \leq 4), roll the six-sided dice
#        twice, obtaining integers 1 \leq v \leq 6 and 1 \leq w \leq 6.
#     8. Compute x = 36(u - 1) + 6(v - 1) + w to obtain an
#        integer 1 \leq x \leq 144.
#     9. If x > 4, return the value ((x - 5) mod 28) + 1 and stop.
#    10. Otherwise (with 1 \leq x \leq 4), assign u := x and
#        go back to step 7.
# The expected number of dice rolls in following this
# procedure is 2.142476 (rounded to 6 decimal places).
# Note that rolling both dice at the same time is still
# counted as two dice rolls.
# There exist other more complex procedures for emulating
# a 28-sided dice that entail a smaller average number
# of dice rolls. However, the above procedure has the
# attractive property that the sequence of dice rolled
# is predetermined: regardless of the outcome, it follows
# (D5, D6, D5, D6, D6, D6, D6, \ldots), truncated wherever
# the process stops. In fact, amongst procedures for n = 28
# with this restriction, this one is optimal in the sense
# of minimising the expected number of rolls needed.
# Different values of n will in general use different
# predetermined sequences. For example, for n = 8, the
# sequence (D5, D5, D5, \ldots) gives an optimal procedure.
# Define R(n) to be the expected number of dice rolls for
# an optimal procedure for emulating an n-sided dice using
# only a five-sided and a six-sided dice, considering
# only those procedures where the sequence of dice rolled
# is predetermined.
# Let S(n) = \sum_{k = 2}^{n} R(k).
# Find S(1000). Give your answer rounded to 6 decimal
# places.
# ----------------------------------------------------
# Analysis: brute force

792998a3e1841cb88d6932593d5f23b4b0d4c17e1a01a648c9676e7ae65b129107bb3db7c84521c8fe6761c1e5b4780a2825
aec794916e988b6b8cd09064327b6c93ebbc93cffc458c32fd409d58b70ec6c4a1ef9739467fcd1483d8f1a20ef4eb61349c
72e049980346024e6ea1b9d21f4e4816eb00fe2a0c9959fe1e45b28075777f034b728ed272644ee2de5e5ad78889c0322d5f
db9c299474877373881570608ed25036dc9565eb4a48c8fe175d2c5b329ad3cd530e381245635921acacb2029b1a3b4022d1
c4a24300a76520dd1c076d3feae9dd2b11e4db3e4b3c61a5fce6c9b7cef0824347a26b588f2dc73b71e6fe78d00379db4a6b
8a453961914b7c2d2d7c38ed01cc6f67ccafcc1289594f483fce8c9df59efbda9204b471eb6f54431f4e04a2fa63bdec3adf
ceb3754f107e33b6ad2261d69d14bab1b67e24d12529e7acb13e0bea346dcfcf3945cf57b8de3e015b43460de14ec9ca4c40
bdc2684bf84c4a5c12da6b12225737fb25bde34b5a6fc15fe9a89199b1b169557c68320a45dd86ab33a563eb46a2c47dbde5
8758f927e86af47a0dfa12d65737fcd9bba4b6a55fc2dd8b033170bd94b62616dff9fac62114323c477470bc6332ca52d47a
91890f21f009e68105ef740a05ef8c98cc0edbe0c686ea4ffb7607d1ceb09daddfb4437672893555d3a7aa1228065b9d2e7e
363a8f806b62c5a8c2d6e190cbc6db217c2d2d7c768c5256329486a76cea1caa3bcabd533c68c656acc511cd51896f2cecfd
711421d64677a0c3c5058cc1703eb3d5c059b44d425ffc59a6ce5a25e12a6ee44d317110fdfb4ee9422e72dcd40072db0847
e7d4cac5976c19c5d174353e4a508a69c02a65aa868005ef263f7ad8b6bea2724c3a2a857bc56e5d1a4e19123b90f18198a6
c3190395a290be6ded5b1f3868feb9cc5ed4e5ac2446b12c15f61036425cecf9764e6db6c83d3d665cccff3e86978945bd1f
4efd319bf151ef4e46527a8ac721edd402a1c52308ce86701eb6ce1523e08b6a72f705c5047cdc455ebda084624d231ef013
ef20081773998b514231da1cc144665c7780134c551ba0a0a01b7c2d2d7c8d2e06357339603247f21f32df95d3be952aeb08
bbc6a51d0fd7ed8e8aded2e4d35a63a61ce7e148deff0d593f2d58e27208582b715197e8bf0a665d6b9aebf2cd014f38c5b4
92435baa1ce5e1fa27fb700c54f87be0dd69c0d7ed394fc94384622a10fadb508b606af2cf94c760da6971b47f73d789214d
b065b1c15d882d960e48e2dad1ee53e1eca75e21e4983915c29bb4aee59f24e85bf61879343c2b7de06c68946fb5b9aa6e7d
78d43b46b1bd6a98785e988cb54db8a03fbc7682d5aee3b611d8c43586eea1991350f6d4c0400d73072fa654b7d44bd9514b
a0f9cda21fa10f38e7f95adc2cd457955650e2c39befa19e477497f9310400faf2c9b740

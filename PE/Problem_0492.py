# Define the sequence a_{1}, a_{2}, a_{3}, ... as:
#    a_{1} = 1,
#    a_{n + 1} = 6 a_{n}^{2} + 10 a_{n} + 3 for n \geq 1
# Define B(x, y, n) as \sum (a_{n} mod p) for every prime
# p such that x \leq p \leq x + y.
# Find B(10^{9}, 10^{7}, 10^{15}).
# ----------------------------------------------------
# Analysis: linear recursion
#           Let b_{n} = 6 a_{n} + 5, then we get that
#              b_{1} = 11,
#              b_{n + 1} = b_{n}^{2} - 2 for n \geq 1
#           Let P_{n} = x^{n} + (frac{1}{x})^{n} for some postive x with P_{1} = b_{1},
#           it is easy to see that
#              P_{0} = 2,
#              P_{n + 1} = P_{1} P_{n} - P_{n - 1} = 11 P_{n} - P_{n - 1} for n \geq 1
#           and most importantly, we can get that
#              P_{2^{n}} = P_{2^{n - 1}}^{2} - 2
#           Thus, b_{n} = P_{2^{n - 1}}
#           Also, from the perspective of matrix multiplication, we can see that
#              sequence {P_{n} mod modulo} has a loop with length at most (modulo + 1)(modulo - 1)
#           Therefore, b_{n} mod modulo = P_{2^{n - 1} mod (modulo + 1)(modulo - 1)} mod modulo
#           Then, a_{n} mod modulo = (b_{n} - 5) / 6 mod modulo

75e7457592fca2be70acd32a1e26852f9565d99966dbce18bad8a79fa983b7fc22e9bb0d1bb0d0cc7cb77544cbc86611b932
1b23d0d5c79ccb197889aaa76df9b4b773da7ee9e1ebb2f9ac9a855798769f1d3c384803ea124212ec3b70bd58619279da71
f50d38f6a6f3be869dbd4d18bce60c96c06950f8c5cd1a41e6ae24affe88d7b2a43e1c4ca42fca5c6cfad55f913e73218690
0b02e69fcbc8b40860c0f145aa30d1f00cc915822818f10417cd190681b305bbc7049505ca3fb89dcce9581a64cc9b0d3ebd
67f12faed3e35a8f3a63f35ce6ae9ec5348e4ae0738fcdc937d445145b4f3cf6406acaa0b1f794a36a8cc854e4d4f821a937
b7feb8ee00b97c2d2d7c626fd234d8f13e431e1e12edf62d1795e7e1231683475ce218a22e6b6b27c19b979c34fb4f75086e
b4170ff3559b9049acdb9960cee35569f828ea6aedaf47ce16d79dae8759c0b35f92f95d46334d8d5a9d8db7b7bf8e97f52c
42ea50c51064b706e812dc571505ac99f07382f13992a479c9e606ac898ce794d06f29dad468e86ffef72743e55a05f57c01
ed70a6bd077f9ea4b4b398077718ee64a73eafc6e7d45c8d83a55d319e3f76817fe1018b43ebac21ead5bcf5c047118281dd
5a7089bc369213f6f0e6eeae7f0a92336ae4e4b4ca3f897ce99074681b7498eb8acdafdf9d6d8f51b65fa1e3e937587fbcc8
1b5d6dba62c4c8f312187bff208788b07c2d2d7cc0fe8bd2364ec0d5328248d10f17aff1776b077047d3632547c9c79d63c7
8e4b4084d539fec34a3bf95c615088c0ced52e2f7d944840536463010ce5365133ff3438b2036d36a4436c0328127c640f2b
4ed2db20a128ab27c1c72ab0c50cd436864ffa6df0175b04e6bdb9d2b44a4800476d3bc4d08879984c18b9ca73be0bbaa1b1
9c5ae89f057ed4c3f1f8714634291e2ac4ee3dcabe95c3f2044dfde7e844c1e0924a3ce6ceb65468c583077822ca75695df4
679fe167f53d205475b72f280a37a84aab4cef0edfa0de9591797cf2b1158a0b56a2d874a031f5d722779d80554472f80056
050ddd3817d930c58faa7dbeab766491aba342e011fda4f11995

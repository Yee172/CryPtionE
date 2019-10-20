# We want to tile a board of length n and height 1 completely,
# with either 1 x 2 blocks or 1 x 1 blocks with a single
# decimal digit on top.
# Let T(n) be the number of ways to tile a board of length
# n as described above.
# For example, T(1) = 10 and T(2) = 101.
# Let S(L) be the triple sum \sum_{a, b, c} gcd(T(c^{a}), T(c^{b}))
# for 1 \leq a, b, c \leq L.
# Find S(2000) mod 987898789.
# ----------------------------------------------------
# Analysis: matrix multiplication / linear recursion
#           Hint: gcd(T(n), T(m)) = T(gcd(n + 1, m + 1) - 1)
#                 i.e denote U(n) = T(n - 1), then gcd(U(n), U(m)) = U(gcd(n, m))
#                 In this problem, we have
#                 gcd(T(c^{a}), T(c^{b})) = T(gcd(c^{a} + 1, c^{b} + 1) - 1)
#                 Let d = gcd(a, b), then
#                 gcd(c^{a} + 1, c^{b} + 1) = c^{d} + 1, if a / d and b / d are both odd
#                                           = c % 2 + 1, otherwise
#              => gcd(T(c^{a}), T(c^{b})) = T(c^{d}), if a / d and b / d are both odd
#                                         = T(c % 2), otherwise
#                 Therefore, using matrix multiplication or linear recursion to calculate \sum_{i = 1}^{L} T(i^{d}) for each d to get S(L)

3246ec139604dc9cb112f9ad3191799f1fed31046106e29d97efe5ad4eb9123607998293a8b4f2b953d9e486d882a6ea2cf1
5113b98e8bd9e438962071fd674b2e76003ada574085680ced0566cd1646e16d36a837a2762eb44a29a45f8ca989a532d585
2afe33cbd011b16c2950658d79ae563d524813b4c6c41a502354a3f1c435fbe96153cebc65ddb84378f23eb6c4950ab99875
c748649d7ee8b3ab7a67e65e946fe0c1d5ccf246d74d4b689389e5efc18b0ca9ffdd42686aea8efdfbc19d318924d359131d
4c7e16e167ebc0995c9a3e391c6a9449722b19ddeaf64c765decbe5606f4675e309fcbfb00c9d474ecccb95cb7e2657db911
98769ea596e57c2d2d7cb11a1112330204011c1e6b4d0254d3d95bc54c370f7deed3f48c02a3957cc2713e7f167db5b9a5ca
c279744ec1f8e9d1ccf1de08abc64ab196f11e66e0d8c4b4c0f0fc6122d0f495a8c0a2532d4957d32f890ea04f23d126a3fd
fbcbe87025c5ce9ded3f41e601c8eac60e7008c5fa660dd76d6e99afc4fc15d04e708f5cfc76bb27748b850dc0113ada38a5
c2660403e91de91e567a442696d04fde0fc7814505541fe2b18ec8577c4b2b3624d60f9caedd74a3eb7e7b836c2b84546842
de4ec84995df79bc062e5ed407d30be0701ab0077a79d6fa9604a6771146714040598c4600467e73dc73d1553a00d7404d53
8559914904bd91e23ddab053a54bf5457c2d2d7c04a761a237ed3c568c3f84c06d094fc39baa28e58f06a484a3f1175d09f5
70e36e42032e1e2d9cdcfeae39528abf8e019c86934a4670ecfb3be77f49d17f3a652e8f9214ceeb65c1a21ad3c842019f73
de7a460e78a284c7be8f7efa6399ce3d2902e4246a709d3018a9e7c9cae78d6a864c4c44c33884af1bce2c33d2f61eae8598
56c463e4ad0e25674ab06e2358eb7121d28dd199c924e8232c41680a0d63ef6e0558f2c9d84a91ed4ccd9b79126e0aeb3774
1b8c1a938d6129722d757835486ac4ad5b837cfaee59b562e461be9d1461e16a5674139877b029b0abbc100e1c3ada4f9e5b
8fa0462e95cce6ca5681fb702df8b4af11c270e91b807a59a6987c2d2d7c6b591fd9e65bae18b2277b03774b591f6569c5d7
b7b7f349c8f17d9f89617950bcb57ff199df4d19ca0e836b80a29f965c1b8c22f409d0de3e1868c2783f1386ed27b7ec2da8
51aac8a12e6e950f61c3c8a33d2dac214f8cc7afd2188bdf6dcd9a47b010c729e3ae261d1c1ba08a34329e9e6f75643becea
ada07ee055910eb1e9b9d34c5c2a3bbc1ba9406564679dbcf8e20de378bd004e9a479db10fa4cd8ad05f5359bbc9bd125518
96da1ce7072b9e1d5c1719097c1aeafc3d11a096812370c4fd8ecfdd8de0cf188af797503a02848981492c71561b585e883b
f45e82308b7b53f6a168ecb636539c221f42956f8918d74eeb9aa59679384907caddb8107c2d2d7c2d627c1b97d603cd18b6
3954711e6af5948fbb27763a9a39f2e4f2756765b806d76f3357b0f7e897b922f84da82e1d29306a4ee216b664843fc9cd94
6bd15ad1dc7fc70a1c4594c032e21ce3857535a05f4430462de464805296537ce24174a33446e8f0eeaec8b51ae5fdfc0409
99da4c3cf05dbb97083065b89add5f1ff0f20e7734c8f18f738dd61a7ca0bc1f607f5175e5cabfcab0c99897b3ca61c5998d
ef6147070c1541e5bbb05ea6f54de5791e5e85d4b2013fc234046b5bb00850a72ce9ed5ea352de03789347d9ccfa7f6cca0e
dab44333a29097fb863057258e7bc03b04900c99477c81bfd47a18a3fce105fefe568577e9683d7b9227abcd920b

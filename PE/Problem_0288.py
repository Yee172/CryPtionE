# For any prime p the number N(p, q) is defined by
# N(p, q) = \sum_{n = 0}^{q} T_{n} * p^{n} with T_{n}
# generated by the following random number generator:
#    S_{0} = 290797
#    S_{n + 1} = S_{n}^{2} mod 50515093
#    T_{n} = S_{n} mod p
# Let Nfac(p, q) be the factorial of N(p, q).
# Let NF(p, q) be the number of factors p in Nfac(p, q).
# Find NF(61, 10^{7}) mod 61^{10}.
# ----------------------------------------------------
# Analysis: brute force
#           Hint: NF(p, q) = T_{1} * 1 + T_{2} * (1 + p) + ...

00decff9d7f5db092dc554b7116f71df9ddfc7f7449649e05e4cd1323d4cf75fd6f172069b10b7e06707840c9b1044c90d73
082d52ae7a65f9f768ae7303fd904728e9894b5e3ffd8034e2e94cd37fa1f1e050df7d335b8cb6d548454dd8b983d202944a
14a76651f1c9103c8639e49448dda33c9a66d7b61e4440a237119eb5b10c3a96772de3ead5f3fda1a5062af4c0898ced28a9
9d0e37e31da421dd7f69dd9f5013ae86173ff9a567074a1c2a16d731e3ed3acc1815e9083cbb6743aa8cc0b43a130006d43c
cb58d9fecbc78d984c395c86a87f7ae093ea6d0e847f852ae7d4f6503174f2bf1fa46552a2d11ad4d462a286d0ebeefd37e5
a46232d2b8e67c2d2d7c19a83d73b49a07917edd12c3030fabe4e121030c60054024948cf6c212c7d693a18e3372de0fd479
404498231d3aa34c1ab0cc8788f40eed8e647365daeeaee457a96dc735b44508468fae45886d84f3c6bbba0461c52ecc47c3
e4556e23edfe2965c21e06e49f10a423e1b32e32406cc2bd3225f784a15d923950b5683af7a4958bc3cc1b3dd84a5cebd72b
36935f4131e7344e298b54e6ad2c5e9cb221b2b553aa164ad15bb337d65223e1feffd6b060f3bb5fc8f84e93f37dc276d3d7
b898fa717ccab0cf992eee763d5d750c8ef11423479cdc1ffd36e14ece816fa608767254133b481af2521c2360856df3a03f
a445db7a4ca22a29768a3629db85863b7c2d2d7c45240a7e2f5c3517b1fc76297d19b4ee69b35e92d73566972a53bed2d177
6f41903148d1717532177f0da8007256662a19b5e9a847e9264ae2c645b17112c663fb8b9accdf701d7b5b216dfc779aebd0
30849d74e65360833733ac91ca336e3199a7e336aa7076eb174eb0a1aaafcca1552aedc37d513ca5ac1c02d36a62eb4a6a37
17ecd6988968bdd376ad3defbc59d8bfe2b230cb9832bbfc8462b9f5650e4e26d8f8f6ce8e6f7be24c3c4709968c658cc310
5893eb04d6a6cc5578a91996d1eaace57b10b4cce6df56b4ab4c8d6d9b5a1d809ba565ca710aaa6dd23b4c7265119aba1215
c6b940750e9b9ba66419fd29cde707425fba366d611a557b4653

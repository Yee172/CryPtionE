# Let d(p, n, 0) be the multiplicative inverse of n modulo
# prime p, defined as n \times d(p, n, 0) = 1 mod p.
# Let d(p, n, k) = \sum_{i = 1}^{n} d(p, i, k − 1) for k \geq 1.
# Let D(a, b, k) = \sum (d(p, p - 1, k) mod p) for all
# primes a \leq p < a + b.
# Find D(10^{9}, 10^{5}, 10^{5}).
# ----------------------------------------------------
# Analysis: brute force
#           Hint: d(p, p - 1, k) % p = (\sum_{i = 1}^{p - 1} \binom{p + k - 2 - i}{k - 1} i^{-1}) % p
#                                    = (\sum_{i = 1}^{p - 1} - \binom{p + k - 2 - i}{k - 2} (k - 1)^{-1}) % p
#                                    = (- (k - 1)^{-1} \sum_{j = 1}^{p - 1} \binom{j + k - 2}{k - 2}) % p
#                                    = (- (k - 1)^{-1} (\binom{p + k - 2}{k - 1} - 1)) % p
#                                    = 0               , if k % p = 1
#                                      (k - 1)^{-1} % p, otherwise

9f923f3c12407e040b91cbe2fdf0c024a437f12ecacd39d7c643f810423b74048b0435e10befb3aab151e5497164f1e87500
d231aecb32d07cf85680531c376462e8b1543b0f7c879ad5ac360d9bc526b2a975b1d5e47149899ece94a06de9771833d5c3
5b5230df312d4d20cc6532bff076a63897afddfbc595133c6356576f9563ede666ef14912887460a32bb4b9ae0dd7c5c9c36
05a4d39f7b802df92b3ca4b44e6da78388a47d5b7981d7f35454a10d74306a600606ea12e7fe6ae016eda8d06a6534a6d0b8
6aecf979be44318df90f8845abfcd1750cc4185a5bdf8c33f2845aeea73dd14f4574d4e083f7f2265ac4fdddfaa643122821
4c1c02b69ec67c2d2d7c1fd5d22b945e11e26419789b5fcadba44d0acdff492c80c31ad00c860ca2d3354da5ec4dbd8ae734
b10fe8392e3c5b62c338beed34681cb44b8b5fa642491acf02ca0f1b3e4e940a31aba6505b076ec46675a13de95cabf46134
55f7e315e6a6b5652fe7c14bda365782f33d7f8aa1c8a135eb0113868a7a7b9c72a8ee84bcbd3d3e07d3c7eeb338d5e55cd7
b98cdbdc0ad2a416b5da698f6f4a070d04710de67739b464b03f45b07e8941d8625efd5f9c288bf4af526bfda28ad31ac49b
64e903c5f2c3c3ab7915d0976879c594b9f2e80290a3d027881f384651e161b3dfadf2e9447ef67577b05c775152f4db20e8
ffd0af3d73f2fdad6d559efee4c4aaeb

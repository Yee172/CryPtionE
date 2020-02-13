# Let A_{n} be the smallest positive integer satisfying
# A_{n} mod p_{i} = i for all 1 \leq i \leq n, where p_{i}
# is the i-th prime.
# Let S(n) be the sum of all primes up to n that divide
# at least one element in the sequence A.
# For example, S(50) = 69 = 5 + 23 + 41, since 5 divides
# A_{2} = 5, 23 divides A_{3} = 23 and 41 divides
# A_{10} = 5765999453. No other prime number up to 50
# divides an element in A.
# Find S(300000).
# ----------------------------------------------------
# Analysis: brute force
#           Hint: A_{n + 1} = A_{n} + k_{n} q_{n}
#                 ,where q_{n} = \prod_{i}^{n} p_{i}, k_{n} = (n + 1 - A_{n}) q_{n}^{-1} % p_{n + 1}
#                 According to the previous formula, we can get every A_{i} % p_{j}, j < i (q_{j} % p_{n} == 0 for j \geq n)

7d5d873f438f9027ce722438c940a474c03da6eb05bcfca6206ac16631d65a6c71b1c4926cb0bcede1262af17217a03698bd
d098bf77573a35c5687cc149aee2bb8a9f207cd88835f03b63f47c216af3865b85ab9eefb7fa631ba0b9f4adccec655df9e3
3f6d7f14451f3ab4561e097f2b57048ddb0883e9a1af5ccbcbdf635e81ed4ae25f7e3ca938a541ae8c2b7c3d29abcb998954
b864979b282fe1c6bd7a1781a1858e1c861a0395ed805ca865215decf732ae414138110f9172ebe11b875c854aeef9c8d6ed
f4a21f1eb98e7b5262fe994deb9bb7d9af949fd87779485960365b2ee0cff5a35ebcb19e150feb35a334c8d4aec7fb9ac1dd
45258a863f9b7c2d2d7c0d530c40e2b62e52b5a2e74019faf15bbe97b6316e0ac0b4efbd6ac85f5872d7e7826e8a03671f02
187077312ecec32688d1c3ea10c53a368f90a127d669e55b828f01cd13758810ad94f4035b8306bd72f08c9df40f1abe53d9
f23f48732db18a18e4455d081a9613143f4644ce47cafa370b3540cffe79a5ac87de3272d45ec94c6e274df03c12caef3529
7e19655f3504dac71779c6f0bb8a59d805bb56150e5df01635049c357889085a11694caaec1c0485d77ea1d38cbcca7781aa
a9030293c5c5eff09c96118dce07576dc3c3aff523d4c8c31700b638f49200da5d3241979ba280493294db2259d7038a9aed
a0aaad69a1a9191f727e7a077b2226e77c2d2d7c59527be33a3ad29862ded4c2b440c0effe8e8491a4299f816878a9dbc7eb
c78ab79261c6a72bdc1658b0f8de4923a6f7542a3b9091b8ae18c418579baf00e299697dfe91c68629ac058ae71a180efab5
025da5302917a3c5a391ce488b0e4d67ff060741e301678121f84074b008816f54894a3af8fe91a31b75cb37e9fdce649bc2
25ed9dd404807ec4aa73ba01990c2e9170627d387a520d26cd4d7e825f5a81f6e69b1488c0eaf757b400ee03095e95598130
df87ec437314b7d4e357091dce40f75fa15d270c585b2c1bafbe4dacdfaf31afae6ceb4dfcd53c415238d6432cbe00cce637
a8b084feffe43b74c0cd2ef98b41b2c546f4c2f5e5c2e9f22cc9

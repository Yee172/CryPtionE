# We stack n plates into k non-empty piles where each
# pile is a different size. Define f(n, k) to be the
# maximum number of plates possible in the smallest pile.
# For example when n = 10 and k = 3 the piles 2, 3, 5 is
# the best that can be done and so f(10, 3) = 2. It is
# impossible to divide 10 into 5 non-empty piles and
# hence f(10, 5) = 0.
# Define F(n) to be the sum of f(n, k) for all possible
# pile sizes k \geq 1.
# Further define S(N) = \sum_{n = 1}^{N} F(n).
# Find S(10^{16}) giving your answer modulo 1000000007.
# ----------------------------------------------------
# Analysis: brute force
#           Hint: f(n, k) + (f(n, k) + 1) + ... + (f(n, k) + k - 1) \leq n
#              => f(n, k) = \left \lfloor \frac{n - k * (k - 1) / 2}{k} \right \rfloor
#                 S(N) = \sum_{k} \sum_{k * (k - 1) / 2 \leq n \leq N} f(n, k)

69470befa463f4cf8940c9d5f4f1d0c8fc3d1d3092cae6457fc0575090518c001132ea091f932cf9789e587e29229ee0b4b7
b5330f452a94816b11fd9752a6972bb25b1ac43b63b13b7c6eea4b3cff042d97c703ce260d33117f6f414eef943367d96a55
10feb19e914b44f787596355c1dfb616f761e0c01592180dbf98464b57026c4fceb8f43de799aa1eeaa3c1d711b779569dd6
c367bf4d1e85ef79a488eedde1ec9d9f1bc76ddc5857ac6e3b70eb6bc168babde6207eb422c6b7cb10fb98ea55597579df5b
566fd87de1f02e23948a0ab0c98e4a0b77a2e4228ba0b260c0326687cf81796996f976f3ff3022b0b7655d8f84bb13b7c3e1
0b639c91c9247c2d2d7c1759dd8e62890d0a1dcb13351cfd7f502aa8b35b1c417489aa9e89815692c4b702fa3a49e4968747
ceecc44d74e98de21e48999bf577a1e5e8eae54c1a92b024599eadf0a4431f4e27c02d4a13d6019d0b225fa26531495513ae
86ebe47121e3b8e64d76112f27f1c66031b96353ca58f664ba7c594594d900cd203a414a633ac44ca0d478f9a224a9958d7e
9739d8a53bed94e4849a11fb5145fd18338330ba0fe9e5b306688f2788f67912ed5eb3d68e4d991b6ece19aebcf6ef1f1f27
4770cce1307680f67cef3755cebf0917b00ae70a618a3916d210740c41c03c88cac1b481dd24586aa11d532faba0183fdf44
918bcb4e5fb9a347a5731db0324adf24

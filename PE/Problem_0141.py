# A positive integer, n, is divided by d and the quotient
# and remainder are q and r respectively. In addition d,
# q, and r are consecutive positive integer terms in a
# geometric sequence, but not necessarily in that order.
# For example, 58 divided by 6 has quotient 9 and remainder 4.
# It can also be seen that 4, 6, 9 are consecutive terms
# in a geometric sequence (common ratio 3 / 2).
# We will call such numbers, n, progressive.
# Some progressive numbers, happen to also be perfect squares.
# Find the sum of all progressive perfect squares below
# one trillion (10^{12}).
# ----------------------------------------------------
# Analysis: brute force
#           Hint: n = d * q + r, with r < d
#                 Notice that d, q, r form a geometric sequence,
#                 any two of them can not be equal, otherwise all will be the same
#                 1. q < r < d => q * d = r^{2} => n = r^{2} + r can not be a perfect square
#                 2. r < q < d => r * d = q^{2} => n = \frac{q^{3}}{r} + r with r < q
#                 3. r < d < q => r * q = d^{2} => n = \frac{d^{3}}{r} + r with r < q
#                 We only need to find the pair of (q, r) such that
#                 \frac{q^{3}}{r} + r is a perfect square with r < q and n % q == r
#                 Therefore, for each r = \prod_{i = 1}^{m} p_{i}^{e_{i}}, we have
#                                     q = k \prod_{i = 1}^{m} p_{i}^{(e_{i} - 1) // 2 + 1},
#                            where k is big enough to get q > r
#                 Since n > r^{2} + r, just enumerate r from 1 is acceptable

c5746ad862d248f27dafb9d350a38459da435065f4bda1e4619c54a4b59b7e9daf1446b5bc3fe0a9dc914b65562221bded2c
6610eaa98eae8445e02fc1b76d8bb47b43166df8c1e4b8fd7937ca8bc8f62e715694c2db55608dfbad22b932a263dc109106
bd554a1262c2463ed58adabc15662b0ad5604cd44bde80d8fd3b5e807a49542e0ee0e0b6c51773e1c6e88b36add8105f8fd4
de6a6a25f6fc1f42aac7b39c9064b9dee133a8fd4ba9437807e5c390dff9b2de86fce3d17efb59e67870798b196c363026b7
5ca286e998d93092a00c77558fdecda69485a9d32d36550943a285726f01a25fa184df5d685c6675e4e9da336fc74eeef5d4
87c04dc682897c2d2d7ca4245250b6dd183900e6f237309ba108df82d40e806e823594abc83e06a9b0c38e0a4208b4c4cd10
6852aa40bfd7ccff97a913a76247c64f85911607eccd939ee23472abde6b8a9315e717e591d15405d63aa5095b48928fae30
7710b44576b64135cd63a5e102329ce982dfddf3581e3d2b6caf7fbae07aeffa52b3d2d52031bca502437357d65fb39dbda5
bfcd9aee9a64d2f06f15c4173ba567c3e2b856e4ef8ba3439c92bc1c82b211b4c19042beb5c0d30f259fad840af9e1268986
0ac81653b15a2170c3f9522d8136c6049cc3e3dddfecbab064b44e705e9cee1bb65c28958c2a8374d24713c5ba62dc81ff04
4af6a172cf2f1ac6ba99e0871d44bfd27c2d2d7c8b453cafd5fbc20e697fe6ecdd999b1dce522c2539c700338066649dd485
ca21cdd1eab29d244d18e4741ac0270d9063b75cd77405f6fceb20ecfd2069b991287a90906364a0d02c30402921122b0447
497f9aa5d7cc9795e2dcdfbabd1bb2ba86e3161ca6b441006474b700485b3dd4cc9aaec5cf0942230e55d2c16af3014692e5
52df03a177a375be856677f6aa116900b1a993a52324b10383e8677b642bbaa1a993e2fcc1395976c3b4866dbd69d9ff62f1
ab01748d8f2ad3d4562c614c2fad30f5db9d6284125d56b8821b4ebadfadb00610ec57bba2d6474817b49f9f65c301af22b7
2ae0ad699da8eeb789e0f68739754dec5f50468f6153f156f2477c2d2d7c729a6275f65eb1aad2282d190cbe813ff3ae26d2
b378c45dabed6f6ef00a445315253e33d9ea0fcbd6a73f235f765c8d83d692e92b51c015fc245a65cb4bf1f2028ff8d5c938
386aeca1f3b29075dedc57f5bc9a14b7277e89039e4703c0ae0a089f7b29b0a1b55ce5ab97588739817537a6fb7b5f890359
2bfe0331d3e086b33a984faa92740d268d48b16ebd061edc3bd9e178352f275d0df67bf3202f5fa235115d262cae9c44974b
f573a0a86561c95d1612e1600cf3a9b16a965ac09df426e4cb7d7ca83ebe006f12ceecd9235eb792ca456fc7e7eee8a0ed08
7e870680cb42ac9ed9f49916a9dd1a933a69832d097c36536566b722bdf0e57eca27a1f7

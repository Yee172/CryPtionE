# Let T(n) be the number of tours over a 4 * n playing
# board such that:
#    The tour starts in the top left corner.
#    The tour consists of moves that are up, down, left, or right one square.
#    The tour visits each square exactly once.
#    The tour ends in the bottom left corner.
# What is T(10^{12}) modulo 10^{8}?
# ----------------------------------------------------
# Analysis: matrix multiplication
#           Hint: only consider the last column of each 4 * n board
#                 1. --  2. --  3. --- 4. --        5.
#                      |      |             |
#                    --       |    --     --  or       --
#                             |      |                   |
#                    --       |    --            --    --
#                      |      |                    |
#                    --     --     ---           --
#                 The corresponding state transfer matrix is
#                 1 1 0 0 0  state 1
#                 0 0 1 1 1  state 2
#                 0 0 1 1 0  state 3
#                 2 2 0 0 0  state 4
#                 0 1 0 0 0  state 5
#                 Notice that only state 1 and 2 are valid, others are the middle states.

5e8dca59660e8e17919524342b33b66f7f81cdcc505eed45f01725f443eb8ab7222ce0265a93136068e22e616b1ae2160442
6e431be502015327e8ba426d4036b4d4e4c6b131a0c396a188beb51be187cd056b2224d36fac222c859054fefdf6e2b1c434
324ba631c5c1f5abbc2df74b57f86731cb33d554bd4b6a10e3467e0f540da3565633d927b2113e15aee4570ae990462ba04f
697ae965c7865c28d6afd443b753adfe857c95ac5ee31fb09d0d21b877a3a2f9931847c78d0816b60983f7473a8cc46ccd00
c335c4619c36ffe200a65431966b2333cb497da3b1fbd8c3661ab41f68cd81ade5ae614b66e8152d096c91f474c4fe7b947e
dfa24db59a487c2d2d7c0038280e1e2a6ff88f18683b334e763512aaf66a5150b278d244209be73f26b86099749e67b33106
81e178bb0356be68fa7430ce33eb49f845e698453539afed240408c230462fcf6669d455ca5f022ce59c17de9deceb4ec750
ecb1f39ed5a02a859142f1cf93df3a68ae82a08a9b9cd2dbd370faddd0730f75daeae36925514b11927d8a4cd2ab9402db58
dd427d0c16db294dbcb1eb6246436d6767b651d6d1d08c6b0e4a6d99574292cea24766e9b45e31c6e5c69860653b521136e5
70ff01727d214997d61d8f458ff534df58376cb0df73710138699fbe59036632d61780d8063b78b1edc2d8767ab7d9271434
76c4a4b920c27a19502c5132ad4ec38c7c2d2d7c37a5f4309f63452713488164e1262c63166b04e096623fdfff6695abf1de
debaee66ab8689d638057932a221a66ecae93b38dd84bb63c26c83d122ecfc0c0163bba62fb628212949ea1c8abbc710e6ca
596547e71d128f69cf5607e9b2e45808a915842ccf6f2aaa543c712b005e125cddcff53a1dd67debfed484115c47c3418f12
f497b1657819f1434a9c4e2030add5ef2831a81a0eec1280cbca2982bee710b633b09dc690ba6e52a30ec4ec259e39c655a9
7f57b880e5045ec97fb7fe06f9e1912f3b7efb47c7c8d3eb524e88d240f176d4e38618e18bfecca4f15c469f45e240723893
242c6ff0ce692a700572a4f10fcad1e464c54fe79ada6aefae52

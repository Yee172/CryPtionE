# Alice enlists the help of some friends to generate a
# random number, using a single unfair coin. She and her
# friends sit around a table and, starting with Alice,
# they take it in turns to toss the coin. Everyone keeps
# a count of how many heads they obtain individually. The
# process ends as soon as Alice obtains a Head. At this
# point, Alice multiplies all her friends' Head counts
# together to obtain her random number.
# Define e(n, p) to be the expected value of Alice's
# random number, where n is the number of friends helping
# (excluding Alice herself), and p is the probability of
# the coin coming up Tails.
# It turns out that, for any fixed n, e(n, p) is always
# a polynomial in p. For example, e(3, p) = p^{3} + 4 p^{2} + p.
# Define c(n, k) to be the coefficient of p^{k} in the
# polynomial e(n, p).
# Find c(10000000, 4000000) mod 10^{9} + 7.
# ----------------------------------------------------
# Analysis: brute force
#           Hint: e(n, p) = \sum_{m = 1}^{\infty} (m (1 - p))^{n} p^{m} (1 - p)
#                         = (1 - p)^{n + 1} (\sum_{m = 1}^{\infty} m^{n} p ^{m})
#                 Notice that \sum_{i = 0}^{n + 1} \binom{n + 1}{i} (-1)^{i} i^{k}

1d226c943307e5696cb6c5e1e2c7f4f7456f0c3b134a4aaaaf84eea79c8e1fb288e42929fa704d09d0321fa9d300a90acebd
e49dc72ff9a07f03279ce5c224332d9dab94bd8d0bc7fb564dadd5f980780507a58bcee3d31294e58ed354d7965157c92408
701c1746d9c77108945d8450f87ff33bac0435b2cf908c49fda8cdf850bf85ce921348251cc018ed303b083725e34e588319
6c9f4b7d97c2cd3d86951b43c20444eea28834364384c72b9f9a960804a01b8b396716dd9600871b25cd0b78f07643148c9e
9bb8c7997670ed5764f3b762050a1ca642bfd6dd146f0dc3b70e491cb781b70ecf9ec9c91cb7f89911f3d02de89ee6128f99
df64ec5900ce7c2d2d7c32fbf8de3469360ab7b281c9c76d4fa72706b26ba4bc49d6a056b79ed87d76298b93f33ee11a21a6
687c23ae101fd72524afa8ffec239698a2f50f16baecc07d2b2d9302404c1e626f03f893f4d689619583f79cd2cee78d8b97
bb136339a4fa11cadca7cdf9fb6cf8492047a2af62c5e5d939f3fc8de31806a9bbd6f5d1c08af943c2aa7b2053a3b896ee50
48dccaca0031bcaaa80f54ae6933b4e70e7d0a572858c17009e1fcaab7051bfd2e43e1e5e692d34df58e6e5b1d21901a8bfe
345222f7a199922be2b46296bda4f8a739916f0909fc0290d67a17f61efaaa52da4bd59a2f119e9fddd89f4a46e13be7175c
089a81fc442e04f04f22140f394614e67c2d2d7c1029fb5f85bf0ed3fb193eebbbb2d742452eb0a75384d8fe16a3f0342d65
d51f83acbfa9e10fcc0b5eca2baa69daf54e808f881fe8149c6a3c1e9b87187855c6fd8ac312f4bdb9a28b3e7a7fcbf3aeff
25cc46a66dbbe4483e311c9ac6e756405c89b7ed2d06a53ef1cf4f556a70ba4daebb0729bafecf13fc4a2db3aa212c3e1bff
22b96e9d0fb68b846e1e07d428fffa15e70585ac5f5bb6cf4cd71d2ed2351b01d1f75c46cf59911452abe3330b86356a0f4e
0e042f42430324199779f2b24fd9f760f29c6e130b34feb81c6aade2524453be056d33d9e4c6d18225d9457ca84be84b9f0b
856a9c600f5adcb5e6e657ddd87b0357ea93595bbe8bc7e45f59

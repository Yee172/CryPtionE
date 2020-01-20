# Taking three different letters from the 26 letters of
# the alphabet, character strings of length three can
# be formed.
# Examples are 'abc', 'hat' and 'zyx'.
# When we study these three examples we see that for
# 'abc' two characters come lexicographically after
# its neighbour to the left.
# For 'hat' there is exactly one character that comes
# lexicographically after its neighbour to the left.
# For 'zyx' there are zero characters that come
# lexicographically after its neighbour to the left.
# We now consider strings of n \leq 26 different
# characters from the alphabet.
# For every n, p(n) is the number of strings of length
# n for which exactly one character comes lexicographically
# after its neighbour to the left.
# What is the maximum value of p(n)?
# ----------------------------------------------------
# Analysis: brute force
#           Hint: choose n characters from 26 characters, then divide these n characters into two parts,
#                 for each part pair, only one pair (left part are all greater than right part) not satisfies the condition
#                 i.e.,
#                    p(n) = \left ( \sum_{i = 1}^{n - 1} binomial(n, i) - 1 \right ) \times binomail(26, n)

4283eec06a967939569db40e6186387cccb2d8aaa7fc98b05a9e236c51db48db77d5b1801c950a4b9d9f7bfc366220431951
6a44279ca2d56e0237d1026e7b79e1bb16c9a7b878ab66afaf42be53ef14e8e65237ca4cb0a957eb7981529108fa18e19c6b
fd1c4f84e0e4edc80a87ca85b554f2ceb09edad343fe4ad35759f6c2e3a5064518ff99507fd2f518f1320a386e25e5b3ef6e
5dd0f9ee630c9f364736738aacf853e3e1763d9166490fe5c24cf6cdf292008773f86caaed74de771a245a50a45111597d14
f8c7cd2ac392135e30528acbef29275e9d3a826b1ed1e675f3a2f91fb37e6d485d19a0ce4f4e09df6b20b4c961a19e1372f4
4767ea451e567c2d2d7cb3224761e4ea279d98884da7cde3d107b67e56d5ecdbcedba89eb0875609ea68ea780d5c6a148058
6d75260491b5c70ef9607162f039b4380ec905587081d427a4518f1ef07f05769310b09bce27d361ccde0ac7cddb841d16af
a40d30148601b18732d8a36802446fdd06608a201bf11d716369f4401df9f2c742c9142e4fc83d657105752bd3acfd074232
362dfe609c973f1ed7174d4e8b72d9b34e39f1fda75e0552c09eaa23a1adac5cd993dc1d20da1ef35ffb0486a44c6f2ea51f
49e30631a64da291ff22093c6acb8f180863204834f16e1eeb0e7666db8b27b4eb0e2607143d7f8dec726ffef50e1dd7aed3
5bae78e54a006fa5680a4b13fb8bb078

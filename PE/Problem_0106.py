# Let S(A) represent the sum of elements in set A of size n.
# We shall call it a special sum set if for any two non-empty
# disjoint subsets, B and C, the following properties are true:
#    1. S(B) \neq S(C); that is, sums of subsets cannot be equal.
#    2. If B contains more elements than C then S(B) > S(C).
# For this problem we shall assume that a given set contains
# n strictly increasing elements and it already satisfies
# the second rule.
# Surprisingly, out of the 25 possible subset pairs that
# can be obtained from a set for which n = 4, only 1 of
# these pairs need to be tested for equality (first rule).
# Similarly, when n = 7, only 70 out of the 966 subset
# pairs need to be tested.
# For n = 12, how many of the 261625 subset pairs that
# can be obtained need to be tested for equality?
# ----------------------------------------------------
# Analysis: brute force
#           Hint: only the equal-size pair need to be tested
#                 #(equal-size pair) = \sum_{i = 1}^{\left \lfloor \frac{n}{2} \right \rfloor} \frac{\binom{n}{i} \binom{n - i}{i}}{2}
#                 However, any pairs satisfie B_{j} < C_{j} for all j or B_{j} > C_{j} for all j are surely satisfy the first rule
#                 WLOG, we say B_{j} < C_{j} for all j, then it means in total (2 i) sorted elements,
#                 B_{j} means push into stack operation, and C_{j} means pop out stack operation,
#                 which implies that #(the combinations satisfy this condition) = Catalan(i) for total (2 i) sorted elements
#                 As a result, we need to minus \sum_{i = 1}^{\left \lfloor \frac{n}{2} \right \rfloor} \frac{\binom{n}{2 i} \binom{2 i}{i}}{i + 1}
#                 from #(equal-size pair), since these tests are not necessary

6fa859ae04ace5cc45e940c68908958223a1a11784981761babe2ebf6bb936e96b18d50600081a6272c99d55d9e860cf5205
6c1eb07f484f7cddedeb693087a38d7a6f033755de3aa5d0851bdeab00dff7b832527718f9c2ffcaf9e11c4e391201822415
cf06b33894043fa40d29142e8663ca7f5ec331fe8f89069bf681f6a92432267051adf0b7f60e88337d829df4b2c9316e7ef0
af59b49e8622c2afb11f081da256476b282c0e7012aa7b226e78973867ce5b2cdef753457be3405309ceb11fa73f1bf23d28
6757bc79657ccbad6b6e2900c8ee7e2a0b083e8c49ca40028203069f93a5e8a53271fcc585128088fd9f0926dfee7fb0241b
9440771791f57c2d2d7c00a8e54055bdfc023f2e1a7cdca5b28f19a9729369b8363b5c96a2481fdc166279d0fabf70940e2f
321ff38556c78ea014eb5e5be16c4b5f65dc513802b7b3f8c8cfbc092277dc9320e59008147bd8278a324294aa7b0b605bde
ff0eda71f6d8d33e2c4c8d38f485af131d6ad08bbbb3a6ae881bbdffe2ae54c33eb53a68e540771e6e7f2fcf448194d0fe17
2c2694018ccbc5530aeb23b97bd7b7f019b37c6e2747772fef3a88c329c74ef262b2f397ffe74e0ea23546fc794bc3beeb51
a7ebf4c3011054c700df211609566e02cf7e74cd62c48c51897a6904783d60731f49152448425c8fb92f9d482fa0b53a6c3b
d28c62ddab92bed86588a72a2fc720ba

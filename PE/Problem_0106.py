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
#                 However, any pairs satisfie B_{j} < C_{j} for all j or B_{j} > C_{j} for all j are surely satisfie the first rule
#                 WLOG, we say B_{j} < C_{j} for all j, then it means in total (2 i) sorted elements,
#                 B_{j} means push into stack operation, and C_{j} means pop out stack operation,
#                 which implies that #(the combinations satisfie this condition) = Catalan(i) for total (2 i) sorted elements
#                 As a result, we need to minus \sum_{i = 1}^{\left \lfloor \frac{n}{2} \right \rfloor} \frac{\binom{n}{2 i} \binom{2 i}{i}}{i + 1}
#                 from #(equal-size pair), since these tests are not necessary

3e44951cc5ac2da0d60f79c56619478599a03b7da1436b835483b6dee99a69c89a6bbc89ac42ef1a8c6520855721b053d6a6
ccf823eda9d26724e08808a70cc95b939bc13c7be60103365090a33cc2cd902e5eaa8561a6626091f375438a4f6f51c01836
b1be710f0ccbe577c8d77889151ca5e319d73bd1ef7b57130fb261d9d2d726e3d5ae3ef86f820d11308dd90a0b3a440d6273
001b169cd520dfe9d3983912eef8dc2d1bce5ddb433a8fcadbe4ead1e9cb7be7003a7383c5045c735d527bcd26fdf585578a
0f5f0ff723cc50325d2df2a1cbf278157f1dbf3b0af616d49f4b7e866366392ae9aa06c688c3c8b6ed25c0703a06ea573cd3
f883e323d54f7c2d2d7c6fe927aa8155ba497142cea44feaa085d5445024ba318793d8aac51e2e97aa02ab934084aeb24314
d7bd7179366a45536a7bd8b6819428dc7ace42815da12cd5e1240f9e393b7a842a845c4f336fffd6d723ec1f9fdfa67242df
1c5c4c1b5f5d6045cd387490960b3e78324a2bc33ae24e01cb5dd8e40b4be196ad4bfc1bf0c7ca3d46e0d478784ffedf5914
dfa0f89066f9bdfae23aa5e09fadcf999e2bf98e918cc14a9526dd80a2c74ef7ac2c0cf91b1617bf2124d8f93d1833f079c8
a9d4848bf4c96face631ab4653422c35234d392e899f3fa7eec276a9fde49fb3b8a973dd9b1b4d8650c5d51629b9d88c6e7e
b3db6129ecbd3b724c8cd39c0e4bef63

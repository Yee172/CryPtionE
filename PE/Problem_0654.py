# Let T(n, m) be the number of m-tuples of positive
# integers such that the sum of any two neighbouring
# elements of the tuple is \leq n.
# Find T(5000, 1e12) mod 1000000007.
# ----------------------------------------------------
# Analysis: Berlekamp-Massey Algorithm
#           Let D(t, m) be the number of m-tuples of positive integers start with t, we get
#              D(1, m) = D(1, m - 1) + \cdots + D(n - 4, m - 1) + D(n - 3, m - 1) + D(n - 2, m - 1)
#              D(2, m) = D(1, m - 1) + \cdots + D(n - 4, m - 1) + D(n - 3, m - 1)
#              D(3, m) = D(1, m - 1) + \cdots + D(n - 4, m - 1)
#              \vdots
#              D(n - 2, m) = D(1, m)
#           Then we have 
#              T(n, m) = D(1, m) + D(2, m) + D(3, m) + \cdots + D(n - 2, m)
#                      = (n - 2)D(1, m - 1) + (n - 3)D(2, m - 1) + \cdots + D(n - 2, m - 1)
#           Keep doing this process, we can see that this follows the prefix sum similar property
#           Let A = \left [ \begin{matrix}
#                           1, 1, 1, \ldots, 1, 1
#                           1, 1, 1, \ldots, 1, 0
#                           \vdots, \vdots, \vdots, \ddots, \vdots, \vdots
#                           1, 1, 0, \ldots, 0, 0
#                           1, 0, 0, \ldots, 0, 0
#                   \end{matrix} \right ]
#           be a (n - 1) \times (n - 1) matrix,
#           then the element at the upper left corner of (A ** (m + 1)) is the answer
#           However, the time complicity is O(n^{3} \log(m)), which would be large when n = 5000
#           Thus, Berlekamp-Massey Algorithm would be implemented to reduce time complicity into O(n^{2} \log(m))
#           By the way, using PyPy3 will be much faster.

54cb3d1244362a08b4a5e74e4c86178b5636022999357922122dae72e871725539980d1d90eac5f1605e394f586c07c11d0a
aa41d8146e7eee2794e1d4763609088704ed3bd5318748c267bec2912079d7e18aa165f6f64b5f16c7ba02473a2b0cd87f4c
2be1b7f8e67e4de2072607ca760989f314a83fc0d1f650fc194f95a9d69d017afd396021b16dc763ef1939dd25239cf9eba3
37657e9d1980a625b45c2d3d24600765a66fdd99b38b4b53e87760df016c349ddea4d66da88644759e435d5d4b28dde21225
5e7f3a9457a578a6ab5d71ad9e2314af75d09c5d78e8808bed688e58fa1d6e5015f4fd653bb7a3f40cf1144aef4bae2d154c
08c473258d3e7c2d2d7cc90a2f4726b417826c04f0fd5358a483af87be360c3960b3b76fd913f534393c5dbe74c2ef95e5cc
86320eee098703c3f2c096a5b50cd8c94111765ea2bf9b7bc49af2a5b74a8ba607ec35a46253c79bfcd4345642fd42c262fd
0adadac803ff66ac66f40c55b98d60fe10976af49b71543901ffb027b278ce931a3e890560b4389617973935630c4c058ce0
008e3623a7695c6622539132523539ceb0e5bbb90b80c043b0138a24c6716381d2bf62f6bd6c73905ccfbbdd96921efdc363
7c58437740b761f8bb5e0a29cbd32f92b538c43357c31e95a89ea6c2dc6f2a95008b9e87359ce7a29c01dbf759903ada77ca
4036fd86a10af2572034b6a06c6b10b57c2d2d7c722718cf3782450dafe046b0f1a3425c7b8acce62b2b541c4c7f3ca45447
e09da54d549025ee79d6916eab046ec66942e687e04a6c76f1bcfb26ffb1f40f64caa06b0808435fbe1b17fe3d333b86bc58
dca9293ee1972dc3d7807fc8b2fe025cbc6bc5d7657c558fb3da7200c7c7ddfe25f9137470ad4fd62e80f886bb8de106f279
511e7c3ada5f4123980bd6a7dd87ab7ea30511f2d6d613a0dbdffebc91e1f36fddad373b11bb752fc213e38478fe80cfce03
e3ebf7d8e48b76064a6d977a36b186d2c835efdafa20eecb1ce5144358e635e81b5ae025cce7d54b05eecc3f2a66c1a49008
1eb65dc012b74cdbd0e0c4ab6b0ebf7d6a94619ad82429717a357c2d2d7cc8cef0911665bcb7d486068463541fbec6b5747b
ba6c9ab5c81db45c57ab87d2487641c09fa6d788d79dd1c102226e064bc85f6b51e3ec0e32f80d6b4e4986d1f61f861bf2c3
c82b818eaab85c2d6a9871c6a8ab6017ea099416be197c2dc8d9a53000dee652d6ab1d99fcbfb4a65feb6fe35070f147dfd3
2e35e53eeb93a3f8e3ba5ade0025fd31fa9a1beffe6d3288a71b0160b51098bf433ca012b3b15212ca73615cd7b3c0f08f95
b0f6023dc3fc872d489e944419433c2681f078724533edb091c97d3cdac412beeaf02b4cf5c38e1e6dd05dc56a3bbd249d75
0b6a273f196d8b02eea5f67460380388270ef81e3bedbb217f6a4f17bd2e22162e6b564d

# The number 6 can be written as a palindromic sum in exactly
# eight different ways:
#    (1, 1, 1, 1, 1, 1),
#    (1, 1, 2, 1, 1),
#    (1, 2, 2, 1),
#    (1, 4, 1),
#    (2, 1, 1, 2),
#    (2, 2, 2),
#    (3, 3),
#    (6)
# We shall define a twopal to be a palindromic tuple having
# at least one element with a value of 2. It should also be
# noted that elements are not restricted to single digits.
# If we let t(n) be the number of twopals whose elements
# sum to n, then it can be seen that t(6) = 4:
#    (1, 1, 2, 1, 1),
#    (1, 2, 2, 1),
#    (2, 1, 1, 2),
#    (2, 2, 2)
# In searching for the answer to the ultimate question of
# life, the universe, and everything, it can be verified
# that t(42) = 1999923, which happens to be the first value
# of t(n) that exceeds one million.
# However, your challenge to the "ultimatest" question of life,
# the universe, and everything is to find the least value of
# n > 42 such that t(n) is divisible by one million.
# ----------------------------------------------------
# Analysis: brute force
#           Hint: you can use dynamic programming to get t(n), then brute force which one satisfies the condition

7470d336d31ea8d0c76aa43893eeb73c85a62a1b8ccdd82a2ba7a3e08ec9f0479b2196b1d0b2095a9be64bc142770753c291
c7e6b25928f8b6dc46cd35cd4f442019855a699efe9b3b9e52db09985953c56d31cfd9ae5f55721e58f32f6a31328847dab2
226b52ee10294dc596824438fe6c767cf68d853fac948ba0b54141683978709ce2b2c4db58641b7126e9d7771232a12eb417
4c1f29dbb70a8ff125a07b7a6480887dbf4bf587e56ae94773375a415351eeae9e8342c6bf61646542c28727de3a84f74951
63583cace410a0b77519c858df1f0ebf27181d456265baaf0ae590bfd4728218f51443f65216a652d4de6d1f996ffce46400
b77f1aa378637c2d2d7c9cf720579371a881939779ea8d264b892b79236fbcd870744b25b5bd968c4511b09bd0e5c4757f66
e8019952bffa2a9ff871e18e4410e2018d9aaf1ebd96c80e0ee3f61ebafe41373ad969a3b3f44cef9df3bf99ef636e70ad8a
3153b7cc590ffc028a1c83cddb1da387102ab9839b84a73f6a7676404bf0b12491962a6a73f96a0d35701bba23cdbf452db3
b7233fb170d6ce482b6bfcdcceba4395d56a0830feda60200183c69971d45b5faa6cf6409ac5847b1381f423cc14459e8187
fa7f06bb61f7cd6fb595704b6139f188ef93163c90932a5dfcd0ffac3cdd224a60a4ee7f76dfd08b50ac2b4a1723990ea983
fb77b6e2f3db927d42bd25de9324b4677c2d2d7c1bb5c21c0b65a21d0b1c0a928a5c14011434331ce53ef705660f731ea756
41763e23ae7b6856729a7d26be45b754c1eae44e43bf50d73296d1bd046d225fdecf28b065691de32ca76f17f8815015b389
8270ed8801046d776ac480a0279a44fe1358dadb8c201d67c291162caf660a85b785b4b8b952a51c81518590c71947d71ea0
e81f6f2546e646d525a947554e92e0dbf8d202a18def7e5cf3784c165112324fde67db8b85a247b96e684b7a6ad93b16566e
c2ef79cfa6fc15d41412ec03ce125feb91e1abbcf6dc2c0a0311121fda76d9b2d30f35fc8da8938a1729d867349b37f7ae51
187fec629fa403ad8065017beea5bf3f7e42f1c04cf54f6ef5f2

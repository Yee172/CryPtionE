# A number consisting entirely of ones is called a repunit.
# We shall define R(k) to be a repunit of length k.
# Given that n is a positive integer and GCD(n, 10) = 1,
# it can be shown that there always exists a value, k,
# for which R(k) is divisible by n, and let A(n) be the
# least such value of k.
# Find the least value of n for which A(n) first exceeds one-million.
# ----------------------------------------------------
# Analysis: brute force
#           Hint: according to the pigeonhole principle,
#                 we know that A(n) < n

87a5ad0d5750cdd4eca0a03e488ed9c1595d30923a5e73e8e32f980cad76b05038c5f60082085898c9624b6c5c9a7863998cdfb260769b698c08da0b9d337566f31247ef04a84454c9a882c20df5d703badaeadabfc6ec0cfebfceb28b313cd95cf469c0890266ce33ffa856e6f8f88b2357f9c7e689a64f5e9ae2698e732e15e97e17d6c8e96e31eaaee80fbedac3d5129a7cbb568041f12e21766e0bb267c554917a48ea34f1434622f9d643aa2a51223e47c133041ba962fa3f7e2f08ec94602d47f4e85c6e3cd608a5c5a50394da611f6422746334098bddf938a58bab12984a5b705f95418d19524f9ed3559c8fb998d0e9e6ec488f785cefb396444cfd7c2d2d7ca0b86893330f5d67bf03d6607a5226755843f04e7002467f947cf82ffcc11f8853b6b11f2645f48f1fe97d40b5df02ed04481256a007bcfc7090aed0f80df5df860db1c071754275f82543c3a50d83d55cc8202ae0f5642378a76988a13b5cc7018a5fd2b59fa6c26fc3f08aba61cb6cb100e746b39b648d90425c38d028b0985d03fac794b834c22f4328ffbfde519a727dfdabe1bb8f18e1f2ba354933697424c73b301ba98707595ef8b9b53d858de6f1db3a382d3018e6383148d282092eb09750c213c8d3bd75d289f2bad713c050e9b6fe207c9659a44f7aa43ac892eeb743e8fa8ea513d1c6e7a09f1138335fdcb444fbea1b00f95fdd90405693c0b4

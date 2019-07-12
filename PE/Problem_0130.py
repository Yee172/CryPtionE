# A number consisting entirely of ones is called a repunit.
# We shall define R(k) to be a repunit of length k.
# Given that n is a positive integer and GCD(n, 10) = 1,
# it can be shown that there always exists a value, k,
# for which R(k) is divisible by n, and let A(n) be the
# least such value of k.
# You are given that for all primes, p > 5, that p − 1
# is divisible by A(p).
# However, there are rare composite values for which
# this is also true.
# Find the sum of the first twenty-five composite values of
# n for which GCD(n, 10) = 1 and n − 1 is divisible by A(n).
# ----------------------------------------------------
# Analysis: brute force

7df2b75983db9f5caf8d7ab677277a2e02aa95f60573c7ffe4a74494d41aa1d04f532876276945044c474c2dd87d6e975cc6f0341a27fdba05610ccc5b1c0b828ccab40c26211650590d00415bf43d76ed891bd2b664220f76c20e81e528596ae15cbcaa03c3ca99b42227ee3024a68cf5fc5b6d928b92a3d9bddf75e4dce4140df3282e21d4fe70f0b07aff3b84920809d346fd8d80745e0ab5fdd2011678ddc17a615391cde82657576fb922e0d1ac5afdbf9d655ce96d73a61fd50a4c11ad3a05c8b756e0b5d672ef21ee5913b0bd874eecb24dc0af1743cb24ec0a72794c35c4a5e521526dc11585e383dae6ae7652196646c06556100e0ef2d1beb1aceb7c2d2d7c86fdbf960092dd82e12e93ea9ef890911b5c2c0655a58a161a4c66f9bcf7bdef655aa68309ba713c124eeddba1700ee45a1f5180546c719c53829fb5ccabf22819390cdc32f618ea85b0b8a066ebd8ef59edfe970d89567377aaae34a45da3daf9af082df289e49787365520fc9b4b5c45a12944c6f8b3759ad5064666c46a75d1c2fffc4ea7ed616e1b59facd408edd70d04ad8120c71408411a7feaf9f65d80f049eb1de937ca8c4e763f45676b25f91e8ee288255fa84631bc72ab2034486688a5f58053a726b5537ef0884863a8e402f9292c9532d6a2b6f53574483faad4cf6ad5fc9f17d3a7ab9510431ba46ea7f69a9ec3316148a3dc1d759b399e444

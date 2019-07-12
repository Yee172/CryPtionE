# We shall say that an n-digit number is pandigital if
# it makes use of all the digits 1 to n exactly once.
# What is the largest n-digit pandigital prime
# that exists?
# ----------------------------------------------------
# Analysis: brute force
#           \sum_{n = 1}^{9} n = 45
#              => 9-digit number is divisible by 3
#           \sum_{n = 1}^{8} n = 36
#              => 8-digit number is divisible by 3
#           \sum_{n = 1}^{6} n = 21
#              => 6-digit number is divisible by 3
#           \sum_{n = 1}^{5} n = 15
#              => 5-digit number is divisible by 3
#           brute force the remaining

c20eedc51461b6cb35e711aab456216e8d13485697a024f2140b2a6d916ca9ab40acb5aac6a7f3188ca78da896725181e774281f022594a44b7b54cae7e9dccc1a80ed81ff088cffa2cfe71c4173a87561a499eb5ed433e54ac8730069127422daf7b04c3e7e64171a9bf0a1611f4d5acdf6a3e050f4e0475c68c986a33597d97cfb9d37b0cb6ff89a02eac01ec792d329b45e35b51148b5ca31c46d920467d9178780fae3d9f30572c494d7592c4918b0ecee6221b2a0d65d04b6800f090bf1231ae525fe430c480c18788daf99fedb89855a69f59725872b6537dc019d3116a019f263bd90fbbce9ac8f29d947a38a3c72aeddc3d1a1d62742dfa56ee8daea7c2d2d7c461c50873fdf7cc90f90b77627fedf299ed47fd9b7100568f539e2fee3d1e8eb7b2257fea9eb18a0b6999957efa09ba2d8a7d062c2863f44e1f1a8f190b993e4e7f6f75e37f1916409cc80408da2f996c0d6b0e801b00580b192488e2ee3497886be361f4c0058e8f383a99156eef7bee5a4a994530a32c0fc39f82b4b3ed31f12672db4bc7f67401beb055e2993f46723b9021b142d1181827de9a2b2d11f2e0dd360c91ada81f57935e2199e2f4ca8448240bc6f70b23949127d61f7644c496e221e7275de479c3d5660c836d0669117aac6f4ec8cdc654129e9ce3fb735079603f3e1bebfd048203b59999daf2d513735f4e999b443f9f2a5ab46773d6666

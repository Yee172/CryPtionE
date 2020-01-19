# We define S(k) to be the sum of all numbers n where
# the sum of the prime factors (with multiplicity) of
# n is k.
# The Fibonacci sequence is F_{1} = 1, F_{2} = 1, F_{3} = 2, ....
# Find the last nine digits of \sum_{k = 2}^{24} S(F_{k}).
# ----------------------------------------------------
# Analysis: dynamic programming
#           Hint: consider dp[i][j] represents the the sum of all numbers n where
#                 the sum of the prime factors of n is k only using the first j primes,
#                 then we can see that
#                 dp[i][j] = dp[i][j - 1] + prime[j] * dp[i - prime[j]][j] (no prime[j] part + recursive containing prime[j] part)

bf3065b60be108e19c85ef467ad95c06eb0e2672a418b81829e614106ac3bee693cc55530752b4a026f5c287b2051902e668
5af27a14cc2a1d1fbc0a7d53708b7201949e09f4722802510743c63a92f502d43463f253561b387fe92ddfaaeb2a6856e8b2
128ae1614388934e484b7cb1cce41906372415a8c9edbc417751a8e13111a2d98c70062eb2a4fdbaebad9ff87b3c99c56bf9
46d3c5af39d76b23589026f07eb74b97d2b57a3102d639a52c18ef0bd8cb08fd84eab745a39801c225b70a4bd8663eb92626
4e85d07a86b1e368b32c6b35fab09fb5bfe1182041ceb231d33049a263867482ff4642db50934602bed37c3ef3fedfa9486d
8581560bd5767c2d2d7c38f0315e7ca50b77c6593c13989233af32cbac99f499531b40730cbaa236805cb3ebf663f9455406
88868e89a690aa346ebd29d13658c05dd59780c35e6b8c74e087625ac1a9a7022a4ed53190c12d72c2523650a1cde422d4f2
724c4e902166c06868c3d1409591dbadfb16da8f1aa2b2b13f3b879462e5b87507b85d62e56051fdd383c2b1b8c9e8c4bf13
dd29acbd30e5a4f49969b10519d0e0bb96e11588b958a8f3232486a141ffa0eb6976b4e26d9ad6f4bc185adce1231c74e659
f4df0380e145b11e6cdab22e5c1cf620f81b04827cce23038fe4889ba606cea54129ee16d4ae190119d5b7774637109e0009
d9d9a70577c5d571b5f0f11bda31f85c7c2d2d7c16225644bf18a1d65ae4fab6a85ba942feddc928a1d625dad92a491b6d96
6305a526a05b69362337398999fabb25bd944b34cd47a9fb64b3f4b1b02f1cc5bf70cac2335bea298e99ebb08237a008fa4b
63f4c896a9118bb7731d6a99b02e89299d67141618949d240b5bc4bd2c7b4158aa81bbd1e1ed48882bd62fdee78fc594edca
9c7ea2abbb0a31bc756746ffe924429d246b7844dce49593aff5deb88d7de0d3bd7692d6fbd2fbfd139781c0cdce0bd9df50
6c1ae8958accb7aab5003f5c1b7c30613bf538afaa6b4748dcd47e6703ed746dcb1e7a19e51aba88f5bf4221d18ea8e6638e
2fea6d0462f87bd51a1a2293e0356a33c0e2a6bdd6ddb03c91c0

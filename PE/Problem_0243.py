# A positive fraction whose numerator is less than its
# denominator is called a proper fraction.
# We shall call a fraction that cannot be cancelled
# down a resilient fraction.
# Furthermore we shall define the resilience of a denominator,
# R(d), to be the ratio of its proper fractions that are
# resilient.
# For example, R(12) = 4 / 11.
# Find the smallest denominator d, having a resilience
# R(d) < 15499 / 94744.
# ----------------------------------------------------
# Analysis: brute force
#           According to the property of phi function,
#           we can see that we should first find the minimum
#           consecutive prime production satisfies the condition,
#           then enumerate the multiply of the second minimum
#           consecutive prime production to get the result.
#           Hint: Based on phi(n) = n \prod_{p | n, p prime} (1 - 1 / p),
#                 we can see that
#                 phi(n * d) / (d * n - 1) < phi(n) / (n - 1)
#                    if d is a prime divisor of n
#                 phi(n * p) / (p * n - 1) < phi(n * d) / (n * d - 1)
#                    if p a prime that prime with n and d is a prime divisor of n

8eb0e352911d2dc4e42d8bf4107471464197f5109fba143eb73bf9391cf8b2529cf6762dff8880f92c20034822b9acf319b6
ce10ea4bbfda957ccc4a28257ec6d825d1f86c368523c7f662f499fd20fa203fe50eb74896160d19eb2507ecd1558db5a7a0
f64ae1d49ead30d6bda84751d619d32fd94cab4292d9481d45694d0bc93cb90ed152f19f3a0a3b7bef598f6f4f35408b4e61
22180b836461ce4c0a4c2379ab60536aa08c6b04cf18142f145d255a4ecf410a6f2d328502a2a9ea8a23edee58736e0cc775
964ad5f1a8abdfe93603ee23c4e09bda3aa7c88c1cdcef2d4fa5d77803ff9a3083d68c2a5aa50d98465a8d0091bed34dec98
3632310ced837c2d2d7c80d4408e86a4e82432c749250174d2fc5396ea495e9314b51ef967b0bb4cf0c2e8b39c1fb2c880da
a5694c283852173d405201b1b8e6cb5edfa9f0d903e526205ead4a93b818cb794c918414beea5413baeb55af1dd68fd2129c
20bf3dd916227ff59da2df2d224f98271f1f08ea3e8a84880885cfaf88cf484cfda1de17242cb6d27f34f3deb1be7f46ac1e
433a9a2c63c5b85cbcd8a92900652d325726614cf3dff750f76afab3cdbed8801785f8b6f3b9f1ae92a8f3f10e213a8d5777
46a35dd0873c3c88623783b843968bfbfc9b5d1e4f1f6e3ab4f1c6ccd1feac1a5379b66f70a6cabd21d582e93357f9b73892
4b22bf0da615bb2825a1778a9e1c2f5a

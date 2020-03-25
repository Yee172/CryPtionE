# The function lcm(a, b) denotes the least common multiple
# of a and b.
# Let A(n) be the average of the values of lcm(n, i) for
# 1 \leq i \leq n.
# Let S(n) = \sum A(k) for 1 \leq k \leq n.
# Find S(99999999019) mod 999999017.
# ----------------------------------------------------
# Analysis: sieve of Dujiao
#           Hint: A(n) = \sum_{a = 1}^{n} \frac{a}{gcd(a, n)}
#                 S(n) = \sum_{1 \leq a \leq b \leq n} \frac{a}{gcd(a, b)}
#                      = \sum_{g = 1}^{n} \sum_{1 \leq c \leq d \leq \lfloor \frac{n}{g} \rfloor, gcd(c, d) = 1} c
#                 Let f(n) = \sum_{1 \leq a \leq n, gcd(a, n) = 1} a, by inclusion-exclusion principle, we have
#                 f(n) = \sum_{d | n} \mu(d) (d + 2 d + ... + n)
#                      = \sum_{d | n} \mu(d) (d ((n / d) (n / d + 1) / 2))
#                      = \frac{n}{2} (\sum_{d | n} \mu(d) \frac{n}{d} + \sum_{d | n} \mu(d))
#                      = \frac{n}{2} (\phi(n) + [n == 1])
#                 Then, we get
#                 S(n) = \sum_{g = 1}^{n} \sum_{d = 1}^{\lfloor \frac{n}{g} \rfloor} f(d)
#                      = \frac{n}{2} + \frac{1}{2} \sum_{g = 1}^{n} \sum_{d = 1}^{\lfloor \frac{n}{g} \rfloor} d \phi(d)
#                      = \frac{n}{2} + \frac{1}{2} \sum_{d = 1}^{n} \lfloor \frac{n}{d} \rfloor d \phi(d)
#                 Find the way to calculate \sum_{i = 1}^{n} i \phi(i) fast is the only remaining key

a55f462202ed4ebb697097b1a88f23ff6f7cd8a1fa7b5754e4d9a4cd9a0521e2d74311ed97c53005ce9a90499dca95bcbe54
96ee003890791ad841be05ec09ba2c50289e1280aeaac46aeb11bf37f10c87ccf662a72528c9ea4dc8bfae61a162785fcde5
8949bbc6aa9566f78958d274583247352d8a6670e9ed567286cef3c6b133b16a2f98d8182f91d09b1db16c144047e6fdd7a6
0a5cec6b6bd79cdf2a0a876dda53ba341fbc86038316f0727adf9f724bc3534a638141c9c66a5ae88459b8de19f1ce9efc5b
19e33347b2ddc926cafc0b1b08cbc24a7cf87fc6733cef433a5e7082ce54c9b4c1918189322586b27b34afb53aeded282bdb
763a7ab59f7b7c2d2d7c45e53362a06660514358b49f9e00a9b2b2d74f90531c2224e8f52241451c1d46fc52f913e2d423b5
cf29b647c25846f2655985cb2a4dcca98ff02cf9e649f402962b595ffa63c0e7fb1f2c6597f8e37b7354fe6f8609e04b80ce
f7b13accd2cad58ca7d06f1f3b694ecfc350fba3791060a003ee3f4cc953ef7204fcb57b5b8b3f5cfbd76eee8491c0cc7ebb
ba872531796c2d957fbc3a71b445b4fca4c87ce77a2c5ccf68036dd559994fea17855ab018c40cdde56e95368bf64057761c
6383bdecbaebaefa667735fae3186e62a7ee62eb31b39a0e8847d96434f653c6bf977f00d7edf549744e96419dfe53b8dc48
e329c214fa3bf261b8776a0ddb1a4760

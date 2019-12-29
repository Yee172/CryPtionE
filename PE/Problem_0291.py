# A prime number p is called a Panaitopol prime if
# p = \frac{x^{4} − y^{4}}{x^{3} + y^{3}} for some
# positive integers x and y.
# Find how many Panaitopol primes are less than 5 \times 10^{15}.
# ----------------------------------------------------
# Analysis: brute force
#           Hint: Denote d = gcd(x, y) and x = d a, y = d b
#                     p(x^{3} + y^{3}) = x^{4} + y^{4}
#                 <=> p(a^{2} - a b + b^{2}) = d(a - b)(a^{2} + b^{2})
#                 Since (a^{2} - a b + b^{2}) is coprime to (a - b)(a^{2} + b^{2}), we get
#                     (a - b)(a^{2} + b^{2}) | p, which is equivalent to
#                     (a - b)(a^{2} + b^{2}) = p (because p is prime)
#                 Then, we can see that a - b must be 1, which is to say
#                     p = b^{2} + (b + 1)^{2}

73a6416e3bc72c9a116b0834ca9fa0a51872eac903b01cd7d63aed0b2499752f9610be8c1a88b5f2198094ad5be1a4e3771c
ceee81cd1b047bc6da11085b840283bf291cdcdfbcb78d5aff5482a4e39c5205e18c21abf4a6e841b493f5ea05dd009af24c
b3f3a84feeb4e798b8e40fe270c5b119596a29858ad410799b9909aac42e753a64572abc64cae81e7158ab6183552328bc6b
585fe56e86d5052a257a97af18e5d3548bba762edde6e6680e2f540ccaa0f08c287e0368a3ce49424ca7fff0940fef00c2b3
cf19afdd3f8d1ff6dd5fa6422af4137fb644fab339f71349f9ef6ac83468228d7e0457cdaaaf4f5083dc7dfdec5b2a24f743
eca7c45e1d257c2d2d7c69f1acc09107109eae071abf04667f3a817a07331b46793440b68bd6008129b1df1a359f57fb05a6
f102ab0b642c8ebacd65d9379ad81e99ecd76650f8434ea37a6b423d8658b919b7e9a258067bc34f0fe36c2e3a6d76c8ffc4
4ef8e793118f8d070c025505fc250ae8cfe937c8132148d03defb769a78388e5d2e8706a46215034ad63f0ac60b96c88f5a4
221c830035e2cdd65866ab43c81b47d80d510be6b069f93617c1b34de77c4708cb52837fe3296aa6205d24f47d6d5acdc083
82a0d48cc1de3d13394341fbce386b626d371e630aa1934ae8dfa4897a6f2906d7f9c464df3e53ede282b31aa2abc4bd3c1c
6ab0765fafe6431b329344c30fa3f7b4

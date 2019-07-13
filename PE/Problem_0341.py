# The Golomb's self-describing sequence {G(n)} is the
# only nondecreasing sequence of natural numbers such
# that n appears exactly G(n) times in the sequence.
# Find \sum G(n^{3}) for 1 \leq n < 10^{6}.
# ----------------------------------------------------
# Analysis: dynamic programming
#           Hint: https://oeis.org/A001462
#                 g(n) = 1 + g(n - g(g(n - 1)))
#                 \sum_{i = 1}^{n} g(i) represents the largest number that appears n times
#                 \sum_{i = 1}^{n} i * g(i) represents the largest index of the largest number that appears n times

1558be3d04ea1b90ccca864b3a310e48955dfc7fe9d4982b9e807853710334f9f609cb5fcd0d7425021313d54a080a3605b5
8279c1712894bf9fd27751db9544484e6093a3d50bac9ab01f8920b1cd2d2ecba22f573d99051ddb4501e4ced9e9f8290252
1e00cd2d608480a9805cc272412ded9caa6ff5532c861102f510541e690b3562d3baa1653bd98d7c8e4bd40449db04cffa5b
13cdf30f52fbabfdbaf993158fed29087e5c6292e26092031f1b5ddd8e7d230eaef5995be6c452845754434cc26eaee34166
176073c5def6a6040aa38a1c85734ce4ce166f8fe406b30bc5103ff5a3dc0d80cbb06db0aa77db0d7d61e164fa9d086268a6
a0c723a4a66e7c2d2d7c336d6385c16f462f9278d6dec6603ea87754f5f136ddeeb4575d3d90ae917042b88f3137113bfbf7
8912d2f8e2b8dd2031da14db66c3bc01b3a9b00d3f7b21cbd75db63bf6e0d166b644ad4facc630b97c4924f155e69f9cdbc3
2deed9b5a06427b2adf5c2fd84a58878d4b8409f521e46864eaba3152de1ef6a433ff2fd2ef52986859f7139fa21ec88908e
f3205485bf85516661efa26e48b247fd23efd70384bd20413bc78806e3752e76546996e87fcf28bca9364a7092dd0d3ca20d
c373ce53e06e283e3e3a41481d6b11f26234ff01d722bc4ae13708804f3d505167be9d82f8bd300f24b3e3b657cac5f0e0fb
86cbbf485312b86348bff35fd8ff69327c2d2d7c8ff53454144c3cadf16385cb42f8a3fae1408502d23a45ab5a9fdbd8f0f4
b2a905a4a76efe47e15c2899bfa58b7e1d6e9550d54b0656c585ff18e893f87e32c88e6a52f9d7dc942fe2798aa72c80e052
dd61ea8b971ddd7df9a72eeacf2774505cf8ea83e75c0bec578718ee46917899562e2ce98c5c761b27e916d0e39aef0e3bff
bce4403b0c21125ad344d5a699c44431a4216c848af1d38b997a6cb84eacc3a760fca5dd61f972c25f0a6bd00fd4809d6e3c
75864df7ca809dcae2e235c8a9b93ee945e31479f0f70607f033e7e4b1e9fc4c3677b40c84b26433fe45cf5266d985ca04d9
62341a68e197a198464f1779cf5b41c1d77007a2f731bd2db4c3
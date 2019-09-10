# Consider an n-player game played in consecutive pairs:
# Round 1 takes place between players 1 and 2, round 2
# takes place between players 2 and 3, and so on and so
# forth, all the way up to round n, which takes place
# between players n and 1. Then round n + 1 takes place
# between players 1 and 2 as the entire cycle starts again.
# In other words, during round r, player ((r − 1) mod n) + 1
# faces off against player (r mod n) + 1.
# During each round, a fair coin is tossed to decide which
# of the two players wins that round. If any given player
# wins both rounds r and r + 1, then that player wins the
# entire game.
# Let P_{n}(k) be the probability that player k wins in
# an n-player game, in the form of a reduced fraction.
# Let M_{n}(k) be the product of the reduced numerator
# and denominator of P_{n}(k).
# Find the last 8 digits of M_{10^{8} + 7}(10^{4} + 7).
# ----------------------------------------------------
# Analysis: brute force
#           Hint: draw a possibility tree, then we can conclude that
#                 P_{n}(k) = \sum_{i = 0}^{\infty} \frac{k + i * n - 1}{2^{k + i * n}}
#                          = \frac{2^{n - k} * ((k - 1) * (2^{n} - 1) + n)}{(2^{n} - 1)^{2}}

caecaf3c56a413b5a23aacb77a355b9008193548bbca38ebd2ff8f5e39f2b0b670be84599ed8d18990efbb6816a39c418373
a81a611667f32dc9cbf345b2bf2a92ba08e14aafec4bd08a8f2e2e9ce7a8d811f3215a05c942272d3ff37a55fb8e1d28d351
c79c3a94c76ac2965f3f8b216a8f8fcbebdaa5015d55aa680f7e0ced286a04050d870b284c5a5e82c62460859941102154a3
a7e5e34d35fba347ec8005d68eb370022bd3d4987e6e009f2eb83c353bb6149a9fcc7939489cbd8c0b392425d3a214fe31c0
51dbdddf9d801ab73cbccbc66fdccaba7246104622b80782e71747aa92ab813a956b0a930a30bae9796a09aad22554c5d3fb
43e79018c8047c2d2d7ca608266c70e5af57c159d50ad7d72cd5a912e43c908faf2a05cc34434c09d9e8cb94c973c24d2034
d211ca2dedc34a836549225e580118fc4b988579c7ddf1f20d72f3adab1382a73caa0443b8c4e861400485503d8cb629cef8
f4fa3dff07fa20134c15ed4439fce28a044a181fae8e42bcb9bd616159194014a656e414513b7fa24aa73ec372e94005f603
83c5dbe7e63efd3c58928191d2f6b776704ff9642dc187a4d7966898272ab295efd57e4cc02fe2994d8c8ca89aaebce4f841
666a08167c2968306a8a262f31f05c1def8afebdbfa16461fececc09c440cdf6cbe9932c8f1f1fbb3de27c58d92077e15f8e
d1276d52eba07e9f4be2d727de22b9c6

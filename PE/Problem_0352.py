# Each one of the 25 sheep in a flock must be tested for
# a rare virus, known to affect 2% of the sheep population.
# An accurate and extremely sensitive PCR test exists for
# blood samples, producing a clear positive / negative
# result, but it is very time-consuming and expensive.
# Because of the high cost, the vet-in-charge suggests
# that instead of performing 25 separate tests, the following
# procedure can be used instead:
# The sheep are split into 5 groups of 5 sheep in each group.
# For each group, the 5 samples are mixed together and a
# single test is performed. Then,
#    If the result is negative, all the sheep in that group are deemed
#       to be virus-free.
#    If the result is positive, 5 additional tests will be performed
#       (a separate test for each animal) to determine the affected
#       individual(s).
# Since the probability of infection for any specific animal
# is only 0.02, the first test (on the pooled samples) for
# each group will be:
#    Negative (and no more tests needed) with probability 0.98^{5} = 0.9039207968.
#    Positive (5 additional tests needed) with probability 1 - 0.9039207968 = 0.0960792032.
# Thus, the expected number of tests for each group is
# 1 + 0.0960792032 * 5 = 1.480396016.
# Consequently, all 5 groups can be screened using an average
# of only 1.480396016 * 5 = 7.40198008 tests, which represents
# a huge saving of more than 70%!
# Although the scheme we have just described seems to be
# very efficient, it can still be improved considerably
# (always assuming that the test is sufficiently sensitive
# and that there are no adverse effects caused by mixing
# different samples). E.g.:
#    We may start by running a test on a mixture of all the 25 samples.
#       It can be verified that in about 60.35% of the cases this test
#       will be negative, thus no more tests will be needed. Further
#       testing will only be required for the remaining 39.65% of the cases.
#    If we know that at least one animal in a group of 5 is infected and
#       the first 4 individual tests come out negative, there is no need
#       to run a test on the fifth animal (we know that it must be infected).
#    We can try a different number of groups / different number of animals
#       in each group, adjusting those numbers at each level so that the
#       total expected number of tests will be minimised.
# To simplify the very wide range of possibilities, there
# is one restriction we place when devising the most cost-efficient
# testing scheme: whenever we start with a mixed sample, all
# the sheep contributing to that sample must be fully screened
# (i.e. a verdict of infected / virus-free must be reached
# for all of them) before we start examining any other animals.
# For the current example, it turns out that the most
# cost-efficient testing scheme (we'll call it the optimal
# strategy) requires an average of just 4.155452 tests!
# Using the optimal strategy, let T(s, p) represent the average
# number of tests needed to screen a flock of s sheep for
# a virus having probability p to be present in any individual.
# Find \sum T(10000, p) for p = 0.01, 0.02, 0.03, ..., 0.50.
# Give your answer rounded to six decimal places.
# ----------------------------------------------------
# Analysis: dynamic programming

9ee4fd1846ccae976230645038e052b9d3a0aed79b44c6ab3174c533157284f9924ee5cbe2b97c5c1452102aced2d6f55e02
ee9f97181ddfe0d744c5c2e673493253a862186a99a9d354c44e7f9e86961073be26f0c27bc431d8aaffc5b60407b84faf08
fd8155a359d99107bcf4836b67689e60a0d2e129d720bb7be3368c081b85455aff82c6a856f95dd14f0bc2712f45e591a75f
9db6f2d93bad7be68bc2577353673cace52ffe78df675ddf041e6ddf1ddb8ac0442f39c8bc24fcb54ebb90cba0fcbcdcd801
b3f0cfe5b7232b845cc9c593e2fe98448d6735375c66931427b5af540508e19f9bd34fbeebdc37e08a95928f7c4477572e97
5518ed1074647c2d2d7cb241a655d0f9cc7934caf1a66c3007584dc010f636523c860a871ad36098e486fdbbf28e23e6e36a
029239f5af0740050becabe69ab41dd5498e0f8ede7caf62ef11f326bdb7514aae5b8946c842e3513e95fb160589757b8751
de368630eceaf86b410fc1d4824ea2e9cc9c405b9286e4d9026c92e6b5f40fdde5f9f4b8099384826a424e73244ef5ae29f5
cf1d2d9462ed65d9277b3a240f374c2f382e0b81734523eeab3d27a50532fbf513b8b02494543e68634ff68fbac3f4f68377
010c07df373bd76bc1a61dcb8fa83b57785938e49d5e6b4b2016bf583d2d22e6e318baee1de937cb0b6633d4e8be98ae2af7
9eddbe8ccdd42c1c199c187d9583847c7c2d2d7c54179e6285944bcdd93656c904a3e292971064045ff792eddf0db4c6f58c
2e054123d0ab6844b2a5ee88721a8996a4e775a03ed07636c1f7d2bf6e62fc3ea1be4742467b2f889eaa3ba316a9eb49800d
8e17a5217fc04246f09987ab4e4ccb174a1781349a6eb510f51ff3ace32f226dbfeab606b88b08554e7a50435840da1b5316
6af32f0cdeb1c80f71fe505e7410d9b1adf34a4208dd371b95fe773be2e964a429814a8d34ea652f03856e16cffe3fe25453
429e644dae20c5fd36be457d34c645702a57f63d36ffea600a88a84e126272e18308a36bb9648bb0aa84b1970d93f80191b3
7afff941ee23337085e4d4b571ef01ff600c30706f09dc4e84767c2d2d7c339d77e934c9ee6ea79239b2943c119cf71e410c
607dd1177e307a5677fc167c0a434d33617a2b91dffab27fc22bf6a359d63a2bfadb9db1cf6076817750023f9841e3700d40
f76b78213787edc76dd0f7a571bdf1960ee723066c51c78e0dbd853097f52914401d89eeaf5c241e55601a48a4179de8cd6a
090b04541c0381254b44c989c9e7b8cda00d61a72f6e0609b9447147ddcfbaba6e52179b5eac4ff2da35c023918e144998e8
5a9bb658c1b62c3bb3f536f5da34f846948af3b062a0048137c48b9c8660c98e6f7818b557dc3db62c7a237bf7c14c3a0a26
74b607ab2d0976fb8206d90a83e3f02364d68a8b563c7281920ea76cb694ee5dc87bc1047c2d2d7c086fb783ff0aa5cd3cf8
0aac522d77a9c5c734496ff55551351ef9fc7e07b776efed6596757874b49704ee3d6485deb209392d0be01fbb0d98fd85cd
b1ef8c8f821e364f3ad844eac11e79087968e4e12ca515fc47a8e9a5ecfe18ad9f0c0672ffdfc0649c1e6cdf6a77966e5c8d
467f638a4a18544b75f42432e34311fb4202af2097bccb22a71cd8c791e98693d0d91cb8bde203e13934665be4026eb4fdf4
49f7517917f3bdd3ae6634699393e13158dd76e91ba480a17e34eaaf90af5eac97b0266e0108acde734ddcf33eb7b690ea14
ed5d40546ae489f33f14d55c6395e35c8746203afa069af19296311fda4bc0e9078d06188e1ef3dace102397eb947c2d2d7c
522cd5ad738e50912b5e010b6b8b3b8f54deb0728398640f7fd992b41b2dcf0bcdf9c71c6c4466e456ea36c34b150b6a3b14
ab7ccf4916618157e2341692e0d839f0f9c46b07f851797c080107b49dbed9385523669f0218a6045dbbe6a7154390935e4b
19b2a918587f828247e32e9a6a57d7121c01c1f2142d3687ba76709b057fc44a957fb1687edfc6aa446c545dce97ce931cea
89022ed0dd676d1aed683f5e0780c8cc32a94887b5f7c48ec2845ab75336c745e2dc92fd901a5504669080cc3fdbc318aca1
c5593b20827dcc75c1bde6fef946298422ddceb27ff41f8c6ff6a5477d84fa5f0dc1b461dca2348aa77016f36be941059f1c
c734825db7e97c2d2d7c037ce5114ddaad23c3a45984ccea78c830b96386c8f98d5befb192f7cb9980943868f30eb048d106
78f1102c9f8fe0dde576dd24484ee9e515352a857608060ea5452b57a0a945829edb656a74c9dfd4da6bea61d0b0765e807a
0c835e31bbdd2dc2c5311fc021f4f878409c3ee6c9a1b6510146af6dc83d674482454de0f496fe6b51b178d10ffa3c5f991c
e58c797c21b0908620287bbec594b156e9dcafdcc19aeaff5265d36fd9b61fc7515daa72a18eaed2526f53ce87b346a3ad25
b79a169e3cfb0958736a4a6e3d534d77794fe56485a9347e25ebbbc9be6e606c64558f54d13d074ec3c62f92019d9f558475
e41d0f650ea208859ae12cbad3fb93ad7c2d2d7c63695cd4bfb344db32456df45c82ba49a35d60e51031f08505bf5879435a
8f0859091eadc086a86b399b8213c921d0243aa0f073a65ce4c4f12abe3050512d9726ae9bab49ebe0185e8107a995af2018
ba45c4ca767accf6b08fe355be3e6fc5ce84d89962f3bd7864478c98e3d0afdac30b3f246146cb2ce490ef96d475ddbe5e84
516f25018fadcfa31e60665aa45dfcd462471c53a0ce3504f94fbea9e0644037cef6099f2368bbe2de781008c47985a1d437
b281fa39e228b5573cd75f79bb1b9379f10be424368ead0d5ddf0bc6ee709dbe1108939cf7b2788546cee024f8b1df11c87c
0a7c322403bb73f261ad29b6bb49d7937ce872a2c0579a154e08

# For any positive integer k, a finite sequence a_{i} of
# fractions x_{i} / y_{i} is defined by:
#    a_{1} = 1 / k and
#    a_{i} = (x_{i - 1} + 1) / (y_{i - 1} - 1) reduced
#            to lowest terms for i > 1.
# When a_{i} reaches some integer n, the sequence stops.
# (That is, when y_{i} = 1.)
# Define f(k) = n.
# Find \sum f(k^{3}) for 1 \leq k \leq 2 \times 10^{6}.
# ----------------------------------------------------
# Analysis: brute force
#           Hint: gcd(x, y) = gcd(x, x + y)
#                 This equation means that when x reaches the minimum prime factor of (x + y),
#                 a has to reduce to its lowest term, i.e. x, y both divide by x
#                 As a result, f(k) = the maximum prime factor of (k + 1) - 1
#                 Also, k^{3} + 1 = (k + 1) (k^{2} - k + 1)
#                 Go to the thread for details about why this sieve would work

c43eef29999489ef3ce9385d7a1e2c746bc86a194d6f7c8e46d4ee171c46312085787c19dcdd2822f7340b0c01d8e448d4fb
b186926f00cc300215fe72247db3bdbbf9c7e995a32d9d7865ab9d45aa1145d4be962456071131f6c41dec12d94e3d487f03
3086861fed26058980af2419a9192e3a540fea3c31789f682eb5c43c0a052d4b5714682c13183353ef3a9d0a1d6753ac6cf6
0c57c96c885629574680bdf49ecd6cce3d2ab6cb95b5925bc403bb45c04c001edd670cace8f35eb1e21b518afcf4623b8cba
e9047a77b47d512de332f3b205858c287de4751259b322e589693739e87d553c0180e85f384e4a2ea4b49e6a38019635535e
0301ed7706467c2d2d7cc61df844b27cd75a8f1942c3013e70047387bf9dae11c3901b2ad47e5d6480769c28e8d2c0dd9194
a582fdb9fa7891fb47814601db3b1b41a9c837ae3a1852acd5e2dedf3169d5e6281e96e251d5ed12d6a8f1176d404610014b
a4aa55307d11c1a898be779dd11c78b7472b96b687cfb5af855cb05b4bf97100f7bd076d92b994c4d63925c6e1e91816765d
b74e097969c68d56bfad45bb6c72b20f6775143d3e306a3035597eaf296731d6eb88390ffb917cd85d03af639096a524e89c
2ee185e4aff178a0764bf54939dae0703b132fcba0f472a4b5550ab9fcc56c7aa0d3980c7fd1143f0879c6eaaa2a60b6693d
76ae3e379a032d5714ad7201debf28397c2d2d7c969de029ddde16dc4343761875bfbf2357772a14f044f2f07561f2ad6eff
9afb0d2ee999bd8dd32e10090691ecae6809dc28b37767b846fe328bfa67951e5eb0f228c56003f2b2a7ca1dad1c0424011c
4c1078ebd26b1187f14d1c87a70ff27a8f3ab1a6dbd8c0623d45cd67c460b3fbc18a872e274df42cbc02ee49add4a9351bf5
542f73ec9429c8b66348d5c275a4b62fd7000c14a449cd6b708de38078905ddcb8781266df2b09c332e72eaafedebaef5afb
4674480fbb7a5f0a8868231f010b7a7f52ecb4939dd8ca9e0290145f473f85cb12bf41bcb7b7fae43071fbfc628d827c4f77
1c099018f3a18eae4574450cc99bc7baa22e99a1a5543aeb68d57c2d2d7c820524d09331a3dae4db66c4d69432aa11dba23f
348b86277c78919e3fb9423059c49ab3bc1d4c9f5a22407ef24f8907ec567c6203818916a3b683d7f83d0343aebc45906d76
0837d5848049d3551536c22b343279299f80270e9f22136ede56617032f89c4b671dd9dc897e87a38a215317972e93f7d243
8d6edff89afed86f7a9a9eb06f5048dbe4899e8f9ebedfa6e5bda8a8884e2a98cf6f9d40105d49906faa480ba7d161d315e4
1570265c412b15d7de0174d92deaa46e8642e4e05df382d7bf38140616354db58993d6bfe6651a814d884a05377860426398
6e83cb7961ffd0bf3e2945970fb6f91498d3b3bd05eb60adf0cb0d94f6a176e9375e2da07c2d2d7c3a50a28d8d548702d82a
6160ddf34898a22d28d3c5b05d116f849d58834d0477efe3cdfe9087898eaafda8062294118d4a64d4fc0031b335b587a2d5
e07c68b5c5ce692f9cdd7673df2e023de55d62105ab26e47221adf6fe6b2f8a37e6051942cc2c5a4c3f1a811074d4d839aa8
0dda5f20976fcbe33d1c869171246e83564c51ec36fccef926c7d2c6396cf817ff1aa98501cf9eb9fcf6b3099f0908fdd004
c03e81eea17286926501f7998d238a7e80d0c1c3b3f9370c30b7619ee2989ed3100b9cc72745d80fab05bc22702903ec59c5
58044cf4eb2d46a3786abf547ee5b7c663eb43e943574c806528d34976f2aaffdf69f2b7e521df37f0d7f6a6aa5a7c2d2d7c
7a3673ff01d79b3baa57cb2567be0987b0331a78d9b5e21e61f11ead37f4a63448e02a4590784273682d500f8c4a4153b010
61b3f043db96d1e035192fa925d4b52565f27c075f077ea74c97830ed4d05023e3dbc697f532d8e6b95f2f718878eb510e71
39849b049d19dcfb473b04a5482283209046b46db56574cb79ccc85953cfa78d4fc62197c9be61d1f4d7298191f08c9c56bb
e9361fa7e2c0df522782fc90befc9aed23994ae472516186cdf77d114b5e5c8152c1e0c3a5c81da65c852eba68c0cb706779
09996929f782e6b8e46dff029e14fffcb549450e925d0f5e3e634fa83fa0472a1e60b62ac640c8c567936045adfee28a7648
d2b600449f71

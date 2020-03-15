# Consider a row of n dice all showing 1.
# First turn every second die, (2, 4, 6, ...), so that
# the number showing is increased by 1. Then turn every
# third die. The sixth die will now show a 3. Then turn
# every fourth die and so on until every n-th die (only
# the last die) is turned. If the die to be turned is
# showing a 6 then it is changed to show a 1.
# Let f(n) be the number of dice that are showing a 1
# when the process finishes.
# Find f(10^{36}).
# ----------------------------------------------------
# Analysis: Mertens Function
#           Hint: #(die turning) \equiv 0 (mod 6) <=> shows 1 when the process finishes,
#                 which means that \sigma_{0}(n) \equiv 1 (mod 6) <=> shows 1 when the process finishes
#                 \sigma_{0}(n) = \prod_{i = 1}^{m} (1 + e_{i}), where n = \prod_{i = 1}^{m} p_{i}^{e_{i}}
#                 If x y \equiv 1 (mod 6), then x \equiv y \equiv 1 or x \equiv y \equiv 5
#                 Thus, e_{i} \equiv 0 or e_{i} \equiv 4,
#                 which implies n = (\prod_{i = 1}^{l} p_{i}^{6 \alpha_{i}}) (\prod_{i = l + 1}^{m} p_{i}^{6 \alpha_{i} + 4})
#                                 = (\prod_{i = 1}^{m} p_{i}^{\alpha_{i}})^{6} (\prod_{i = l + 1}^{m} p_{i})^{4}
#                                 = A^{6} B^{4}
#                 where A can be any integer, but B must satisfies \mu(B) equals 1
#                 Therefore, result is \sum_{B = 1}^{\left \lfloor \sqrt[4]{n} \right \rfloor} [\mu(B) == 1] \left \lfloor \sqrt[6]{\frac{n}{B^{4}}} \right \rfloor
#                 However, calculate in that way is very slow and needs a lot of memory space
#                 Fortunately, we can calculate the result in another way, which is
#                 result = \sum_{A = 1}^{\left \lfloor \sqrt[6]{n} \right \rfloor} M_{+}(\left \lfloor \sqrt[4]{\frac{n}{A^{6}}} \right \rfloor)
#                 where M_{+}(n) = #(\sum_{i = 1}^{n} [\mu(i) == 1])
#                                = \frac{M(n) + S(n)}{2}
#                                = \frac{(\sum_{i = 1}^{n} \mu(i)) + (\sum_{i = 1}^{n} \mu(i)^{2})}{2}
#                 Since \sum_{i = 1}^{n} M(\left \lfloor \frac{n}{i} \right \rfloor) = 1, we get
#                 M(n) = 1 - \sum_{i = 2}^{n} M(\left \lfloor \frac{n}{i} \right \rfloor) which can be calculate at time complexity O(\sqrt{n}) by knowing O(2 \sqrt{n}) previous values of M(j)
#                 S(n) = \sum_{i = 1}^{\left \lfloor \sqrt{n} \right \rfloor} \mu(i) \left \lfloor \frac{n}{i^{2}} \right \rfloor
#                 As a result, this way is much faster than the previous way, and can save plenty of memory

a86600ff7195546e75cfc55c451f0561708807d0168640125b6ce9e6268aa3f060ac519f1e235e1424083b3b469a67c744dd
096a64bc89259f6d8a132a55a1888285c9cd61c68c11a53dfea2c709f04ff881d0f5b2f2e5dc2a44e97bfbd688ca3b554d0e
a77b225f40cb97dd38727194b18359971d1e60c37bacca2d50cabc2e2dc390b64787191306efe288558d5ec50736f0ab5a6d
7ccac78c79298d3ebe61adbd3cba1ba4947320f2b1133e9742534ba03e78719b31282a155a470dd36929f9860f95f2afe6fb
0426382c888a12eae39248df2e395a9244b815ae2e38e6ffc413f5131e26df0643ab69d25138600657e2c49c8cb4db1a8cae
ce80ecdc1dda7c2d2d7c41bec6c292e749165b3448a12dcfaae58ebf320b95b226040fcbdc1d89f999e075d38d6310767097
9bbd4934bd7a970c21d7cae49c3bcde5a235e26f192dec532ea3ef05549a769584db18df9c7db39e90554dc6cb49cbbfd6f7
c4dd33ab15f372857517178ed9669d11de48a32598171c7db9808710366cef35c3cf803b06828a33028b69f8a3ca706ef425
4c6f46783acc23a8d82b9efdadf8fa496d4b7c83f28da871af340677c2154738e6a81b341bbc8fbd6364ac890ac9137181e1
b426a1ed38fd5057d08fc2c548e8b3f32a399df13fe8dd94fd18cbf06435063812477a3bc2d5db89c0c749c7ab91bbfe72e3
41db8128977b8f0298258ad97ae8b58a7c2d2d7cac448bed8eeb4332ace95844f4b3fe2cf33fca7e044c15044f4c8be7c8a6
0aab2ba9375ff2a2808872f8a95ce488de425fa935d6304181fa25278a3a6c3877d981e5f8347aba3f66b9ed2cd51b2af903
2e5d2b5a44361a6f53725c1267a5a586ade7280c68d2ae59f54947d3d889d3856403476cc65f46964d5f315c07593aeb6dae
54404c33757b8189216ae13ec6520df7cd839a148a66b573887e6a0f1a55e4f3b1c21ce9c32a1194e858b3ebddc2301efbc0
9bedeedaea0745e0d4ec8c3a0610567f49edc7d919fbc6334116e49e5a25e4fe4fb9fa3247672e1a223e588af09b003b76b7
b2cb3f1c9912e3ceae6b067a911576bd955b65c68028fe9ad3ed7c2d2d7c3d1452976484f6238eb9acb88389d8bd58dec54b
27b088164b50f7442f7b71b6c185976d29ca04c13ce52ef37b4ebe1c8cfc6e134bf061b7a89edf37f37997a224e049e708b5
53a0e90278fd972f7d8d974bc4db81d4e00864d3f13063228586b3e953aebfd37c6e511d73faec1614565c4e3fbd48151a6c
fbcf6519071680b7af27d20e4117cee67900fa4bc58cfe4062006a51e9120f67ec9647b28ecff0110c4ada2e636bcbeeb315
7a54c1bd9c63464a25675824ec3b17be533a7e73d18b5528b02487b23da791a312b3f696b63db75fb9612556d8056d6dd691
8edc1b427f3e4df9c341a24de949c28314aa824346a1844451ecf883f03a14b35ef312eb7c2d2d7c944d9be9e80b914a6f3c
d07450fadb7dc1cc35adb0207f7029891c59539b8671f0378065c77e88668b9718d37767edc69c04e4b1ecae14384c2e88a9
1049e5181ceb3596609a174ba7452b96f06cf9e05945719e5c6d56877ad74d0787d01273638bc3f89f105543462dd6950f9d
15f5f169a8fd39352fd25ee1ba55e90bd6f2d8c644b3a52266dbff0c8e181fe4e27195567bfd392d5882286e97b8ca99fc6a
8ddd9e9ea23ffdc786e42269cb262a94eff68f074e4c54761e7ff564a2027df8e774649caf41bc463fa596373c0d62f284d8
68717eedad597aa9f8063c80dd621d5e91a1a3859cb160608654f8645d5625a3528ba3d0473d44bafa7d52e81bf3

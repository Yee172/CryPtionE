# We want to tile a board of length n and height 1 completely,
# with either 1 x 2 blocks or 1 x 1 blocks with a single
# decimal digit on top.
# Let T(n) be the number of ways to tile a board of length
# n as described above.
# For example, T(1) = 10 and T(2) = 101.
# Let S(L) be the triple sum \sum_{a, b, c} gcd(T(c^{a}), T(c^{b}))
# for 1 \leq a, b, c \leq L.
# Find S(2000) mod 987898789.
# ----------------------------------------------------
# Analysis: matrix multiplication / linear recursion
#           Hint: gcd(T(n), T(m)) = T(gcd(n + 1, m + 1) - 1)
#                 i.e denote U(n) = T(n - 1), then gcd(U(n), U(m)) = U(gcd(n, m))
#                 In this problem, we have
#                 gcd(T(c^{a}), T(c^{b})) = T(gcd(c^{a} + 1, c^{b} + 1) - 1)
#                 Let d = gcd(a, b), then
#                 gcd(c^{a} + 1, c^{b} + 1) = c^{d} + 1, if a / d and b / d are both odd
#                                           = c % 2 + 1, otherwise
#              => gcd(T(c^{a}), T(c^{b})) = T(c^{d}), if a / d and b / d are both odd
#                                         = T(c % 2), otherwise
#                 Therefore, using matrix multiplication or linear recursion to calculate \sum_{i = 1}^{L} T(i^{d}) for each d to get S(L)

1894da6fc83aac7e45dff85995a0d663d9e8b84fa2d4df6ea946bc10bc52012e6c2a963e6eea102c1ee891c5142a51fe11a5
860e1682cb050aa6f91798bdfe6382770fe8b119c7569bad43d52b437db02d96ad361b65afa2058db1c25c7848bf677dea45
8d857ba3b51beb350a4ddcb2002c67bc67379ad4e8e1b684e9570b3d795f0738725dfd2b8b41845bd77cbef7e27234b991ff
d98496d599ed840cdd94fa4d490b80350dcbeda7fd3cf8d63a8845bb28f7b0927cb4e77fa34a97fbb4a2e8aeab55f54b4259
1ed1b7f1329f0dce929f302bd4486d9a10c9be092af2692ecb59054b1a0d1f7b116a5affdf3b580a5be4b7fe48c3ca00ea33
e6da751706917c2d2d7c00f3e7cacd7eb28d2e31c39a34c1ae7f26a5daa3d2e8bf27d054856dad86035d6ff0b283c792345c
e0da7d633faaf2631908da32278f6098afd5a40f2b367e10ff5438dce16762f937ea2cbb227dd1e76dd242bf488b72dea1d4
25e5978073fc30c567cb77513db132215ac13e45e0107182826c0141cd9cb133b5ee28261758d5e61e6500bc5f4d119ad7fc
c490a92fd0290b461807800f340c61d8d00352f80bc4c723a806f3316f61aa10950cc88b6be85eafd7e7c84d76c461280c01
44aa742b833072e3d1b720940ea4a68f1a6457269ae4ad754592e369dc0d9d64c8c80826b2893d09108589c7095bd1b53779
4128f5c6c3dbf061c393fbddc5040a367c2d2d7c8059486c077a6520f0da5f8ef1346d06761d0389c3d94b00e6975d1245fa
2530b2a1dabcc292a50dc3aeb75b22c3fabad6dd0465c17da16e67fbe50c0b3bb1a1d38a417e518d1c24e1d178644f542184
b0f148fcdc870f47389692dd2f2ee794ae77ac23db1679349dc4f7a3331006f9009f9efe763c4d53ee1b671489e552701eee
ef282e6843c869c2b52d1bcbe479e8a85b3813586e8396b806928ac9481987788fc385e08042a9baa368d5488fd164fe474f
550cc1f8bdf53e9c3e95ba39b1dbff20892a80831c5126363d88326728a207197e20fe5ef58cc57845d9c4711330c98186a8
ffb4db4385faab127f408095d5c0d2c10a8de2d3230741a8bff07c2d2d7c004ac5fb0209af928444cef91f3ac9e38b5c56e7
0583e393fbb92298ebf9c9d0f11be35e0c6438664f341999fbbbd5fe08546b066ed8a071614424fb2cdb5b3af3441d32ccfd
a127568229de7ecaac80754f5b0ce8ae31f30ac27c9e54a6ad4281319accd39a4f1b91a74eaeb2981fa871bb93d154bdaf77
7944ed6a182ad6e1f94cd8b83124dd631248b03a93a044d1117597eccc715df4708f921fdbf521efc5705d96829860ab0a47
21a01bee3fd908f2661f8a4832eb9054b430b7a3d78a11869cc553e3d55caee343af37ca25bda7aa535ce7c64ef8729b7a6a
8550d8e4728c1a1a780f1ce07fbde5a9381e1d93393ce370c889ac20618934c18c6b50127c2d2d7c44baa3ceb07e2faaa6cb
3e4fcb6e6d90487e794b228d9a4c4e3917ea8cefcd712253881e153c2a29eb792b0e897d672286e655761fbd262ce026cd3d
d819fa1fa811b1dbb9a92f2883261298cd5f16a16d6b4e1672059f56f8cfb6a840bd16215ed1d436c99b2e0ffe7ef70ee225
35ddac5ae6b5c51c287f8c49b082acc75d9c69dbe29162113e2e61f8a74312a26034db8afc141be9f1b94248a65a54ab0923
2298e8845e826916e56f0f4374e578980adc58c86bc9f7e5497080fa228401fbc987e4ad1d38ae8e2a34b42947209c2dc6a6
f5310bb884de2cfd554373b2ec39235025b7ad901e44b0beb32ae8cdfb9ece5dde0fddd768b40da5ece1dd1bf168

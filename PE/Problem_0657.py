# In the context of formal languages, any finite sequence
# of letters of a given alphabet \Sigma is called a word
# over \Sigma. We call a word incomplete if it does not
# contain every letter of \Sigma.
# Given an alphabet \Sigma of \alpha letters, we define
# I(\alpha, n) to be the number of incomplete words over
# \Sigma with a length not exceeding n.
# Find I(10^{7}, 10^{12}).
#    Give your answer modulo 1000000007.
# ----------------------------------------------------
# Analysis: Stirling numbers of the second kind
#           Define i(\alpha, n) to be the number of
#              incomplete words over \Sigma with a
#              length of n
#           When n < \alpha, all words are incomplete
#           When n \geq \alpha, there are exactly S(n, \alpha) * \alpha! words are not incomplete,
#              which means that there are \alpha^{n} - S(n, \alpha) * \alpha! words are incomplete,
#              where S(n, k) is the stirling number of the second kind
#           Therefore, I(\alpha, n) = \sum_{j = 0}^{n} i(\alpha, j)
#                                   = \sum_{j = 0}^{\alpha - 1} i(\alpha, j) + \sum_{j = \alpha}^{n} i(\alpha, j)
#                                   = \sum_{j = 0}^{\alpha - 1} \alpha^{j} + \sum_{j = \alpha}^{n} (\alpha^{j} - S(j, \alpha) * \alpha!)
#                                   = \sum_{j = 0}^{n} \alpha^{j} - \sum_{j = \alpha}^{n} (S(j, \alpha) * \alpha!)
#                                   = \sum_{j = 0}^{n} \alpha^{j} - \sum_{j = \alpha}^{n} \sum_{k = 0}^{\alpha} ((-1)^{k} * \binom{\alpha}{k} * (\alpha - k)^{j})
#                                   = \sum_{j = 0}^{n} \alpha^{j} - \sum_{k = 0}^{\alpha} (((-1)^{k} * \binom{\alpha}{k}) * \sum_{j = \alpha}^{n} (\alpha - k)^{j})

0e01d9cc85dd65f703d674222fe4f479cb1a7bb83ab48f653b9d99cd623338ec632552fa2b382a0645ac8b71c6581f447886f837571c03ae1a123a54297d04dc8e012ce900dd32f3b68c41e3edeffcc4fd3d1e62551d94060886248afb83e8cf4d8bf76442ca3c7d87502d74a84eb6fd88d17f5af278797315dc0bb4600572335e1d48a0e37f0358360465c5fc386ff1235457e902f2485047eca334b4b31e28d9e8437f9f1b63cf7aabf47415fbb6ea1d55f8363c2ca13a7822c2f2b87ddce146eae3efebd624bb6d50dd061915639a81ff164cb3eb9a1607b1f5b99698317622d251c37227b5d84af554268b8166d787e24dad2c8d533297751e475cd610b07c2d2d7cc223fc8b5fbb1ac2c8fb200210d7a6d27c8288b3615f223847a7a62bf35ec272f447de9c10189a778d6942da12b6454ecc57b6a5073c799b93caef6ecda8d18e7cf77ef5d04f0b402bde58cbb27290853f989a32fe10286dd0d0c197c059a9bb232710db98a5cdfe1140bfb0613827d3f9ac9368f8b865ef855018cd492497b22c60999501eac3e0f834e7d7e195ba002c75d598a0b52b895ccd5ec76d73a8809bf7ac42fcd1849a49d07112b5e95f3e0d986eb0ce0db505a7e41912e0bf757849d2fd698d73edad52a66c2aa70fa3c2b39f4debf2c3f70af29dc7ee28c6bd455550053c5f28fbab97aaef73e7142ef82dc0dde62243347ebe6c4b61f082dc717c2d2d7c93f9e4aa57933956aa3330a20c831a3dcd296d9059bdd71cf6bf44d230370260feb5f2dc2ce8429ac45ee5ef8c5c3f992e8b29221b889e3822fbc885da2ead0b7a8a383dc199e627badcec390e32f6541c9e3e9562b343ae692d9db61168f70bb9a0f874521a7dff6734416c3e5bad179d5aee655a792fc11c0b9755f2ae4d98eaeab57ca7324f51ecabc98046e9ba530081a5bfaa562b121d7924ba782cd2d1375bfb84b3f6458184e6b02a9f515b9497a3a2d2a149d2acbe8cc698bff75fec4b46eee661be0b64712e5d9498fd57beeead8d2cbc7852f2f529b6482d7ad62102df5cb5a5bdd155be23d39f3c7eed84d8b6994e4f3281aedf33a73dd833f4067c2d2d7c993c23ae1dd2e4d2d5c643775f5da2258995a6bcd1c5bee957b19c4da452f672495aad372879ed4685e5fac56a6d23493fbca8cc8829e01b1858baf18132f4fcba061beb3d1f10d02ebb2613ed3225bee4522973eefb27e4217f97009d0472dda44b4efdd3bb4747e353b8b7f2d0820247900a280ed668871ee8ff32a7de3506322a69acce8afeee1d543b74834ef672011fa5785d49997fabee66dc2a6c1f9ed2c5e29bf32270e19be6ea8c842b33a5686882a7b0c931c907854bb4f9af3986b37c5ccb8badbcb6df927b4a5cdac0ff169563fafd5cdfbaf9588f247da62174115b3af0fa86e14f8a58903b0809e1eeace23999526465f69f284b0216ffa7587c2d2d7c2d7014a991eb6fa007a20cfd232a148c74fe707eb1a65a9e396ccc3398bc30465daf65f9622f064ed25e50e87b056fc35255a87f1105857776733e890c39f0081b6aabb2c6b3f4a4a83d2ae6b923218b0f3881b8de3e00f5f0446485c734c3b15b7167d6a5806526c345e70ff9df4f4edae1032b22b1de77450c6414adce929509f2528e0a603f2969522e7569d3ed710206f6fa5dfbe665f17e343f3bc15aa38ade386ef287ff514a694d78c290592e044cd41b197f3c6774cba1af5aa072f4c279aee46cd2a04b0c510cf0259e20d34b5b3d8317d9fd678911c7ca312f8a25c09086e6868575d689b840ddcac855c2b55c4572ca9be175c9d7d0726ca9e907

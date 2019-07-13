# A hexagonal tile with number 1 is surrounded by a ring
# of six hexagonal tiles, starting at "12 o'clock" and
# numbering the tiles 2 to 7 in an anti-clockwise direction.
# New rings are added in the same fashion, with the next
# rings being numbered 8 to 19, 20 to 37, 38 to 61, and so on.
# The diagram below shows the first two rings.
#        8
#     9    19
# 10     2    18
#     3     7
# 11     1    17
#     4     6
# 12     5    16
#    13    15
#       14
# By finding the difference between tile n and each of
# its six neighbours we shall define PD(n) to be
# the number of those differences which are prime.
# It can be shown that the maximum value of PD(n) is 3.
# If all of the tiles for which PD(n) = 3 are listed in
# ascending order to form a sequence, the 10th tile would be 271.
# Find the 2000th tile in this sequence.
# ----------------------------------------------------
# Analysis: brute force
#           Notice that the tile not at the place of the lower bound or upper bound of a ring would be impossible to achieve PD(n) = 3.
#           If the tile is not at the place of the lower bound or upper bound of a ring,
#              if the tile is not at the corner, then there would be two 1s and the difference at inner ring and outer ring would both be 1, then we get PD(n) \leq 2.
#              if the tile is at the corner, then there would be two 1s,
#                 when the tile is in first ring, we can enumerate it, which shows that PD(n) \leq 2,
#                 when the tile is out of first ring, we can see
#                    its neighbour at inner ring and the neighbour at outer ring in one line share the same parity
#                    and the other two neighbour at outer ring share the same parity,
#                 which implies that PD(n) \leq 2.
#           Then we can just enumerate the lower bound and upper bound to get the result.

91ae4ba3764677d68f75bfd94cc56c64a2ff0c5a7ce131c7992cfbc4a908ef14103668830c6337497526d3c5ee43b9ad18e0
68ff7f163abcf6dc1d7747f045a06c8a35a85d716f28a88bfd91ff82fcee73b1ee53697f2e05d959f8a08f167acf4f4f6f04
d3f74e8c68ba022d5858e50ed3aae3169eb233f9ef1b9d0ff817f2c3f4b7367b807c2a4f26d9851360a23a0081c1da2a633a
06982bf2cedf73874129c5be6cf90028fe58ac3ec1e8ff2b083b961b72306e5a3aae71b5d351a7945fefe677c1a90fd2c9dc
4c7f58d0e821eb291322ea84970ee414cae80ab6aa78855083d0384e9146d9b4c6395f45f02271ef23c32a84acb7c140cc29
e7e2602a90ef7c2d2d7caa31e586b57af5381729e6053afb66154b478d69c20496b1e62b3411934d28ed3f89c9f3a382750b
894ec6c1ce37e817c0b9b5a5e66890adf79e77904439a519b2c3eabd9e7aa02873043e631ed4f522e80d10ae3b6ece5f5cae
1ee7cd51968e4dcf57317ac1697355c12d5296305c2632f64fcceda03cf7e15df1378a373e31cafd83d6c7510cd032a11f8e
3173e6daf4caee87a303055c2f1c3abba469636d233c1276ae74b14aade776422dd5b6db74e7b14b96e5a77184d6f3db8fc7
6eba9e6cee92c56504bf3ed232c4261db2e0e5d43f85178b8b0136a7a733d57ae1306db0356b67e09741ed69ad0be830bfaa
0afeeae86f4e1cfd28c797f56334aef17c2d2d7c4e659ca800f133f07f9f8fe7d6de9c526ba31ca70b610ae6126cc3a8a389
fcc00de27cb11c7c346709e6e1c2a7c205ff1f055e9bc0bb1a233de1c3f709f83886b019fe7a503de103f2520392cb05f220
127b0fa8d5474bb562bdf7fb49d1afc3a0d82d78580cd8216af7ad04833c27f4cc1039866ba01b00b5ff025b37bd23332c84
6f6f7d092c726f861e3aa0c033569fe4cbc2ec68e7c58d53dfc888738ee29e5e66c0415242cbe2e1e32cd1ab9c5bdaa378be
63da92d4d36ba65a4c163e63240f5d5f500ca159236f3cdfb5dd72c4a073f05c5eed006c1d7f64a9a4bfadc9b898ce40fd0c
04ffcef243507f23b1b23e2dc6b80ee3ac6739cf997480ae99617c2d2d7c5c48b9811ea622b02c2db62d0081bcd4cb1e9446
c97225ca04246abea44d21be75b077c3c44084ab35f30e9aa82064fb2f11c499bce46f345b23da8b475bbd17d23cb5aa4624
fdf81e098f6cb2a4dd2933899165bcb61ab130c303c5eaa3b0ebcf5038b7ea0e3b44c58d5f3b266c809e02642cac9ff6db0d
903ea1337dfbed070920de166fb34476523f7bca3e7f009ad83b8b1ff1b87dc032135174493b0ca19c87d8b7aa1c9342368c
6aea6909e23e03f011577bd839e7fdd4ed41b50ba3282900adaf3314f3e6137c2d509128c73bf95581f0723b6cefb7a9fea3
8340b8d0e6df29f7568397676caf899a5033317bcf98535949dcdf0f58babdc21ff793e67c2d2d7c5fef5945ed5fa95e7ca4
1620706ee66b22f8ca33eaf10682290b580ec16e500aa1356ac900d4f715f6ec85d9d1d73819c2d4777f3a8d1de887c25674
43683e5ca785343ee8d3e37c10461bc4dadac563a23f30a07581919f5201c15bbf38ec4a420765e522493c10bb488eb996ee
0fa0ee67800d9458a793642a8431fa91ae60a7e8473cb1e568f901a47a6cf572a6f0fb96033eb399ad361d7d03a1fe1b98e9
b4b6602c293424a6aa87f1df22b3a75231466f2b5a4d951da3717e3ce19d9aaf024a278c0eb355117b3179b590c88b1db8c8
94be7519ee17ce1abc30dc16e16c66382cd5b5ce406bb4813adcb7129d662f448b753bd1dd465455bda7ca09e8cb7c2d2d7c
5898279d54514b84f65aca4c63b1dd487bcadee628bab5467f61285bd70a24f07a1372d5b4a2ac6c68f14ac9723ae38420fe
8e96ad38c25ca5c76f30d5434f58135d0ab5f94335662599cbe6769190ced9b6115b4314fcdcd0f747d71c4a1bfc37c5105c
3ed722a8a9a9e68c377147e441bcdf215113973acb56362cdcc39dacd81fb2effed1cd0087460498adbd0e4cba704ecf6cc5
5b7bcc19d6e60464fbb140edff048d6b708c051acab5ec2e06959398e0ec86474d5cb47dd1a49e705053f95b626e714c72d7
cf063e141d9d9dba1bfe95789abca9102153c622e0f78c6567a6bb57b7e9ad6b7c5a8a45e66075ea662caea4a8bb5564f51e
2a606aed25bf7c2d2d7ccc7b78663d31e54a3a90c86890e07350903f51af738ec743a6cefe249a45ea9960d8c95d89632c56
034614b6661159e157b3d6023868b879d38a4e75ce40123b1d945a1dbbfb5ba0a5383fd16becce26ca134cb7093e498570f8
51917dc7c5a7beacc5780b60ada34818caadc4f739ea76bc27738984b70a7b40208fa428e21ab9cac7c1cb1b62138b1e17ca
5c71f35ed4c6ed6fd3b2c54b5ba6aa3a3ff801500eaed215db58053d6d7333a4bb01d919a0aae28ef8f51acb21e67b908593
c6b54888b72d6815d5a226027d3612cfb4027fcb01a7aba1cd22420fc0f7e9912ef9dbc213b2de2e4fc304ae27749b40ba49
97061737b407ebaeb6f0fb110cd1663f7c2d2d7c8a3e4c4d330a72fe3b43875f1d794c362d14d22078ed0ee449d6118f9e52
fe2fbc9f19b2138915776d3a4baecad0f7c6610834e4557f4c580f6b7c744f1faad26b82aeabd8ac0037a101dfb9b2191861
e580083d413133454cf9ce6e512d4bdf536208b1202c0958dd67768b0b64f2d1dee94691812bb12529c352e03c12d1cbe6d2
8444883f857b9e947779547248938d6adeca8935f942ac7078f59857f8e1204c72b9612ae22d68f34754f9239fa209e3a5fc
ccb959e1771407a047fb0a5cd7e2ec976b3bdecbd4695533122303829c41f7bf02e13af8a543e37781125caa2403126818c4
f64e72b38bb98d761d2a272a464f8fb89eb61b83d50d08e5c90e7c2d2d7c5bd83548de9b75413313b9f895b05d1806f525a8
1489abc46da2acd80c0a64f336c9d1146a849cf9bac8b8fbc0983ec62930d922827a2af59a1489af2120ac4a6367195c6f01
e3685d911ab1e4f35b757797559286d85c0e034c02e0d0b85a27c65f84ad07c6ec8e6ce30e200bc7006bff0346f6082d458e
e7458eb7eef5ee08ed4615e2c3609167ed64dd6e6fa3e8bac1fd4568092dd5237cd400bd1508a0061229aad352cb7f7530e3
1639d73909662220aa253e91567e74e3d45d6a02dcd60f964b1e3a943e1d7205be7dea0ea78d726bbb150ea0e99c9cf804a0
ce768a0e686cdb9d49582903472034125de5c4d8f2ea2e2baed6a0d9e6285b58e1dddce3

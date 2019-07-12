# A particular school offers cash rewards to children
# with good attendance and punctuality. If they are
# absent for three consecutive days or late on more
# than one occasion then they forfeit their prize.
# During an n-day period a trinary string is formed for
# each child consisting of L's (late), O's (on time),
# and A's (absent).
# Although there are eighty-one trinary strings for a
# 4-day period that can be formed, exactly forty-three
# strings would lead to a prize:
#    OOOO OOOA OOOL OOAO ...
# How many "prize" strings exist over a 30-day period?
# ----------------------------------------------------
# Analysis: matrix multiplication
#           0 0 1 0 0 0 0  last is A  without L
#           1 0 0 0 0 0 0  last is AA without L
#           1 1 1 0 0 0 0  last is O  without L
#           1 1 1 0 0 0 0  last is L
#           0 0 0 1 0 0 1  last is A     with L
#           0 0 0 0 1 0 0  last is AA    with L
#           0 0 0 1 1 1 1  last is O     with L
#           Since the third row and the forth row are the same,
#           it also can be reduced to a 6 \times 6 matrix with
#           the last summation use 1 0 2 0 0 0 weight

4dc895c6889e2ff1fb0b97b6cc2003f14533ab1fcb742c97f0482ef07aa17176605f2ca3377b486e34fde6d30bee550a6ab9f3d9eaa9a38812cceaccfeb6bca52e3c02ecca6f44e32218dc85d516a03743f08aeabbe0d808b43b4cc7dfbbb300022d6cb7d23d3c7c0c08c3cd6a7a702c85089e3beaa0458012ab963059a927cd96637439b9c059905d62a6a89d70b3f24221da5ee3f7071a8ae229aaab0771b3a3b976deb4e03976ee4111b5f9bb2db6bbf13bd701d8e8260de568e195c6b63f5fe92b5eabaed590c2d8a854dfaf29f88c4d12e1296ff5826521f193b81a7e4e6812456bc5a65dfd40cc02c2fe0100eb664a4f9f3f5137f1e2b75af831f43d427c2d2d7c62cdfa7af64cdb7702c01f51e22ea349f741124be41865256b006366d97aa1e436847c38cbc5e0d051578649c27e54edb6248308ddd72b611d449e8664efd1eeeec0e2e3122c46c252e31c4823998766c14ee9e1bfa29e90f1031123657c9bc851d6784a5eeead2d770bb64b3e424d4557b6a3d6ab6dc1b3985207cbed93030d02fed86fd129eb619c9fd77ae3259ee316cfb368b890712979de674fdc9eec1fbe8bff0da18b09e3ad5e37c58dc02a3188b9a28b782a6d63cd187188dcbec364da07afd4d753b369bad1985d7c49f171365f6fe5a6d8936fcb217a4b541ec1c5f704e7bc59c124cb1795e8f1da656a064f4f72b9a2687b859d3cd861bb5660a27c2d2d7c351dcbee469da82bac3218ccb2089c84040c4d1a5999612207fbe6c3ab5af4afbe9ddcbfbf1c4fbbf3f8fc5ae5f97408d4cadbb48b0dd313f031ebc5b721497fe921d17dd488c5cd82264a2d73d6c33d7a6f42e6d20c23c511c64f6398a60fec506ede6d600462c39eabbad8a484ec5843f99a7b636b44f9c3d789d699b9e57c5f88f3ee6abcddb2f406d74b1d927d7bc83cba4708612c380faa6a59b5ecf2fd61fb660618204590a80db6efde372ed448a21e69b88e57f122d9d3328d5c90c63f1693c964ba0ca5c1f0253b12eab1f8ecc0b15e24bb1b0d4f47c551211accdf0147220035853f09dc489f13d52bb7f1e903346262db2f54221851b28328027f

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

9bf26a04bec1ae899502db756bd2006718fa61582aa3e4801b60a6ff0285949313979d363e517c0651603aca04501e580324
ba564c4adae8454d8df5325e3df0076571cd487a5889ebe3271871bc048eeb8de69d7e061251f3ebedcd888a2cfd81d3a2e6
3e443d8f8aa5e36de9ba5a589f074b6002f770472468af72caf566a6acd12aaeb80c48523d5d0630e91d1b5748569fc4b0c1
35bd50cb39cac2723c8d3c2cf0c9f26d98248865f36f046a407cccd609fbdf68a12511405c05aaed4f5d5a644e5d3832e3bb
a83a399483b8dba154e710e1b97f59ddb56252a3f98400b29280bb76870846bfdcc8375f68720885fb59cf4590a5fd0115fd
aa4783c963497c2d2d7c232ab2a79acd749acbfdfc2b0f64e19941a1dc353b1a36bcc7c66a86e0da6b4c2e36f53afdbb4541
1495bacb04513533c4b74960de4e0350fa7e074648811ac34704c3830a054ef814c077ff419498c228aa0f36597220779998
b965d17139507e74464a1b522984369eb933bcaca9f755a8184a45acf382b3d58e46ca57e147dbae8f632d6f10efb8b4afc9
7424e9158361cbc1ecad45c8916fd5787bcb8e6de79f1fbe74ca23cc3196983bcc64bbfb6330a0e6a769e4c35d5082bb49dd
c9652ad16deda805f159f591e00630d1878756077fc2740f5d14610ce104322982b1c4f5c27e0ac3cac4ebae3317bad0e818
55eff4d076b0030764cb1b16446481317c2d2d7c18fc462c95e91f2ba093598e24dc06d48b1ba4169d8ed16f44d8c74c4a07
96bf2ff3662e90b2d9903504ae0009b2731e157ca618eea90949d6b67eb966197ac0a9999554b2aada174659eb84c86f943c
743a3a4016813d2246c78e0900869ef870becaa634571cb581c95f641d82714e5e88a94f8ded16a33f9e6edee7c13a56ac75
cdf3488429c20bc0912956ebe19ac00334baa3c17926dfa37d80e1b7ec6cf66d1a3dd553d035bb3d6527c186b8ebf184156c
d37e200f513ce9c25202f24a0ab095653c7a4639aafe6408a3de52272788cae0350d1d89dc86fb35cd6961b3fce5167a621e
19c9914074ef92922ebc6d3a8dd6e693f8f4cfbb1a8aeacb8eec

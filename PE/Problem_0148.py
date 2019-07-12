# We can easily verify that none of the entries in the
# first seven rows of Pascal's triangle are divisible
# by 7. However, if we check the first one hundred rows,
# we will find that only 2361 of the 5050 entries are
# not divisible by 7.
# Find the number of entries which are not divisible by
# 7 in the first one billion rows of Pascal's triangle.
# ----------------------------------------------------
# Analysis: fractal
#           Similar with Sierpinski triangle, only with
#           log_{2}^{28} Hausdorff-Becikovich Dimesion
#                 1 
#                101                  /\
#               10101           1 -> /__\
#              1010101
#             101010101              ____
#            10101010101        0 -> \  /
#           1010101010101             \/

29a68495a2e76d4ff9512a8cebfe1915c7ae3901548cf44e414da81af3a29c8d5c60ff777f17b04eb1dcb7783478a9df49c0f9d3d4eafca3f30a5c2bad72f8aa04506d2af4c70b7394015adf9bafe102ac00e1923f3bdef9e70bdbad64584ea18b516d425b46f3546d4a015cb1d3928b363820dabb3090bf8d961439f073e62a9a2ce8539eec7aa060f785a34b9e7d076f170f9a374edb5099aba510d2b7c77d6168e17c8557621bb4bcbbe2acc88ee4f0dc7c6660f0a0fc0ceaf8225b1ced81cefe1cead30d0e7bc3d6da9253f07603a1c14575cd254c5d7a29f419d0e04ad338ce5c3e7ba2cc39442e6107a30b88900f9c0596afbe8b9fdd3accf4c9296cc47c2d2d7c9e91909efef4338d772bd6608235abdb68a3c26c09d5d72d07b7dfbc20c02f0bda0bfd69e2350c1cd354412c6aea4cbaf3eff60fb337cdca670e4a60a09f69656ea82bd3fd3043f1e4e13bc32c53e8b5537ddef5d897a58ac5018f01f4fa978a7c97b162932fbf56963653feb46c3d97831e68b0547ae68d25f033395ea2d483647ae7a6d39b0dc44c5ae311dafa2eba0e84275aad7cc643d7c389dd7bc6e45c48242f3888c47197a281274d1ace873577a53b8b0b4b4130ad4162c5eea47fba95df6090144b232e7dff894fe18c681e2b76997890ab71b30348314c76d1bb4ce7b882531e7fa8663a63cd87d436199f0457509138fd467da6760d1aa8b6e6b1

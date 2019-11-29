# A position in chess is an (orientated) arrangement of
# chess pieces placed on a chessboard of given size. In
# the following, we consider all positions in which n
# pawns are placed on a n * n board in such a way, that
# there is a single pawn in every row and every column.
# We call such a position an open position, if a rook,
# starting at the (empty) lower left corner and using
# only moves towards the right or upwards, can reach the
# upper right corner without moving onto any field occupied
# by a pawn.
# Let f(n) be the number of open positions for a n * n
# chessboard.
# Find f(10^{8}) modulo 1008691207.
# ----------------------------------------------------
# Analysis: brute force
#           Hint: only the board in the form of
#                       x E
#                         x
#                 x
#                     x
#                 S x
#                 is not an open position
#                 We also need to notice that the form of
#                       x E              x E
#                         x                x
#                 x           or       x
#                   x              x
#                 S   x            S x
#                 could lead to count duplicately

6d9e52d91086efcc8d083e4f04d4e0cb5a212e1baa92c22e0e3706104e5f1313d24275a3bdffddc6e92ef8fd583de2202667
9fa05baccc11c87662861e6b4079d60451c977733eaa339ad5451b6155e6051e5a357b85aefe6fd83d30f5863062a0b3e450
33fb6908f2dbb92df8b7c41d5ef08411f9d6e3522c1724bb3ea636862ad784371ba0c948d7bf7664a3c9927747f69ad0233d
987ca2f177cd468d5c44c4aacfc7a38cee35a2d05deb6c42a103dc77b50bdb2cce7d70fa1176f5b95a1440b39785005e1579
515b0154f54e169b01c62dbb97f7dc96c84cb73cf0c23e4e644f8b7aae73e37217744d90582896ded159f07268be42fb921b
cf3b41e464907c2d2d7ca644d9ef2738f424633e3350e6dfb646ae9c658057e4fac7eb910d7b290e86ef32811abfbc081ab2
3ff888310c12f38a39573a643d59958796b0e081697a585c3f89c390afd24d72f8edcbc3d85459e143eb1f2fb9682b8bf30d
e6a293851e394b0a8f0c624f113c328fe2b95dff89e59591ea29afa2b30b624b66073d3631ed3a5c3c2f26f33987bf1c6fd9
bc19f95c1f014ac8e38c179a12644d62a755e802c6edf9565aafc16672e3e9fd052a48d87d3169564c372b42dc2fd8142ad6
4ed2b145a167921cc47f1fcde0686531d56c67b0fb5a6bb4aef552f3a4450175dc7bfddac7bb39571fe7911b54a322d8b9bd
1dcde248c8b3d0de554a618ae5a367937c2d2d7c252f06333520a2cf3882ea1701b607f213577eac72eb393f4def6b036b7f
e1f03466889da6520e911d78012c175fb425118682f7c64c923f2398035efd9f2f86aca32077442e9aa5f0767e8d742f1f63
8d624a2511ac69f784bcd2b504b440c45972687a6f9b478f69ba8ee8407dd6c15c2c652b7f3a7872f48840fe8cecd0d15613
e1261d9c7e6c90fdc58516f40a19c28f5e4f073a658abd16746058110d0d09e78219b0cb71b5ed28588dbb251c29cf65239a
7d3afd59bb23b6ba117141a5d481f5e3bf25a2c6c0cfa98570ce65643e978788d40fd4aa6a91c50588a3d815f6d694213afd
e5174fb8168531da4ed0fbee4fda52295ee04c52d7d0cc5eed9d

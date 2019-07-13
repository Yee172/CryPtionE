# A hexagonal orchard of order n is a triangular lattice
# made up of points within a regular hexagon with side n.
# The following is an example of a hexagonal orchard of order 5:
#                 . . . . . .
#                . . . . . . .
#               . . . . . . . .
#              . . . . . . . . .
#             . . . . . . . . . .
#            . . . . . . . . . . .
#             . . . . . . . . . .
#              . . . . . . . . .
#               . . . . . . . .
#                . . . . . . .
#                 . . . . . .
# Let H(n) be the number of points hidden from the center
# in a hexagonal orchard of order n.
# Find H(100000000).
# ----------------------------------------------------
# Analysis: sieve of Dujiao
#           Hint: Take one sixth of the hexagon
#                              .
#                            .  .
#                          .  .\ .
#                        .  .\ .\ .
#                      .  .\ .\ .\ .
#           center ->.  .\ .\ .\ .\ .
#                        1  2  3  4  5
#           Then we get
#                                              .
#                                         .   1/5
#                                    .   1/4\  2/5
#                               .   1/3\  2/4\  3/5
#                          .   1/2\  2/3\  3/4\  4/5
#           center -> .   1/1\  2/2\  3/3\  4/4\  5/5
#           Obviously, the visible points can be counted by the summation of phi function

5fc70b33c6ad302deec017511763f2808f1f1a5e9f8aa3ea7968113afcf2c505822a52b99d97793f3e449855087977b224c4
751525a004d780113861f765f226c2504ce9d225e7b651bd95146a9d1fa805a70ef5ca1c01b78d1fc10dabcd67e6935c2099
079501f19216403bc3c0fceec8bcede097a7e37a19d436e9c14ef06f75b28a9a3440414f764c3429f2480eaba3ec8018f46b
449ecf1713136d9dc08563bcb6e4680727b8b67ebb146aaf0d8ac8fea24dc357df3236004b63fa077641a9ce85542e9d3d0b
211f71136d0a0f3d3feb90498b632080ea80e6d2b5a5c933208df42a7944a3bfcc4b4f8877a66d136af399e18e61b7c4e278
3261806f75d4

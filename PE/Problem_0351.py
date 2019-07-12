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

b55d4e0cb48475a31ff63757d35fa289d72e90b848a953776870c21709d4653029c16377feb8339208e4b24b31c28b7eb5570b4a4eb30b5d90ed9097931e62d7ddf744f3d3bb34f950c134c372aca8576f9f4e55655448e554bbe62c47a38611edcdaf13f230df95edac9aa479398a513c1136c16776d6a001e2fc6fa211d50d13a7a181fa170de8de4c19ee0cd03e57a8e6ae539546f2b518beb4f9d589652f84c56aac97b4f3a37e6ece346da3bdb6e5eb782ce89ae007e04b9d75d27ddcc4bfc867db170c799d01847e784e40f7ec5b8414a15ee0ec5737e6b9c850585637f81b44454617388d6f2a473a9ced5e4aec6231e41cbd713fb8c106cd1854b966

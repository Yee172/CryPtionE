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

008c8d83e4a113bc78e06c795e7a315ff0a126f6b484577ed0020489d2680901b6c0bd7ce7ab6450f3ebf7382b5860f64e68
33915d0bfa3ea337af261daddf455551c01b0605d0a9d91d7c24c41335b306426caafe99b6da37b53e5942fbc5dbc56f8227
8dcc59251bd1ad50b31cb8caa8045ae8de5e6250f23f982e7dfb2e663da8222b35110c2875cff4f811cc55c652e703a564a1
0581866ed9d6fe3318dbbb72ff682f7c4867495ff99d583fe4c8135dbf57f0b78bac1b4645b2171d273ea198a510c12c0b6f
ce8dcd46f90a812c6ac10dd2f9b4680bc5ac4ac92dea0f39045364de4cf6ba73d8d713732bf9d73fe08d1607fa0bf3d6b506
d0de6c7da2e2

# A horizontal row comprising of 2n + 1 squares has n
# red counters placed at one end and n blue counters
# at the other end, being separated by a single empty
# square in the centre. For example, when n = 3.
#     ---------------------------
#    | R | R | R |   | B | B | B |
#     ---------------------------
# A counter can move from one square to the next (slide)
# or can jump over another counter (hop) as long as the
# square next to that counter is unoccupied.
#     -------          --/------|-
#    | R-+-> |   or   | R | B | v |
#     -------          -----------
# Let M(n) represent the minimum number of moves/actions
# to completely reverse the positions of the coloured
# counters; that is, move all the red counters to the
# right and all the blue counters to the left.
# It can be verified M(3) = 15, which also happens to
# be a triangle number.
# If we create a sequence based on the values of n for
# which M(n) is a triangle number then the first five
# terms would be:
#    1, 3, 10, 22, and 63, and their sum would be 99.
# Find the sum of the first forty terms of this sequence.
# ----------------------------------------------------
# Analysis: brute force
#           Hint: M(n) = \frac{n (n + 1)}{2} * 2 + n = n (n + 2)
#                 Only need to find the integer solutions for equation
#                    2 n (n + 2) = m (m + 1)
#                 https://www.alpertron.com.ar/QUAD.HTM

54b5b640c9c72e4f730015558d9dc7f30910d1ca6445f2cb7bdd08dc189f31a1115f9569fd327112fc4c7b3d0df93b190745
e8f3c66047b1f3f90499323c45be7792976e25128611913963760d642a56fc768b2c13cc716417f161a66c972dc04aa50290
74622ec479d4eb90a19e99f1bbc9b0350e0b3e48d0b065f435b33e2bfaf78b5ad5940a39a91571e7f831d281659002144b0e
8b095729d28658a78bf38488a04b058817d0b1a6d85ea09dd2c03697aff56dc2f56c084dbd1bb6b30180385a549e46831b99
f8115a6b02b1c287da40602c2e3982f56994d6290e9051b65fb04d512e43fb8329f37d1a4626a62c29159f09238fa63f5671
ad630cd087167c2d2d7c695d8738b6b6ebd6b76a236af568899921d9d611ca8499acfc3e1e371a2f6e81942730dfc0ab475e
f02f91a5d131d4f1eb322859683a5d5066b1ec4ec1157508215de88e4daf932121a12172b87723eb36abd57e2e41760237ea
d2f37fb5c392acc4e7121502d7ec2c570005f67177b57d0fb6c9f3c5a6e451b0aa41dce8e8aec86c73dd3560ce5fefc5b725
9699bb434224a43829f1d8cf7f907f25e996d7723d1457fded0b1a5a077c9ca2f28c3a05902d32d87ee460ffe052c45d096b
5192d27db9afeac156621730631e06cd692b3c779d0e62808af837601442c5e621641eb1f10a8dadf32ad260af59769ca5df
f2fa3c81b5eba155523c1076882fec917c2d2d7cb4ca5d0d745d611c3eae43654335b8e816f9ab47291ba9beed4827d2d791
76363682524e2bc1514fd36aa3c247d4fd29bd0dc0d3912a83d7cfa86905ebda59fcd2fbe52e73ac24d7e752b41089864f1f
7c576ebaf1c40a1de924a9bebab57aafb23e6987014e70d67d09af0b460c1abe4e84d2edb5958f00c8305ea5b5701af1a6c5
40e7b8cc6ad91f9b3009ef2407430ba743e80816bda8971587b5a0244c96976661a456cb4348834d3057d833acd3c81260eb
8231897e014b0165367d5cd31d8f1226e68df2350d1b819b7973858c8e160b4a257e5c564a11596a3772c2d65b0efcaf031f
ab587808051ab49f8ba90322de02a1365526405f3f351be17c9e

# The Golomb's self-describing sequence {G(n)} is the
# only nondecreasing sequence of natural numbers such
# that n appears exactly G(n) times in the sequence.
# Find \sum G(n^{3}) for 1 \leq n < 10^{6}.
# ----------------------------------------------------
# Analysis: dynamic programming
#           Hint: https://oeis.org/A001462
#                 g(n) = 1 + g(n - g(g(n - 1)))
#                 \sum_{i = 1}^{n} g(i) represents the largest number that appears n times
#                 \sum_{i = 1}^{n} i * g(i) represents the largest index of the largest number that appears n times

409cfabf0c2aa19ae21ffb7f278537c981a89fffebfd093c53dafe07987de6055cb8a9c97f5e323d6624aef3546af82ef000
1e1ece2e496d2a9898d79c58d1d07b69d5bf864ed29c2b8b565ca5091ee6e4b0291d66a25f97128e2530fe74d43642fe8d0e
a0a420bd668ec6ba49976704ace242e3fe744bf119c5705dcc59fdf0577f9bb6a639b674fa9949b52ae9eaa0d8f2f6a5fe3b
5c22a11898cbac38c8aaa59e5355b7d4f0f7108ef45d850501af66a0583a132379991ee53f59724a3e2ade6271066e30d5ed
1cea3c7be6125d762fbd1998b1fff5651191e456f36da1e5eee4772304fc06a7c04e6bfb2170aecca9b2a5063981ae31f0fb
2dbb05ccad957c2d2d7c53d3d9ff073353d90df53b154c0b79bd4378cdeb4e67e86168452144a8ad11c098dc1fc3fbab415a
dc0b9505dbc2a9fdcbf6c751608ffc258416e833f2414adeaaa16eb134795519693180d95c36677c755e80a2d981348155a8
95e19a66c876eb5d35ca4fac62fa98acb1422c6595fc831a8aa0a5e6740145355f1cb145c911cbf1cb95928842141b0c653d
8582bd1b0cd8938a60cb0d2cb810321ef3b487e136d934969e3aacb8cfbc2a8c2bab92ca2f664c3fe22630f691d012904100
f5f226ae03adfab0564a56be32936ddcaab325361de16f19f0f06365517dbddb74059521aac69bcd382ce267864b532944a7
a9c792bc4691fa7398599eaad328da687c2d2d7c6f1454ef92af41efae17232dc7d7c752fb47f332c88eef00993800be1aeb
9593c83a53cbea1dae61c239bfd28dde0b690c37f8ee0fc89af4ee037287947a07715e591fa8c30935c567cd69684f84603d
179553b18ad846033da1acd8122c2673650ef1075667e840e0192ca42c16c38713025e21944129e0e4f82517edd3dcdad54c
b34cefcef58f0fbb4127ffadb7684566a46c67401f4b0b60a6705ba0e0ece31cf974929347907ddce612cc99147f85e65ee5
e62282158d7c1079512b1a26f208b62dc010efa30bb5a81eb6d0de7cc5ddbebd0fa5f502a55a30fa4c50a1ba6c4e6dda47d3
5a8e05808167f5f6437c4a3a4379d73edf5716cc67565b9945b5

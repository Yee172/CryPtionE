# A riffle shuffle is executed as follows: a deck of cards
# is split into two equal halves, with the top half taken
# in the left hand and the bottom half taken in the right
# hand. Next, the cards are interleaved exactly, with the
# top card in the right half inserted just after the top
# card in the left half, the 2nd card in the right half
# just after the 2nd card in the left half, etc. (Note
# that this process preserves the location of the top and
# bottom card of the deck)
# Let s(n) be the minimum number of consecutive riffle
# shuffles needed to restore a deck of size n to its
# original configuration, where n is a positive even number.
# Find the sum of all values of n that satisfy s(n) = 60.
# ----------------------------------------------------
# Analysis: mobius inverse
#           If the cards are numbered from zero and the total number of cards is n, then we can see that
#           the first and last cards always remain fixed and for each other cards at place x, after a riffle
#           shuffle, it will reach place 2 x % (n - 1), which leads to that s(n) = {smallest x, s.t. 2^{x} \equiv 1 (mod n - 1)}
#           Thus, \sum_{s(n) = k} n = \sum_{d | (2^{k} - 1) and s(d + 1) = k} d + 1
#           We can see that \sigma_{0}(2^{k} - 1) + \sigma_{1}(2^{k} - 1)
#                         = \sum_{d | (2^{k} - 1)} d + 1
#                         = \sum_{m = 1}^{k} \sum_{d | (2^{k} - 1) and s(d + 1) = m} d + 1
#                         = \sum_{m | k} \sum_{d | (2^{m} - 1) and s(d + 1) = m} d + 1   [notice that (2^{m} - 1) | (2^{k} - 1) when m | k]
#                         = \sum_{m | k} \sum_{s(n) = m}
#           Therefore, \sum_{s(n) = m} = \sum_{m | k} \mu(m) (\sigma_{0}(2^{k / m} - 1) + \sigma_{1}(2^{k / m} - 1))

2f18caf368ab23bc2acb07fb0ef36c38147ad4b6a5acd4cdb73647bfc17a7fed8e73d4313c6609a1f56cdd3445ced0bbb6a2
fc68e12359d797e889ce18cc21301af2ea49459c98f44a2ab66af5bbb970a4e9a8bfdc13c1c046ea7736e1d23078169ae221
5956f9a7701b0567e6e6450784d761f8ed3ee9667cc06f0ca2bea781e1353680ca3ecf2ef3359b7f676ecdea93e7abe9d7fc
213c08e3bc53c7767a6519e4fce5d7a46a828abc780f8639d7747250b5cc6a2907e04926b27f0e81b2a4a0841ab33c296b4f
a4e935503cbaacbc114384eb0757ffd268abb0efbd1c23d0df5fdb300f7d4af45fdcbdd85a924e3e613648df58572e748572
be83b804c4bf7c2d2d7cb65f4a02fa25e0b38c5733ff680868a3bb5b5c412561f748663ec0c40d8c2515b324ec3d21b9c0ec
b532eb00371034bfd28c533a379f4582a8a97acebee423f441fce4375d12c7dd4cef865937976ee121f03f692aa55221359d
ea60954ecb84dc1b7a01396f047ec85406023cdbf7f164de629c0fbdb3c29a55fa7ca2a84401ecd5a05fed2510194235b2bd
2539a25d6fdec2886910b95a646ee299cafa9f41535db51630429dae88ff1a62571cf2fbe2d9cc2ba619aef18272cd1b4ac9
688e7af4797bd6a642e1278daa709e300b91946ceb32f116f23ad4d709b9c29a800a0208febde090a127df4eb6faac2271f0
7beb957a25b29a17c9a53465c9fb9a827c2d2d7c4d654dbee706d58297a50a83f39cf64123b980e43a7d74505cfc38a6c1fd
64e9d7a60a3c42a6f878ffd6dc1cbe1f8f41a826bd53469e012b0704dd6749c62f55f243f66c85a2f00c7b8e6d32ba21638a
8f0941b0a786e3dec7cac000905f44554ee744afcf867224357d8e5e6fae77961b3432a361d3f45e14ab051a4c9f08d06e64
04d0a1ddc5efc71e9da0a8478a2e245e93d1f0b5957060b5b4c8d3690e276aa8c8029a6d0efb3942a0db124d4ec796ea0512
5676b24321ebf88aea5bb620e7b8f91bf7f647ecd904ca9962e58580d2b0aa3fdf3b91bfec99653f8db98d846b08e8ea5f77
5071e08469e82a8868ab57283332a08c0774447706b816c9f2d17c2d2d7c018a6c9aa6b702b8dad118a7c6a4f785d7f44065
fb94308d7195ec4027989dea2b465876f10d8bc66e3a66a48b14ab1acc5eb8de6dd4c3d53e2ef6a7de9b6ac98a9011352a3a
3a1cbfe77f5916ebcd89972885e2146a48d7af7b46f9726b1f90484db88de42aead92a7360a1a8431ec63ae252cdf64475b8
b9a009b3fe71fd5850c6accb92ce5b16db54527ffb232403367879ebbddf4acebcffd995faab93e81233d6610900984d571a
b9309af090efe0324f690af9ebc5906b6844d3706a1a3d5b35d120fa05459a8174f69323dafcdb5a551086ad9012f83b87a5
065a7625675bf8dda50d8a3742901930f4491677c67b742d349c5bc0d85280e9d2586450

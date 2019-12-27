# Let T(n) be the number of tours over a 4 * n playing
# board such that:
#    The tour starts in the top left corner.
#    The tour consists of moves that are up, down, left, or right one square.
#    The tour visits each square exactly once.
#    The tour ends in the bottom left corner.
# What is T(10^{12}) modulo 10^{8}?
# ----------------------------------------------------
# Analysis: matrix multiplication
#           Hint: only consider the last column of each 4 * n board
#                 1. --  2. --  3. --- 4. --        5.
#                      |      |             |
#                    --       |    --     --  or       --
#                             |      |                   |
#                    --       |    --            --    --
#                      |      |                    |
#                    --     --     ---           --
#                 The corresponding state transfer matrix is
#                 1 1 0 0 0  state 1
#                 0 0 1 1 1  state 2
#                 0 0 1 1 0  state 3
#                 2 2 0 0 0  state 4
#                 0 1 0 0 0  state 5
#                 Notice that only state 1 and 2 are valid, others are the middle states.

09a99b1c01171d8553f02add67dd37e5bdb3366e73590c4f481dcf9d322c4bb068c38165f9bb4c367886f0baa9aace2cd474
6a1d0e9478d43ddb57653244d660a0133b2800dec6df32d0983d2c47ec81cfcd510ce306c90738feaaf3998e31aa06d16421
5801e4e7ea665d7c167295bc3a244186759ae4ceb79db7342a7945801683dbf6989dad8aa87ec1a4b0d5f42449ab76465a5c
7147cf49c045c993dcece34b20b3eacb5b79c2783b00249c975eea772f1bbad88e20b2350f557cd5587cd65b68d172567784
d8a521fcb21b88243aa98edb8580327588058752d4985817fc3a9d8509fc584671064bc1f019f2d81a90c50384f5bd99cdc3
c867ca34877f7c2d2d7ca0896af1764980146fc6a84c65aa6aa2dc9eab8ef7a54030c9238b16ad8d2e17efba6db240eb3369
97743632676f8d212664826b8f658ad803b15119a995da832422e582684c0ce11b41b4b09e6375470c6144c9fdd2086d052b
46fa3c58d34e67bec17022a775f80e56759ed41ba413fc8f0462a646ec107ac74820fd9d470f70d1f3027f87030dc4f40f07
6e31b1b2bfd8a166897f23fb31ed9d1f69a8379811389b1abff859796b9dd560c29b75924f27a8ba91c7915f41f228b1ba0d
609364d479975701ba903fe2160ec0cfbd284b6c04f02efaf4942fc59d85e6cddb5648807863f22b42cd7311ebb4065d34a1
60909901781ae481fc83fa07b43ff94e7c2d2d7caf10a4b7beee13638f968239158b6e823fc61c54777fbf76b6d6d7cb3cb7
2d4634ff8bad937fab07c38f5264e62a8ee894e47e6d4cafd06056b2fa04b1d08f2f28c7322fe4cae66658b06e2a0a00f188
60bd4117e1eb3bb16a55b02bfe59a9421fbf8a8b12289d4cf66ed520cc1d5ff2f1ae9e74484ba4da3c8186ec52a3136b62b0
22e74bedcf2b3c9e2f656ad152ef30d0726843c6e163450e809da8f1adf3d13d7e35be90e9916e920f7c552d3aacad12c5c6
b953cad5937b606b408b260f14aedeca293652de63f303d602ea3d3d618c1740a22d6961cbe740bf5265abfbd4f2ec355cb0
19eede43a15b3d0ba75e4680e61b4a2d31090839a5746ed9d202

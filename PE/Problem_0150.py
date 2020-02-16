# In a triangular array of positive and negative integers,
# we wish to find a sub-triangle such that the sum of
# the numbers it contains is the smallest possible.
# We wish to make such a triangular array with one thousand
# rows, so we generate 500500 pseudo-random numbers s_{k} in
# the range \pm 2^{19}, using a type of random number generator
# (known as a Linear Congruential Generator) as follows:
#    t := 0
#    for k = 1 up to k = 500500:
#        t := (615949 * t + 797807) modulo 2^{20}
#        s_{k} := t - 2^{19}
# Our triangular array is then formed using the pseudo-random
# numbers thus:
#             s_{1}
#          s_{2} s_{3}
#       s_{4} s_{5} s_{6}
#    s_{7} s_{8} s_{9} s_{10}
#              ...
# Sub-triangles can start at any element of the array and
# extend down as far as we like (taking-in the two elements
# directly below it from the next row, the three elements
# directly below from the row after that, and so on).
# The "sum of a sub-triangle" is defined as the sum of
# all the elements it contains.
# Find the smallest possible sub-triangle sum.
# ----------------------------------------------------
# Analysis: brute force

48a44b53a83791d8c8f47d8ee72d65369815039ece5646f566346a6bb0d12500e7a7267acac35902946719f4a28c05f2e59e
93b7c539d835d54ab45af6da78d0e42fbf1325f6bae1cd6a53df2857f88445b5eacae6d0a11449f1eb1f176d1825acb1eaf5
d9db0807684eb110ae25689b41e9b1ac788fbbd6f134ce043bd69fbd0e05c6059f3d3031968091a12a6e52fc6cf57f18d434
31b22c1cfb65c99320d2aa137f82743ff0e525b0f0e1a39dd751756cd08f08e7ca21f72af869b5609f12d476016e03730a79
02a376be91170c2087c81d532facf8650f009e53c019b9427807eb3f0710b6d4286c9ef06c41a7cfa32f2c2b657da7d48fda
0812c91024f67c2d2d7c3dffbc1e1f0225bf115e7e58271bf0fec61ef97442236d2e796aea1766cef9ebb65a9af54b3ece31
a6852b79a87f510736eeb8893f082d6c34193f33a9fb60ea6b11f33dbc9e0e89bb9eee6ec6aac242f25246c53ef64548d359
e859f1c543ec32d1fe4cfc6def3449aa9ffb47e862131beecb9448215e542a727b17acce1e08d0b4eee49a5ff9ef941d40a4
49223d3567491bc92c1a3e7a1d03bf06ab49cf838efe12484c8cebf91b2c0a207de9a830098900456f4842a43c30fd926c9e
5b6c35ad004c70ab21c4d5dbb981b839dc7808089c7c65e4c53c4fad852019e29aa65d38652623e9b2f4abf8a58356c0e090
0e4a214d2ba4e9c89c2595951c45d0b57c2d2d7c3c0613155ce9d83aa43fa5710f6ef99c6b4deec4d8f5fdd9af835ece44e2
d77657089306be6d56d442077070a72649a267b6ccbf121c349561d276df722f13b214b6a49d398682fdb2ad3913ccb9ebe5
f06097e44188c2b3ecfd3e01553eb94ef8ae3ea7362326c2e3d57f2072e58d30e45b023e51df48a35dd8eff7c81d6772e544
c85a51bf91a17cc99a06acc7982ba56328b6629bfdbcfadf421edae835a50cc8704412351f850ea2e65df535af58f61e08de
18f4fecf32eb47689d2df92c53b9876b77f8f73794d422a0b6d3c7c985d837cb31bcff548131e41354d29b5ca4493837f73b
63e33eb32eb9629ff4721ff9b9c9e31a42cca8fb43662bfc94ab7c2d2d7cb41ba4041814c8905cef04b2a8865f2a3423de68
8d5da8ee93c08f713139230b90f91788e511622219ddff63a6a7e30da73e293e88c43e1417194389b79a2736c7ee5c34261a
8d1fe1035df75fa67c3cb39bdca8ee4265da790e778128bdd93d48c42a54508089b4e37be0a6321242d3e7d0e33d064021b3
2e4f1f0cc14edf9b29f3596a44317d310d59a1c757b1792150111a16de0863f1d0cd976cf1f042e863a21f7048b6a47759c8
a4d1f55ee3166aa06adc6123849310c3bfa85b9408e2cfe09d44e347981964e7bdfed639282e29dcb4a9c89f29da7de21536
639e9e6c326b7b5bc1576d8ca42ebcab3455bbc9f58b3e30884f2cc38e83bf6e443e6113

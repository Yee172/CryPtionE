# In the context of formal languages, any finite sequence
# of letters of a given alphabet \Sigma is called a word
# over \Sigma. We call a word incomplete if it does not
# contain every letter of \Sigma.
# Given an alphabet \Sigma of \alpha letters, we define
# I(\alpha, n) to be the number of incomplete words over
# \Sigma with a length not exceeding n.
# Find I(10^{7}, 10^{12}).
#    Give your answer modulo 1000000007.
# ----------------------------------------------------
# Analysis: Stirling numbers of the second kind
#           Define i(\alpha, n) to be the number of
#              incomplete words over \Sigma with a
#              length of n
#           When n < \alpha, all words are incomplete
#           When n \geq \alpha, there are exactly S(n, \alpha) * \alpha! words are not incomplete,
#              which means that there are \alpha^{n} - S(n, \alpha) * \alpha! words are incomplete,
#              where S(n, k) is the stirling number of the second kind
#           Therefore, I(\alpha, n) = \sum_{j = 0}^{n} i(\alpha, j)
#                                   = \sum_{j = 0}^{\alpha - 1} i(\alpha, j) + \sum_{j = \alpha}^{n} i(\alpha, j)
#                                   = \sum_{j = 0}^{\alpha - 1} \alpha^{j} + \sum_{j = \alpha}^{n} (\alpha^{j} - S(j, \alpha) * \alpha!)
#                                   = \sum_{j = 0}^{n} \alpha^{j} - \sum_{j = \alpha}^{n} (S(j, \alpha) * \alpha!)
#                                   = \sum_{j = 0}^{n} \alpha^{j} - \sum_{j = \alpha}^{n} \sum_{k = 0}^{\alpha} ((-1)^{k} * \binom{\alpha}{k} * (\alpha - k)^{j})
#                                   = \sum_{j = 0}^{n} \alpha^{j} - \sum_{k = 0}^{\alpha} (((-1)^{k} * \binom{\alpha}{k}) * \sum_{j = \alpha}^{n} (\alpha - k)^{j})

110580d4238e541fdf6deb682889294effce3d77800c4e94a28a0b03d9629aeaabfdd032fe8f6a24f6df3c29d458665bc3f6
138be21c6aef6b1417231112f45e1c70e524ed8c4ec88c3c80edb48082fdd3e64ff43258c6d64a4df0d150dac98acd303ea0
92da68546ab6c2395ed8f6029bf5e939a1220666d45b69574319bf48473ea2855252b74f49704a14e3d596b4438e710f8107
7d58fb8d9d1e68b379433c76d0abe6e12ca612fdabac68796e10daaee9cdd7edd778a0847f89e892b1a16839e3b4d775c9c9
22a39509879d0815481347fe7c8964a94a190e4775d9450f32627c1c3bae28216c3cc8c7a991e02520ac2cdbdb56c295504f
8290a291a6837c2d2d7c1bb5c9ccbf4aea6354f6c2efa00ac5d760d216cede0f3a3d4e8eaa23f4da6fb71b6d05d93f63ed8f
62c9e796fbf09c3eac536e2ed3a689112f096fddcbeecc308f24b879eaae618c6a8ce4d22cfbfb476a07723d3798c6db1c6d
b6ada68f649931ab4ccda70facaf0aadfd9ffe102e83bb5a4285e6e806cac7f59471eb8801a64d27cac81249e9ed85ffea17
7c05ffec0afd51a5a771935ed80068e28bd12f9a672d7b049963f11c384d9e63b084d24c22993b2eb259ff208bbb8319d694
682644972366a64ab822331bc50b9efdcb7adf9ae525733edd31fb33fb7e940343284ee5d9d60a7e88a8b7ee59f9e3009abd
d6ff6e04937652e94fa952892da981df7c2d2d7c9757efe05f9e0c0d965d1e23d8f552bb92177440c2d8fc95348680df6a76
dc6e0308024a42b70d67687c8da99f8d7932d79b55e9e34ffefb61a01d115a72a4093d5fed406b2404111bce2c4ab345d62d
58d8ec98d220f49188c9a05fdd07876c8212805ad497f6e61eb34d8459132161a296442a104ed0a4f8007edfce816ef3eece
b35b9fd9d7eaa5efc7aca6716650223ab5b63e162b716120ad019cf18410deff56d98af9dabb84f520d26763d5067111d96a
fb330a141a0134e1cc28717f44277779735259e35321fcf33c15ab97c84a09fea0af150281dcffa351ccf05c3f2b4bd1651c
3020f4f0831b20e43d1b7ba88fd4984c529f5e59a94fb944fac87c2d2d7ca2df4d2d3d8feeb0f2fad591bb84c4068973b76a
4912da522c5a81367b035901b5b0725df68d1f4860351916a247db1278df113e323d98a0bf9bb43400ee5c882ebc0c31a418
11429509fc06d7712c59c25fc07929c92409c9e374a99cde3686c1edf55ada87161253c108070b40e382bfd68523d1b41905
91e8e70ba095321bb7fe050838a57d73c685c06885a1104f4ddb63bda5f59015822498a38ca790699c1b61922c838b92e877
d547de4d016f96a07df46bd5ab097d822a50308857f57a76d7814c4c9f39a181297e08853da3cdab4f877b28d8eb714b25b2
2c464575a3535a8afe3120008ec1aa48b59428ce29ed93d3ce7ee93b64bef267605274247c2d2d7c1d1e43b4a337698cdf35
0dc5648f8e2ff7ae9055ea83f1c18b665212646e9b9685bf6070d92e148cee2cd47b743ac1124729d9ea7c7ac0bfb97ed55c
5194d511e29598adfb901a776050e38e444cad50d38dd1e0025b518a00d56b26f5f429bbc1b4df21e45e7b061a2e4654f45e
7a1bfde60b080e2cf147acd27d0cb0d8143053e47120e4108d7df340b259947eb4b2de05108a2082d16ef54b047e496d9754
0fb75b98a095ce33345d191058dfc6ba41db8966a18d403be0f903c671c5661b278be0fc5ce741199ddd0cbcae16628fb194
9ce5aca7f7fb7c934ccc42be33be5a4b050199ea990ba278346e6d7bef0e076683338ec2080203a0c4a9792a8ff1

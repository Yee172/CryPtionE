# You probably know the game Fifteen Puzzle. Here, instead
# of numbered tiles, we have seven red tiles and eight
# blue tiles.
# A move is denoted by the uppercase initial of the direction
# (Left, Right, Up, Down) in which the tile is slid,
# For each path, its checksum is calculated by (pseudocode):
#     checksum = 0
#     checksum = (checksum \times 243 + m_{1}) mod 100000007
#     checksum = (checksum \times 243 + m_{2}) mod 100000007
#         ...
#     checksum = (checksum \times 243 + m_{n}) mod 100000007
# where m_{k} is the ASCII value of the k-th letter in the
# move sequence and the ASCII values for the moves are:
#         L  76
#         R  82
#         U  85
#         D  68
# Now, starting from configuration (S), find all shortest
# ways to reach configuration (T)
#         w r b b       w b r b
#     (S) r r b b , (T) b r b r
#         r r b b       r b r b
#         r r b b       b r b r
# What is the sum of all checksums for the paths having
# the minimal length?
# ----------------------------------------------------
# Analysis: brute force

489bb818ee69a5f3e71f108dc92b760d46db523f3828109c65c714c18e13034a474acaab3d51ef59fddae9e001a3d686ba21
c13054deecde4e8c89cf500a4f3709d71bb941e1cba5eb85b30d5f7c9c80e4225e16b2b64ae5822a5a79d4b6dcd526a33ab4
e4bab033fa849723091b87aa1488336ff6ae4b5ab82690145924def31a3a1f31a3d7c89cb09f0612bfad6add5bf526a44402
14cbb3355127f66e58cdad51f0640e60b988b1ab6d0ef30ef59f0e01a409817710a97befc174cc52f4e3c80231ac382ee646
83b2b72065676bdde3b0e9776e308414e13e71e78a57ac1004ff7a508b14531cddbd3479f747008f5e22378553e7370b4cc4
ef41ab8a8e957c2d2d7c67ff590037fab37ea4791a74c2af83f58b6071eb756877fa00b20b026a9b4b9ad856000e58017b6c
5f9a22823270b8e53ceb21fb032991ba09c8f528fec945cbd46458474ee76845fc93a3fc76d7134a4bfbb959557904d2bb7b
4887b47923a738970cd0ea0b435504e422c7d5198186cd43e79ec41c39a12938aeea80512c1e94fb5f79548560c6c5ee814e
464c979e7c9f7d91fd3318702470c874bf3f8a05a9a22724ec23fb67f24fc914be827ae2d91cbdf59a3eab4009ae3a77f443
3398956b89fe883ded46132f1ab45a4a3698ba2ec0c7b5a70f5875bfe89b8b7fff85935eec2256d1fbe648b9f228d28ceb07
062a81feb505435b08ff748544d124a47c2d2d7c4371302950db3964f87c69ef34d10e5c6377239a42931cf8881f2b461588
8dabcced212a464973037b8647ff149f5f5c7b304e378898f6223d11e0efaae0e7d8ca4ec0801c5ec63a04250912cad9b07f
b320f033d2201700d9ec8d48f14a173b740aadfd588f32a4967bd38502f71d46952905af1b82a39137b5d8da3438500c9758
c5482abbb6687806a98d924ce96e2dd4c3689fb0753efae9f5ce8f74757b049fef10558a3b0a58af72fa89b756b6d4db3bd3
ffb96ec31ea779a5a6b2937b562c4b44a8600dfe218a6759796f52af15f4dba738e9e2c22a9704f53e08f3fa13beed9c94ca
ca86e96db4f7f01f8eeb9373c7763e9dddda41136328d69b0f177c2d2d7c928341cc25331166a18e7a70387ed0100dd986b7
4d1e390393ac59c2a037aa023692306787f796069cedb58160645ee252ec73dc0950d9edbfb55fb7d2de6c5b62098661749c
16dbd781697443093698f525cbfe66fa4ea9468d2cf8ef364dbad2d285f9a8c25528a458b4456836c8d2bba5662a3485b224
e7f6d58af652123820fe2402aaa54c6767eb1117eecc3da2fd0da653065e1d0fdee61e2ed43f9c8e34616588a582f49537fd
fd6a58280c81d2c062a69f1a202d3d8ff4d64bb1f2438a85ab2d904181de94f7dcbd3cf00f38a53c6f2bfbf25c738ddd988e
a595d1235a25c433d142606eb05117ef83a0f64c3a036924071a42fa0d567aa12622251e7c2d2d7c4cc1bc2d6f944d88206e
67c3ac8e0eda76f73e6f439b8633d7559d56845fd77a610a7d572f31571c21c0b2f791a85412fd359f53c63785dde2ec2f92
522bb75c670091133a940a7eb77caed8aaa5dcb3ffd5d84faf18d98b4f9b43ec06ccbcef0ae49086e38d7a289f552869d097
c7639e1d5eb729307ba497942298d7ef857dbcac651b46298672163b656242a550da34aece7b1b1320bb9b118ac890cec9ab
1841ed93d544c10b7fe5bbff491f41427d0c9242bcdfa50a5f1c18f2a79201b9bf94d06647fd9caa3a3d281d4e8c7d9aba59
55004659043571f02d18794fb0b324686ebca799fc7b7374af315b18c7d36b3d2a720347c901819c7be76b8bc1117c2d2d7c
3de5423e30b1f8774dc343f298b34c5f71bd1a1ec7b875d9e31788623bca2e7cace396a7bff6275eecc89c50d1acc18b1db7
302511172dae84dde064783902ef362b4167e9433639f91c1fb21ce4541c8d2062478cbfecfeb437894ff267c6542de5d253
ec12a52f2544fab4169b7bf9a8fab476d6e6eb9373f377d64497bc87f08e0d203c161c266607857f7364f2e7a826961ed267
bf807107092aba29a14ca109a3a75840427e313fbe2d4adebaec191023f2577ee85bef9b4d475eec8dd0740ad6de50f9b472
45161b7c892d619bf20edecb148d00a082ce30d73303e3e34fc275e8175a399d826beedf8949d357a51b78fa407da7efbc80
48fce5e1640b7c2d2d7c021891aa96cf305ae484003afadbf392565c89a9b203a23d0b90b69382860a92fd62a5e513292947
b72425c133a6f16e81d64a52b1681ef5c65de3a54b418dcc481ebf48ebffd5ea203d0dc48417fc932b8306381ce038aa5b21
5b87d6433cf8bad43341c71dff958ac4e366bbb20bf43cd38ebcd50ee83528332f6e9e4a1a1957b01b934c5280a1603b603a
236370dee85796e3252d79578a4e71a6341473b1bef3e610038ed65091725616d10b25304ffa9a3a5dc784d4c27779653460
8fc6f3f2bfa4e1738afd99649ca8043c16b7ddbefdd934de8238d43cc7726db8c20b6c78db98ee1519af0a3fe07e68b23d5c
4afc7ffcda3d344fd42d1932f433ecfb7c2d2d7c9f2f06f7eff37495250dbb9091564376f90d78b0d2eba7b817b7712e032d
06bd03fdedd4686249f1bffeea5fe3b0a056085d1ab158d5c1726134a3b49d2d5a6a1128ff12a71d5b1673d73baa437c536a
f8c525ee91a09684fa0ef0dfb5c544ce7400c37d1fa9020311c794296e2fb3b2ab5a326eb5048ccdd80b8de92079d7ead003
e510a46e0ea305861514242d13f59939b713c6102f0fbf86c1f5c3ea89eee797a075e3db650b442f0ddf133bfb33a36c9910
9053244e67afa8c30423ac4214bd2685188a3bf15eaf6d47fb337920e4ef201884988abc28b7c2dda8216a17872234dc7445
91f987e93b14870dc626916698e0abecdde9e809c1b2344d21a97c2d2d7c416580bde09751fd4929641d641c5d1e27712dea
11b01218e9b5707a9caaae2f584cefa1bce7d06dc0f4388ef2488005e9a31281f68f3f9c619363b84d4312e17d7f259d1629
80987a04d925870db75c81ae486b75ecca5bbf8cba970b92abe2a36a74b473bc99e06b037f1c4f09bfb3c12e8677464f2776
85411c8ac7b2a846e3e99795fe5de312f7aa98c98249ebb7e31acaa716b6a857bba66cf7ca8ba78cb538bb84eea26ab79c41
f41ea252bde653508d6b320a07b8b367b0166f661ec58858c0d6935570162cc3bb734946513df11c38a633d5d1b30d5ca929
4448e85cf38ff5177bb6dca76bd8d8fd1bb9630c924f741e4396f9d570e8fd99bd806a827c2d2d7caf840d9acf4678a4806a
edc63976095c98b3298b7a0fc72b9ddb9f3ef45c8e6ede4a428e882b1c53b4ab01c5324d464bf02c6150c639a0b7a080d483
078b488c1e44095a30337497665c6423fd085b06ab25774ae1a7df0d5d31555576c36982836c090f5e96b350a2e0a9ac6764
e0176073823c6cfffa39ea30155ccbeccc1f762bdf2e5196a0e08e6fbc98bae93e6a5e8121aa0d4872abe6c47b1413bbfc6b
9e5abcaaea905f91c1287b3674b49898e3c0061e19ec7e18ea78fa3da913965ad0c578e26bf70b1aacc63139adb2a67d2932
b22125dfa6ba135e25c3b7fc323062dc28b238fe4860f889e1a5c1e30315d212deb802cb243ee45cb4c758132e51
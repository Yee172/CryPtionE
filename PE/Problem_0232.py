# Two players share an unbiased coin and take it in turns
# to play "The Race". On Player 1's turn, he tosses the
# coin once: if it comes up Heads, he scores one point;
# if it comes up Tails, he scores nothing. On Player 2's
# turn, she chooses a positive integer T and tosses the
# coin T times: if it comes up all Heads, she scores 2^{T - 1}
# points; otherwise, she scores nothing. Player 1 goes first.
# The winner is the first to 100 or more points.
# On each turn Player 2 selects the number, T, of coin
# tosses that maximises the probability of her winning.
# What is the probability that Player 2 wins?
# Give your answer rounded to eight decimal places in
# the form 0.abcdefgh.
# ----------------------------------------------------
# Analysis: dynamic programming
#           dp[i][j][k] means the probability that Player 2 wins,
#              where i is the score of Player 1,
#                    j is the score of Player 2 and
#                    k indicates the current turn is whose turn
#           Then we get that,
#              dp[i][j][1] = (dp[i + 1][j][2] + dp[i][j][2]) / 2
#              dp[i][j][2] = max((dp[i][j + 2^{T - 1}][1] + (2^{T} - 1) * dp[i][j][1]) / 2^{T}) for each T \geq 1
#           Since dp[i][j][2] always takes the maximum value, then we can see that dp[i][j][1] also takes the maximum value,
#           which gives that,
#              dp[i][j][1] = (dp[i + 1][j][2] + max((dp[i][j + 2^{T - 1}][1] + (2^{T} - 1) * dp[i][j][1]) / 2^{T})) / 2
#           => dp[i][j][1] = max((2^{T} dp[i + 1][j][2] + dp[i][j + 2^{T - 1}][1]) / (2^{T} + 1)) for each T \geq 1
#           Therefore, we have
#              dp[i][j][1] = max((2^{T} dp[i + 1][j][2] + dp[i][j + 2^{T - 1}][1]) / (2^{T} + 1)) for each T \geq 1
#              dp[i][j][2] = max((dp[i][j + 2^{T - 1}][1] + (2^{T} - 1) * dp[i][j][1]) / 2^{T}) for each T \geq 1

1415f443b1b48df0d2839a62a0ac2cd4f60e417afad2a3c457b50345816e2e922ae570d7ecfdf83e5ac8db5829a5486e99c9
17410e43dbb29f6db9524c947c3630cc9492cd684deee2e26bb2f957ae3a0a137479db597de11f1b7c4ba0f6107ea005b3fe
2ddedcecc1afad463f9aff200faa8dffde131258c218c13993b329ee239cd95df2a970f35b690fe9def0cc452537d00c31e4
c241a47faedf3285e3658138625552378d599adefb90e91b74fa42926efda9b4ebd698a0602b8502b00dc106b3704212d40e
71e25121f4036756e4d77a69bdf2d6c9e24ffec69b28eb87ef0f0a23617549eaaf6c859bf76a87523dce1caa101ef90b7ed0
94949a4e175c7c2d2d7c649c045223776c6bbe3c3594bdf06fe7e6e2c047f981c78864e7a95a80f055ffcaa0d5088c69e027
25de5502a0394fe9b7f5f504205be218d7a6b390ce280964e105b7b490846110c2be1631763d4b78ca6287a005f6bb249159
84f928a89eaf2b836731bca8fbd8f8d5b97492631c0f2d10ed964b4cbaec13c31fd198a4a2715db6a1b6e346711a20b7a9f6
ededd1547a2074b9c903c1fa0a9feddd14a9886cadd95672ff1a1a09751ff8cee7ef286c62f64560ea219c291e5432fa7fd6
88b636cc4bfb2ef1a7624f33746fac23f899ba3cca773aa38eb54ed4086e87520605841234556a7fbccfd6544950c071bb28
1462ca00fb34494510f0b8b95a195bed7c2d2d7c1522b5134a3407f86ee40d86236a4909b4c59b6a76d441fe5495f5987572
33bfe11e2d5b2833e67464287ceb2169925730a492ba142521805d865c3b7aac0771b4ae4dc316007541a2ff1a510e1bb617
0c287b1ab5744a6294c4074c8a52d6d093dadaa780ef1da693971a68845e3413a2d4217e717e684c2f5911f0f75b6d0f8a64
9b2832374125809929cae0b0d2f8ac3fc64cfc0bb81d3a669c110437cfa2e44dbe3a6a8be7b5113b93fc18a319237204e73a
af81703de0288b5d5237c2d77de49619776bef46efbd45f0b978817576c8ede7e20da2c9cafb3b6d2bc9fc744250c3d36315
ffdf03aad60d1a3c743797b076fa8554a97ece41dec1ebb84e1a7c2d2d7c51c04c9adf8d74e85ed5a2f139b80217cf3c84f4
9b42c9156f355c84e2849095fcfc8054d847725a30d2cc30310f07eaf05f5d928d6e6d048838327c5b2758d458a9336890b8
883192c8dd2569c656b146fd1b86dc592495e469d492a6ead5815ec44e648041d191615cefe76e5411c62989c4bffdc82bfd
cc5aea7e4e0330309cb00a7d081eba0ae94c94facbeeaee4b3473c451c884f8d025bde410b4787e689be485844f70c08f6bf
4aeee1ee22c80a51910f06fe69edb1d2d8519d36c494d44fb2e41e1ea26e398c8a8a090676e9589b42d979764435a4d4e5bd
cdeaa47c95d1968be000cddafe4f2be3f8511605872f5bc8498f240a3efc6d1d661962607c2d2d7c9768453262871bc44866
8281216ab7b7da7b899cf4cb1e8ddcba051e7e03ddc4e6fc724bb08f83d3943af154e6898e4fd052819b5c70e1a294da8867
1e28af35229b2553239b3e22f649c5e81412b212bc4a0ca894839e475c73475f60cb79baa7422c30d8c1327360c77364914f
32f1d03652f500459fe92a8c3d39a1dc84321e64f2eb64f30285633885f85a2b18f337cda96ad859f8232ed48a7c7bf507aa
1e7890c5f8ff28d857d943977e8743ee26c9d261a69631b6170b488e5d1f0f2ae08ecd5dee362880eedd2270fe9e5918beb7
0c262316e41365c77018527eb0e729383956e4138063ad10ffa71abc3751707c0fd5559a715b603d59db773f7a9c7c2d2d7c
9ba1a873227e9ad5f8c11bd8a63a6dc963bd1962b8df98ac026e52e22256e98e258480ffc9f61d41dda3ad4965fa93191bac
ea9d6c697358c294db2390520c104babccafdf84dfa3a3aa66fed16eb981b1b18ba5152f82ff20ea8f8a269b963a0c108142
342d0261b09ea9353bab476811f3a2533bdd7e8691141c2f629acc6628536f4e6505b62d7acc023f11373be79b96febbe6b9
057a4a8c1c0b98e880e538ff339d5a74de0a2d59dcaf39ed7465ed452d66921a7afdf893b9d50e6a915ca8f9607c76435202
c03b888ab418cf9d5590e15107fec9556780fdd209ab35a03ab458b28871091ddb1eff3f982403643ae901d36ceecc478958
8f5781314dcc

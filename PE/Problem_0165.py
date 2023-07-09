# A segment is uniquely defined by its two endpoints.
# By considering two line segments in plane geometry there
# are three possibilities:
# the segments have zero points, one point, or infinitely
# many points in common.
# Moreover when two segments have exactly one point in
# common it might be the case that that common point is
# an endpoint of either one of the segments or of both.
# If a common point of two segments is not an endpoint
# of either of the segments it is an interior point of
# both segments.
# We will call a common point T of two segments L_{1} and
# L_{2} a true intersection point of L_{1} and L_{2} if
# T is the only common point of L_{1} and L_{2} and T is
# an interior point of both segments.
# Now let us do the same for 5000 line segments. To this
# end, we generate 20000 numbers using the so-called
# "Blum Blum Shub" pseudo-random number generator.
#         s_{0} = 290797
#     s_{n + 1} = s_{n} \times s_{n} (mod 50515093)
#         t_{n} = s_{n} (mod 500)
# To create each line segment, we use four consecutive numbers
# t_{n}. That is, the first line segment is given by:
# (t_{1}, t_{2}) to (t_{3}, t_{4}).
# How many distinct true intersection points are found
# among the 5000 line segments?
# ----------------------------------------------------
# Analysis: brute force

335c0cbf8bd5d2b501bf8be32d00819f57d04eeb7dabb386020a44b46edf1166d79539bf753466eb53eb7207e7de98fa7a47
99ae5fc21466dd5ec152e5b7bcddba97358a627932bd348ab13f163d70ecc58daccde85e6881b284b051c9b935124bf4e009
04c3064465fd95fe72f32fbe207f001d2c817ddac97387463936587f5431742e043f9102fb94b02dc6d6481ab088d16f00bc
dc9bd7126cf95f01984c15eb75013cd21342a87268a7499bbf11d5a806342448a55ceb5a0397c7e10ebf7df396c72390e8c1
4291768316f62bf31c062265ec53e2f5c6a4c8fc8844ddb7083c73c418ac334722f2ae111b9415bdc90ba109c989971dae07
90f0ff4f11f57c2d2d7c567cad0a38ada771ba633cd7493ceeb7251f17dd11207d85558a8b385408b2f0494e57c71a7df77c
7a6618707d41ef2184910f16b6fbeef6be09ed88c98b7b807541628c46b2d09911f02271062191eb264782d309101a1e9c78
044abcc289f98c498a3c6632d5f41b1b3c6ab1b0a0164eef7f824b719e6d76b59910ccdb9421f1165ebcc0b071f142b3b215
c0db55c523f994bc2af5e4ba9e4a763c10d3bd33313bd94985831577d95f03de6d5c53389bb0e18a4c7a941679d2028aefd5
d0c12acdfed787cf7677970456502ab954da3c1e1057c9391574a3365d3300b75a4386cfa179035222532ff87d1fdb5a5963
c98f957c3399b8da431128b9b358d9d27c2d2d7c351037927580df766b26df2d21a8451a9c0e3050bccdf062e54a14461b1b
21c4d79104e239619700dcfb6fe84e0547bee9cce9fb7920deb7f62250c90d9a6f6223304c957351d77f4010f535cc4d24c4
9e21c30ac07a980639b46e0420932693bf738cc7bb7bc908c01ce67b6a099c862488f63a70e37a146d8cef5414c41dc4793e
e8f33eae27bd0d8da4027b34a3b8433f162e390a15d50c1e3c96e82766958fc69d1f4f9cb135eb2ba601896bb9115a9db176
161a71155512094f8bf42470bd1dcb1ed1094ae3d48fcf8e3dda214f67353468b16b2d6965e79e293720a6886a44eb28dfb7
aca9ad0be042207359563e26bf888ecae017805189c82c4ff15a7c2d2d7c0bfe333cf55f3cc98e7a5eb88add57e65144365c
1f0d87fc596f689c046033f81c139f8280b0dc14772936fef55719e01b064fc393e0d08c3952453569af9e67e05792832b56
88228fa2867e7d2d5d4ef355970d5ba4d77be2bac0bb661a7e9fe037d85266101568be765e8ee587f1fda4a800f175676b43
629c818698053c766bf1630ee1204d357c376288be9373555da3d9677a4c3a13d1cd25468211b3b2d636f3acb34f5001ccf9
4f58b8163cf1d409c575793504391288dbbb91e8d5d9cf89b0aa9e97e3677200520fef00939e5bf10cc461b8c1000577abb1
b8e7ce85950b3fd884ecae44e518dabbce4f37ec1acc257518e66af64bb31dcbf14309187c2d2d7c4e40e4f54fad62f6078f
5269710fe25e4f6b32e4f0dcbbc0a95fa773e398b4f1efe892401604e2f8f9a77f048c768515a3123cee96019a636077a0a5
e31fe92bab77915e6d4983812a8c768764692bc7ec870b30737407eb08090691ab0f12574d322ef26f3afaccb5e41d0babd2
5e45bff2cc2ce7ed8002a18acc7968ba347a732e2710ba528988630e374acd1e0b7bb6d83a81fecfb20418c936bcce02dfbc
06b1fa20fdcbc22abbb39c89de03dfa3ab81c7ad47709b27a63dc821554a18dbdca0fe4ad9a892464c77894f373199f30b15
1529c93790f219257fbe936e3dde7f11b6260c09de5f83ecb61390fc5c8cf86b19e5fcceebdcb09a16a033440e4a7c2d2d7c
c6c7f4fd20d681336932be0d5f118c84cba7788256ca63121dea04f9eef5f591f49dee9e9e1dfc720f19e0c9d46687e3c2ba
fcceb56a7491f26eab405cada6381214f3fa650258f2566e51af652b2d11b3a61bf3daf31107f47ea367d218692e4fb71d6d
b03e23568a7773e59f232424b5d016114f68c700675f1ee6e79ab0aa9bd626d09c7bbf369d2f39485343d62b0894eb361141
d50a457edde18f8f238e28102477453c1f6cb5a77287e8758fd1b40c7ecf05418c30d3160ccfdd08278fe5f826a218a342f6
0bb5bf25a03a74123a98336e4402081faea91e7fc270c68c14fbacd7cc64676df37461e631111d01594fd20a003f80540670
d0bf7b52eea27c2d2d7c6b7d855c454a814a33995018b122ea5dfea5580727f9e231a071fabe03a7e421ec966ea71ce311b5
b0b4aecea3f0e89e46bdd67ab1100a22f699f67295a741a452f183e8d4575e7095a650ed7b41607b9a1e147986ac423c2124
df00b338e8589a5e3207af7c26adee4d12b4ee38671af5ee7afcc9f579e39add4a37a4dd43f10489c9152110b724aec2034e
cedf7d2def68589413e068f7b9bf16684508a09f6436504c4f9a7c052da88b9f2c30eeebe214d7320486c99b013e2c00ba60
8f0959da272dd68bddefb4879c9841647ba734c027062eecee505dfb3d38c1c95998d538f3a0ee30887087a28e3869cf73ee
e754577ad95bb8b4572ebb2c8e07cdc57c2d2d7c6922cb7b34a1693698bfb28c4ce76ae6fe76b74e6362f471235dbd0488bc
827876155223c13a9801a9e08fe0762925040501d40cedbb8eb0841b2f6d54297b0621ab23da508e753682aed7b2e5277540
cf1a5a6f46da0dd82505c7fb26999d3134d8a15178fb1173d1be3c10124a84461a43467e5b94d99b63efc0b0528e3b3a51f1
0c4a0752b035d8c29c5fc31afdbe649488a52d78bc3e920da1444de5ed5f2f752bc422698ee833d35930d1bd95d7d10d33e9
a862674389b6501c4fbebfa9a72c04f16df08151377b02fe5f1b5ff06b84f645371df9470cc0b5a9eb44cd67002247529828
1471326a453101dfc93d500dc4d64c32f079487e9b2bd295dc91
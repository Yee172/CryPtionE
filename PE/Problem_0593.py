# We define two sequences S = {S(1), S(2), ..., S(n)}
# and S_{2} = {S_{2}(1), S_{2}(2), ..., S_{2}(n)}:
# S(k) = (p_{k})^{k} mod 10007 where p_{k} is the k-th
# prime number.
# S_{2}(k) = S(k) + S(\left \lfloor \frac{k}{10000} \right \rfloor + 1)
# where \left \lfloor \cdot \right \rfloor denotes the
# floor function.
# Then let M(i, j) be the median of elements S_{2}(i)
# through S_{2}(j), inclusive.
# Let F(n, k) = \sum_{i = 1}^{n - k + 1} M(i, i + k - 1).
# Find F(10 ** 7, 10 ** 5). If the sum is not an integer,
# use .5 to denote a half. Otherwise, use .0 instead.
# ----------------------------------------------------
# Analysis: brute force
#           Hint: use two priority queues to maintain the median

582516daba4e77b7c0646341d5c8af672b89bc4e3fb0cc1ab56de8fa1494c53fd7628ea2ab5b0c21a7816a1c000028e4ddf8
9f2cd22241e559de04ffb7b7802317dcd3b41e806db81348fd4fe4f097fa41226d0b320caa947197636403a3277f813c4c78
e73c85ec356d8cc09762e761c7480a1012b4861eec423801319ac593b5214fe22aed629bac0998165d1cac675a77b9f60b8a
9bc0a3391dc48c91130c4cb62ae4591e91d811cf7b1cda978f53a6dc5864076e31b93d3ad0b25f62c3581d872fe6e91aecc7
74d37a42bba40f897fc5c9539bb184ff318e59be237a1e6055f1e1c56cbef97d31e3a4581e3df84f9c6ed69a6e399839ac1f
970ceb9b6a287c2d2d7c7cdcc7e6d7b2037aa89968e4ddcc5f2b615fff255302fcaf3946d68938f98bc8be6abaffc913b09a
6564305a008eb136751493bbf6ca226013f194bc5ebb5aad3c5cdd0ac45629bf2747e603f4cbbc51f6177e58fda82f82577a
03e47426027736d868ecfa635ee950066d07590fe4a57e5648c6d70e4c55ce763349b3beec670fff30c13f0c00eb629c5e9d
1faebc147ed9917c6e0c9bbedc60a35a42e84f68d34f1c9e0fb29ae61cd4c777a1d3128ff3cfce2bd050f176ef59a28821c0
1c10b7ec42d3099016e32f49b9945c75b0e29036c77676359bff74e5be80b5fc472308e61e16a6d6f158e71db32226a26d13
be7267664455a79740233dba54cef8927c2d2d7cb32e70b4de93f7acd19b78f0ba80d7a324965c0c2e380fbe94b5180f4797
8d7af71b690796e171c73788c6d4a64b1dfecd2b3dfc719b8ef6e4648d6a1b23d3ed352dfebacab332c8c2d5df8f9b64df5a
a6d6342c47ab7c46c7f7098d5fd6d8d794424249255b656fda2ec9bc215054ed6a74f49b8e075442aa55ef2e944a1b6f67ec
34e091ceb84d892fa580d4ed6035754552350d20f96f6fb823bafbd99c61c1707c31d91819459f487a2cd94ef53f915870b6
af497b6a2ba641d4ab017ece5b067a7e203e56f21cb9c6ead37898b9e30310a14dc869793e32ff91b1dc0a956ccdb383209b
7780c745a0ca200d3ca515527c8cd7be9be70a592545754735b87c2d2d7c6dc7ecf9659a04bd3d6d297dfd23c063bce065f8
7ad1ee34e34580f65f91600cf7bfd92a30010334f030981b4f5f606ca805d3a93bff9cce35d075cb830f7a9b2a98e59385c3
645eca51c95da830104f99cd79dce5caf5bc75f46cd22416ffdf733f9dc434179259785fc72452f548f63ebc53ade517663c
ee47945ec068cd21953206eab28847d88a5d418072f8b2e991e13f18aefa53927d5b4bda48574caf0da82921412ceb8ae154
04037148854ecc71ff1940a7a10889c7e5f95e5ce789dbd7e6b41f9e91295cc1a8859d4815015f5fdfee04464ba11a7ce093
a5cf7800debc54fe88c8559b820928f964440ab07edb91fed7f6369b04fe02b7ae86ad4b7c2d2d7cad5dd05ac29a573afc1b
c77acf5070552b080678c7930cb5650e64fcb31dd0f2b879f799502e5e3e623a9ea4e0486bae65658c82e6cf42543c2ab81e
a961c5dc8c6bbf388ca635a9382c67b00b0006a652a48d1adfb61d0f0b3c2ff2a701c1a50f1492cc9beac55545f46891d4d9
0fdc681e8e1a787fd23fa348ed4fd0a78960ee18a766c276a97188d874cf9d6762c57dcbbceb4a64343de034b66922c2fb47
7ed696e723ab3677c55b47ff77070e878018083cb94b6af259914438f2a60c62ecf4eec04e789f71786a5cfaa34b18648415
98068f0b3a8a33132c6add75d011e4429061aefadd74c583f3870efed7d7b91f6bbc299abdae82b824d2a40d993f7c2d2d7c
0ff9fb46bdf667134c7fc2cebc2b5be22b3968b2931b995344f1db5026056d2a6ee1875bed3903deacb830a279448795ce61
d4bf53912f9f6f73c28c9bcc741f9fc1f05474778a37cc842f6c01d7f7527f3a421e1ed7c36787700b7ceb6ea6833552ab37
57fc7db3bda460b919a424ce36e7eeefff7fa61ba2eb535789890f271fc34d5c451b2fbb34c11cadaa65b2e524d8e5f3b15e
8aa8f99e7718896232e8eca68bd37fd7173f422b1f5b352fe258664207a146a07757660241bd8cfe56c24798027ad44e21f1
7cd6b5423929ba7d4db596c48b5324d186028c9b28220afccbe25191b73939c2159d54bb1cd87f790e895faeef162b08f82b
709773b4eaa07c2d2d7c970e471375fd03d91853c222e4b53bd652de25c3e28da0d5258da613b4b343eb195e159d5676e6f6
67bd77d18da7adfa46b437bc4d394e301c19c8db4f698eb5a9ea64a4bbb75ed36982c0b26f58505985f97b0c153d7c5d5569
e7ab2707694b47b46d4d06762514dd6170feacc850e1d5ecc64924955f142e7db81b634909953b79a8f172905dd17870e314
a712ac3a7696fb5ecf7c949cb9b66cd88943ab3b33543d50d3a7a34eea8468013abca800a247140f466369b8acfe5569b4a3
3038af78ebaa912d82cfcb2537c7140724d7802a2e81eb3a231de642bc569812101c3c97a910df8cc8f389fae86bfc61ed69
61af91420e67a4d22420f95e27bb53947c2d2d7c923440164f7004ae6848c13860c5797bc9ea25c3ddf65eab30bb1b048ffc
6a414a00870fc4b1068fc5436db97a9c479f38195a9554402e2b4d4e33584a8b934897fbcd90676a497befcfe127ce6c3893
32784ffe1c31216c9ae9cab28fd069f18b9e7a58a0fd50a93f2798a79d8bdf2d424996773a5536127ef2b30219ff03537017
983f5e9753b4125f9df779719bdc29c7fd3eeab2bc24de43cbb7b1ef78165dee24ac54033398b36e7f2f314f3d652b9e7621
c393beb870eb9213cd9e6d7ed9522fe581c979b61416116845995b36c37a082d1944cd85afe2fc7a9937938298ac1c0122d9
79b023cba556e10212985eac2f003dc44ce4565a294bbe9b4cb17c2d2d7c1f388ddfc9450eaebf578792a3749c478e234c44
cd22881ca3f6f7422997e5aad240b3a7a2ebe4c650e1bb52e5afbf8e787e3c30d5410f8c6d6e0c7e578ddf4a1842441af551
3846303ef34381c936db474029b79e2cda0c164d0517ac8d285d2d60bbe0d1ca4fe9b7579e95c28719cd20889430bf33aefc
9c929e0fa3c61d07bffc719fb08ee11b4e25d4c95c90c01aa7b885f2266de830cec5ae806f33c7a340da5819a74f570d2f23
081514d12c8a7aa6f991f6254fe98e84a8fe29d7073b6b2b16a8d49903aef3de5f372f828e4b5241731628b94647c0680f99
92d5ab5b6fa5a5fb5e7761caa8a0ca2b2dd9e55c89a44098bd31df026e4994762d61869f7c2d2d7c6d9d9e6e7d6586db4ab2
4937d6714ee901e869903c9baab9daaf60f463524cdbd539e5de445ab3c4c5923d1ec3f81e58d12b6c9aa7d12c76e2e6b6c5
ff3a003b05d0192c148a8961e15d623725cc34adf309633076d97ad3b3d39062d4ffdd96a91dc2daac96cc9f910427db26cd
5f3e20c2775b52e1e273fbe2038853e0bcbbf35323d249df76241db87223d31152792ff5be84b396ab1aa0392a4707479e18
2d76dadfbc4d0a13e55b5222f92f0281b80f512c5fd772b3b836263062707816a88fa31260392f422a6c165034e1fba60ef8
d4012905cc025ede6d895262016163304ba559c462d109f6755b8092959969095e4aa68c87c2e59e2ee6101b2a717c2d2d7c
a3501faf6feb4cb27a8eb64722078332842f1fbd75101935f6b81b0533f96908c6046d204f7399b203d832a373bb8ffb6b52
0e4efe82a18f6b72eea8d4e601af13fb26a5e17c3cd184dad8baa3fffb9ce1c90214e2d37c6b43c8783b2c269e51ded6cd2a
c6764211d434877fa956958e33fd98933bc649040376197900f8c602ded105e8e3f0c9d8966bad16b362b5e78717968addf5
26006620694c52b7b82d4d7aac5e4e1206bf191481da94d65c8a39f27c01b3363341e3ce53f19a9db118f046cfb47458495a
f1ec07bd20dc3970d94c6468d18f7f22f4776ecbbd80a85f6501f4283215b9fa633d3c2fccfd4cd6697e7dd43a16b09bd747
117c46711a1d7c2d2d7c0cf1c6e4ab7159740905b13b782845ba495da3be53058ef8fa517e8bd1cc7beeabbb25c2600f7549
0dd90cfbd843027a328bb55d226391a776e522f971956349079a3196714a646a23b8d3f8b4949b8df4fde7dd9eebc6bf2c32
e145faf9f3ffc54f9035308d786a832a7db3e16023a155fbe443b8141223a940266c2c77f034a0445a57d5b68be6b9c053a4
50a3b367616f7d852854eb585e7197afda70553da5be5b48d9ae446c0b18bf7a0cb9f08106247e66ca800071a037a8035128
077615bd130674f30cbfeb30d709a7a79e8d06b780685dcff903b0a27817714e9db15cf7a4d963fb06f7dca650e28e892be0
895ec5010b0e93fcb5d004cfb1503fd57c2d2d7cb54b37f19da8669094e1fc461cd5e116a9484de9edb5a7bd125effb2ed2e
107d2ba19ffec0a04ee6b0ca9018df721765db991709d8cefbbe9c046451a9ba96df8c72e172f1b5362e14ce9baf3850c367
078c6abe4fc26633b487561119f5c1fa42791f983830c0f0265ac2c9b905f84879ee69b7b0fc6f54986e7b017426cca15319
4a998d523b31438f233f0cc4161cb022f1de37a2d6dbb276604f2d81760390cab02a40f2fe713d1dc3f1fc6a65020efbc768
a5a07ce7f0edb91de261ad9d0c6d17b048488ce9e589ec564b7def1b07c001967926c570d15007e87dc8bcb15c2d38743d69
991dd35dd177f588fb2a24e9eab9ef59d2bd3af7b9dd20353f597c2d2d7c63397d8c1a97ecbdc2e712b79433281bc3268fff
579cfe8eb1e8ed05bc65d59545a707844f7f109dcff072292a439be990c88517782657ebb21b93ec5ec280cb6f7ea0d2f1ab
0807ca00cf3728867b95c023f80ca5aa0b7ff45a2eef36aafc80f541858d5fd3fcbc68af630886e66809e1ac422c758dd701
034c2bc0f0841c69b3f0aeb847df5f76e5e60ec80a2e150682923b950144db815e605cabb060eb887e015e6376f60811f705
4d4b0b4930ae04503576b33eccbb87e8bcf45c7d2ee44a23443a082cd169f9bf240679c1133ce3b8c1f6c9e1cf7707b3853b
98e55c2fd85a8eaf13beca025f8a3a7c121e7d8206ddd2352994114b4108bb4bf458568a7c2d2d7c94a9e2dbb846964823fb
d1ec2e0f893994f63505a08dee42e29922774764c7c022a1d3c0f5b748d2616140f419a8d2f68aa0e6de73c28d6d661b6a8d
371f8bf7c97eb283c7bc0e3ede56ad3ded87473751dc91060304887f69b482535bb26ff191fe471cd847062cd43e2111d225
133a56be2116b684feb0a34f68a68c37728be447b548c58e5e39ffe8d1b515358222a5f8d5408bcff7c9768ce4b9c8213b7c
3911618be6a3a292619bac778964581bd4f37610e20449c438e20b06ba7230c7dc3caca1aa9ee655184d65e9525469c12ba9
2734e0dff6a73ab7ab88cafd17100f8ff8a72f9eb18b0ae2c6a5ac7e08bd18f62e81b4021352ce36fcd24d9d776a7c2d2d7c
b1ae4a5e7d03f00c2a95462842e9b4319d8c02c6969a0c6446ecb2b92ecdc08eb707f2a0ca9f3d68f5ce4679dda0ca3ca0dc
664d27d1281bf7754674474f6485d6842c3b869253ecbea6a7147318c600e42fd354e9a0d7bc32e5c64a480af003ed7bfe70
71941d75d10f382710072cec5b35d29bb63c0e36399a1c75da6460489efe173ccd5efc97cb39da3c0ec2beacba38b4cdbacb
c66112eb4d3082c99dccf707c7312c1cf856098679eee3ae3515b86141f279110f67489ad5a2e87bec8d4458318bedcf22b0
c3697706d20d77d184a2dde5accb2edf4058055dcc5104cc8a67b3397b31aab469afce34cbc89f92c6d3e01d136109feae10
07af7ce3cbd67c2d2d7c2f324c5f1ecab46f75bec4350ce90d51c91763696c2d9494698981bfe370c075a7f74e49beb58955
e9d190433256cf01686c212fddb2fc9b1a1512ccb7fb8f19b762d9188010fb6b072f540b50333ff577c296ee2a119c09c5a9
0f14a65222fbb45c90424e68e0e72ddae700d863c9e61fdc29ed28fa4ce14471bcdf72a876b608cc54eb160567f8f5a3a7db
7aabfcf85564abffc68fae566588d1b19caeb1bd526610e6a2a4cd65b9ef47320d438704d03c8c0fbd3fa24d3167ab46de1b
bc74d08966ec8de5654cb277b81c6299a6407767292ccc9102cfb43dbbcba0c16684836da3895918fb01aad4c12297edc582
11b1df3b5f5b88db1dde35b212f39f9b7c2d2d7cc304f4607e59a219254f1a8286be59896425058f96e42c0567de24cd711f
83d23a48a45f5b03229b62f2294ef03468fe4254f2cca8d648aa24cbd7e8bc8eaedbda823c7089ed9b622f5fa6a69c025922
fb6f850ef577a397c92cb2885c9338e2b50d747e0ce1f85b0fc073a0f56dd537fddc268885924260ceffcec0254c0a9223ce
53b30ad1dde28489eeec7140a44cc40bd8bb9c986f82a1be70d957e72751c25ea9a1a0ae09d6438fd3ef9934ce4f800bfd7f
4e427a85bcf2f43f6f507ffc270b7cdd2a2adc5367f3f099ad47e2bbb3cac425f610b9de9b0e353c17285d8de675f7a0bd8d
45847036a01e089b1b95fa13b048711053a16f5568bf74f00e14
# Let g(n) be a sequence defined as follows:
#    g(4) = 13,
#    g(n) = g(n - 1) + gcd(n, g(n - 1)) for n > 4.
# Find g(10^{15}).
# ----------------------------------------------------
# Analysis: brute force
#           Hint: calculate all gcd(n, g(n - 1) = 1 intervals into one step,
#                 that is to say, we only consider the next gcd(n + k + 1, g(n + k)) \neq 1 from last n
#                   gcd(n + k + 1, g(n + k))
#                 = gcd(n + k + 1, g(n) + k)
#                 = gcd(g(n) - n - 1, g(n) + k)
#                 ,where g(n) - n - 1 is a constant for a certain n
#                 Every time jump k steps to find the answer

63c4e74617ae5b1c41dc864863fb9be6d37afc002ed0c028940178dc88f0204c37a81f94b251638f46931e439d2f6c3fb23b
080f304207a5cde28d0d9b9f7025deef0bfa3b9a03a6fbd9894900126b8f3b9f04ce5015c7439efa0c405e7a371448294e0f
07d2faf6fd6ddee165510828f485eb46a30bf380441ee5d9ed276e9cc19155488466a2e26f96fb06b4a6f156e3409fead8fb
f58b65aaaf6d70e5e0004a9e41b2bd98e15ceda9a9c2aa26a9a22d08ea9cb8704157f8fa4a59bb1cbe2bd57467539f8b55d1
31ba9fe7eec535578608eb2d1f0a9f3d1c69d83c42904b71c131a22e51be652120a864af21b8e19091c34f055dd31ed38e16
570a6de80d9c7c2d2d7c4b7251eb1487180368ab33c0b6450ab395be06edd32a40b4651b5e0ece3e0113c0b4a2cacd97ddbd
e138a4a8848f2ea446d54b8ca0c0ba3ed21086cfce92285e1f7ceebdef4e585eab2cd10d72c26fcdda69cd6d2bf7fe7fef6e
cda573a7e79d2bc91533981ccdad45aefe762fb51fd411bfb63668488be99184be0a901aa02f4d6324483bff1030de74f32b
82f96f062bf2e7cd0cf1231478da3afff6736624c73161c7e771b3c56d3ae07125818b5275964a7c3dfb4046fbe560cd8e42
809dbc2c1ec1c056476092c463598225890dd53af9ed70dcfb91070a6d6f7e87681d694c15f8f5f700b2c1c0f6191d0c2b0c
407d8a94e4d62a9e190165e8658fd2d37c2d2d7cc193c2d7a31bbbb156f720178bd2caaa726447ff599d5861ee7d04649fe8
32ceb6bec01eb85ef6eeafa70e1665e76ff6c5751f8ccd8d91e4dc6c66e5a5179006b5fe09d38a693a17d4106618b89e139a
a03e4e57f02e407b2bb65e925626fe8637c61e606ffc0b96663372398a446945964f46e8a4e093336c095d45d58948fbe3c0
1b8d4428f8be1ae208ffef3c177444d0d62ecceafcd818d88e8911914aae0c40a66ab8b8f11f494e6106cebf823f929bcac1
7112aed09e6a59892c9b7dd51c406f21878ffb70325e0b45f6bd89f71f96837bc175fcfbb8dc3c72bf8dc3ba2c721eb4ed7b
4de5a9d942bf2864ee772d22011b40423e9b3380d01be77afc887c2d2d7c8ab36c3afe663f637302a5997e1fc3524ed77689
d5249f4ef26cea4e7cc440f10dba252576bb2900bbd30d937c4a4134cdc666d757ba8924e7128f566fb59b5a3669d693673a
7c733f517197f595e8f5560177c9d7f595b487cfa6028a7e3e07df4e1fc5c447efc3b2d25b66b4931e7a893c7b4d0b6fe844
6f696d4783fce0717f930ff88dae2e8d17b4572e07381bca9922364144a123bc9d0a2765089074cae3e1f5e8b58ec37732b9
43e99be61941abd7ee5c57956d40c0633b53dacd2579c685ee235cfa3d65d7741ccfc927830f8b997b2e941594a3fbc289a2
0de5a1982ea5c82747034159664f2a8ab8c705eae5cd8f8a0a200f1de674d235ca645cdb
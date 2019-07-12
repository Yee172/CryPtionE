# If p is the perimeter of a right angle triangle with
# integral length sides, {a, b, c}, there are exactly
# three solutions for p = 120.
# {20, 48, 52}, {24, 45, 51}, {30, 40, 50}
# For which value of p \leq 1000, is the number of
# solutions maximised?
# ----------------------------------------------------
# Analysis:    a^{2} + b^{2} = c^{2}
#              a + b + c = p
#           => (a - b)^{2} = c^{2} - p^{2} + 2pc := d^{2}
#              ,where d > 0
#           => a = (p - c - d) / 2
#              b = (p - c + d) / 2
#              c = c
#           Then we enumerate c and p is ok.
#           Since a + b > c, we get c < p / 2

143228193dc6f630e4cea88b9d1d498c3ff843c7aff743d615d0ab63da95671cc12701803b6fa097338f0f6e36813dd19c35a2bbaa6ebed98c681f5fbbfa0b7178afd7aa51897ebad0d76b656976a3b85e0bd0674e0ec4c0c8584fc730513f08bc9435878886aa6b61329dd0a70d719113ad4b430b2372c65e9f3159f05dea51870d2cd4922b4235603e58e705b7cc7075708538891b5ec4eb60b9845b37882b34c3fffd01468cf06e9c54d908ee8481433106ba73db28b998e64b302a47e9ae81e2f040bca335ab221e84cbf82e5eaeb22f38fb0f21cc081fad818f3173c4d91a300c0bd42dbbc36a718221d02cf1afba45afc2a492c3442d7769b069328fb97c2d2d7c0bc3b19ca41974bc63635faa3b7d8d3f1fe047721ac28e8d7d8be6ae19848e3de10d5f1f16b4b8d133f55c66cb6551bfd6da444eaeaae9efc1d6f9d8bb0438440cc342acfd59ca72a93bcc7552ff9b35538e4cf749152592e41ed87784754640c8edb69f3837223f693e621bbb533a79dc81ee9601c1668b0c206d6b046ed945916d527e2ae24573438f75dc3b09be632c82ebc58a03cdf4b9dd7e750a26a4d3252b3ed705b65ee9b5e7a78b568b966c4f4d88cd5cc1a5c6370b854b84471a4c4bebc2db9615d21871890e560e680c758c968096542809258632606e9e71d1c0bc4fab81244755fd9ba90c7e0feab6cf73eb7fdd0b6d2b9786285da9ac1e22a6

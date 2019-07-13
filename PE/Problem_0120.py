# Let r be the remainder when (a − 1)^{n} + (a + 1)^{n}
# is divided by a^{2}.
# For 3 \leq a \leq 1000, find \sum r_{max}.
# ----------------------------------------------------
# Analysis: brute force
#           Denote A_{n} = (a - 1)^{n} + (a + 1)^{n}, then
#              A_{n} = (2 a) A_{n - 1} - (a^{2} - 1) A_{n - 2}
#           => A_{n} \equiv (2 a) A_{n - 1} + A_{n - 2} (mod a^{2})
#              A_{0} = 2 and A_{1} = 2 a
#           => A_{2 k} \equiv 2 (mod a^{2}) and A_{2 k + 1} \equiv (4 k + 2) a (mod a^{2})
#           Then, we can get that
#              r_{max} = a^{2} - a if a is odd else a^{2} - 2 a, \forall a \geq 3

54766865cad8d89392ebe39330e85205084bfed41671079bbdb1c538bdf80f73ca2cf1698bdfea088a5b8a1c737dc5c20aad
8133ba3db85ff21eefb606faff4bee6dde51e62eb9d2037a2d2f9b4eefe83a805608af1361a5bd7864edc7ac0e18f3b2a6f3
b199aafd2196cc7b978d8a8b8bbfa3e91c0cabc8e5ad4772a9922a5f5c51079ac64482954ff8ca460417f61e1613a76eb424
590f8a6f331f5d51fb7662318a3512701706330a3c53022ffe48a92fcabc6d7005fc46496a376109cddb6367c78915d845a8
b13e0fd448af8da83bc42743ac8611b3f4e09051ba0f7915c70ac352215e69562e9a0aaaf7305e4c042f95d21cab549be3e1
9a5c36cee29c7c2d2d7c1449d89a4411cc02b9f958746704c09d98ae1b588ead313cb942c1a35b8c24695409bc529b379675
aa4baa56341de5e6792f2c6979e6ce04fc1d12b60ac6e5a0450f275557353169760be064012aa08187900e32766c263076b9
d0b8b0291e9d1422959d0a3861d16e60b75ec405459eaa82fe140a4d7f5a0049342937346b4c9e316e605b56b326831f5a2d
b3d7941fe68e2555cb777656358fe0bb2f4b79cab184d0f8985072f18eb79d9f0db4fde1101bd4dcf692578c9cdc68e80543
b319adb808ca1c212a4dd96e7283196c16187cc008442c854151fb60777a98a6b8151165724a51e9c0487b63b4c109212852
15fb32610fdf59fc07876e73ac10d7d6

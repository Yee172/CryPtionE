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

1531d4ce9d45bf2c8782f17ec254e6c90ee9bebb726763d5f830039361ed24d5cc32fb9e51058278e79a222a903018350790934c6eb62dc558ec69e22cbdebb02c9b9a8b1626069dadb48f99b39ccbc9e32efa6770242f10c4cafdf0da603844a9e5ac9587ddaad54dbfa0f81e3d68a3c74db06505dadf4d53c5c676804e1966e3a1adf9ae7ff9877372764176a22786e9cd91febc9dd294d201911a3afa0a2c43eb1e3debae3ad7a4e310816817de54df1307852ec6f9aa5606c55cb0236236a489788c76dd3b909c7a0c811afe0d64518eef6d8945b9d0116bf35b3206ca41c19371b3584ea28b96ab56e40caf5a6f6c69f46820f9ebd5a291f4db5c31073c7c2d2d7cb4a5f3375014449225abf46bfda4f47dfdc2702938f5dc95b37ba45416532e65f04057f0880fb1da883dd01f2803e866d0694c882e41460cfa62d633027fb3e4916d684a3849894fadac77d47d4a1701899075633f2c4423b12d050b7b1d0826bd5f96a976cd67ba77df94830116f5621cdb78a92c94fbe48bc6273e64abc2f30dfd1ba18a5e14245b8094924c6ada1895644faa7dcb3a1a06549026a49e78bb8ad4bd68e01e0705b715619ea13135588a24a2049bb30eb6a5655ad4c600c02c4050fb1c67289a42575c43c5203523a585d2c0741c3a9fa497252a99eba44e04f093e6e44a95f75812fb30f07b568b22865d03a536f4cc337c2562d8b98a1253

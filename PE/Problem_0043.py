# Find the sum of all 0 to 9 pandigital numbers with
# the following property.
# Let d_{i} be the i-th digit, and we have
#    d_{2} d_{3} d_{4}  is divisible by 2
#    d_{3} d_{4} d_{5}  is divisible by 3
#    d_{4} d_{5} d_{6}  is divisible by 5
#    d_{5} d_{6} d_{7}  is divisible by 7
#    d_{6} d_{7} d_{8}  is divisible by 11
#    d_{7} d_{8} d_{9}  is divisible by 13
#    d_{8} d_{9} d_{10} is divisible by 17
# ----------------------------------------------------
# Analysis: brute force
#           d_{4} must be divisible by 2
#           d_{6} must be 5 because d_{6} d_{7} d_{8} is divisible by 11
#              if d_{6} is 0, then we get d_{7} = d_{8} which is a contradiction

66e81fe9c2ccfb20d0d3dd215991c374dc3f563c547e0f940ee4b587d297f221113b4489f645129e8223d005b7dbb1ef254867196a880c0479b53dadbfe4ea44fa5c5608f463accbeac6150aa590765b877ae88e41b109281e826f7e5a6717d27102664560cdf14ab614e453248ba7cbd53c9dd2d596b43eaa49d364b15c160357679b7930025bbbc6fa7b377d36e9d9df850655f34b474d91b0acc52746083dfc69c141338b5d239caf78d06573f3f6a54a8b0f61726898ae805fe5ea0fe73f2101a54d29b41f3059628a997da3c26d30dbd0aa257b6f46e683bcd92008816970692c47f6fda8cb509f895d5bac6665cea41cb2a8e1a049d5640101036e0d647c2d2d7c9b6f81e1d3b1ddefa71645fc9d7b61ac6d963d623c3121952409c28f9cb1361530910b0bc1bfef6f2742863158b4d87e8753b99ae616c04fd076f89f14080c026ab6ebf109a8405bc21de2f11f07ec989e3e7528f499e01b12d365ca8f513212ca6d9fe3e73e7281f0813cefbe62a7cbc7044a0d0f33d8f935c7532da343822da311d93162d452d6946082a90222790de13e3b8f722ca1ae7c24278c0b6ecd354544ac421a719bf9ce72d4365e3872d4773b1b3d1fb33ab788cfc024769da9c3bed103217f28a7b048858d08ec38c22d24fba1ccf2f13b23fade42114208b2b24fba786043f542f390dfc8c1ca2718200287c279081f103e289b928e1bd2e088

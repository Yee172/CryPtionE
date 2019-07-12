# We shall define m(k) to be the minimum number of
# multiplications to compute n^{k}.
# for example m(15) = 5.
# For 1 \leq k \leq 200, find \sum m(k).
# ----------------------------------------------------
# Analysis: brute force

c9ab3f708c7cfda31e53b86eeee54261c1b6ca7f50ec8c0fdaf64ab35a107ea414963f7d2a477d86f1bf31140ff98524909f3c8e7160a21c2a5e6d4e5178af08f531753b538ade44f7002de70ff9e6ee299166d3dc28556f5d9e46b8e2adf6f01027b95d01e8a8b29d89fcc2ca9508ac6c7bd1f2a037d529c33a4dc9696ae6b10a2db7ea55af934476412ad799dad8847fc8a1562e3ec138d1e144d57007ab50dcf72366d0286d8bd3c1febf028fa79958e413565eb4cd7a5de26d52b18110519e1466b77cabe331fa2c40394becad203de57e8aa336ee540aa532148bc4e0a190ac72d56475b27a83a2199048ade4a35c7736b548221238e2ede3e0602e009c7c2d2d7c72ac6d6091c80bc1a79212592550ce55dea666b689f97cfd52fb9f384e91e3fbfecac911f060d40eaf9524980bb28762126cb1c68fb3f31b03ea8ff6d02b9a2b837fef0b217aaf86f09c45b59601598627c779dd0f53bd4c61be1d6b1358277e89075d1232ba943eee497180e96c34eb58364ff8af7d2780c6a3ab951a38dec08e2c279a1e5b8db8de37ff4e9622584c549e390689cd147cbc61640f5767cdfe9ed98d32c2b797357ca84eb40db3e40c266729571ba995efbc7de9510ed02305134edcc1e3b2c701224d089789cb006f88e4eed69d2cb97049c25c20015379e38176291956fa996e05b44842e6fd2ab775c4519e8e7174a358948b43e37e5ef17c2d2d7c99455caa44e8dfc8e148e1ff910187ea1418c7b0c87820447a000e3d4bd4a265cbe62b07bb5fb36a77c814292e5bd6ac23256ad80ea17501341672d57de12bb96ac61da72a95cfa88eb0c03d1b860808afc1f138782842490b835f5a4692780caab3a33fe456430b4861d59b28de08656574f1c08971dec0674a2fe64c264b3225d937ba959181961e6f44bdd143d699e3ba3f5ebeabc06630bda35cc7c72bf21480fe2addb8af10b619410cb768796d7993fdb9a24c8cfbad713f3413e3bedd007afd876e4b82931cec3f8cdaae2a453ddc3da55a8c8700b42e63c8977ba88ae926741d6a6bb4a48de43c1ea57c464ff03a0a2553e4d24c37c2a7cdcc916c197c2d2d7c7705f44e857befed68e4e322bdefca0f68e01c770d4dc5877d7ef863e7d180203cabb8b0cab78e2c234a21de3c9db171c0b1c7d4f6a622fe754ecffbbdc160b17543cd14a0c0b096c8c7f4adc7f4574dd582e0aa9bc2050826b7d0ddd5aca00d5459157c0799013a0bd282aeeb9c493392bee275cdd59876336ac7542024d6f13d5fffa71d8b75d09471caba24bce860a14e0e5f42ee6ed5d7c69b44cf4b6a7705e059517ba97d9775667330aa9b7d8ffd924ce0fcd1aa3b0fcfcb99348c48fe609cd468d06b6f9302feaf4362921c4a3082c3ce454a28096c112965ef1d4913f67de93883faabbfabcc43796f747122a9054338f465940af7e83dab5d71b9f7

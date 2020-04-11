# Every day for the past n days Even Stevens brings home
# his groceries in a plastic bag. He stores these plastic
# bags in a cupboard. He either puts the plastic bag into
# the cupboard with the rest, or else he takes an even
# number of the existing bags (which may either be empty
# or previously filled with other bags themselves) and
# places these into the current bag.
# After 4 days there are 5 possible packings and if the
# bags are numbered 1 (oldest), 2, 3, 4, they are:
#    Four empty bags,
#    1 and 2 inside 3, 4 empty,
#    1 and 3 inside 4, 2 empty,
#    1 and 2 inside 4, 3 empty,
#    2 and 3 inside 4, 1 empty.
# Note that 1, 2, 3 inside 4 is invalid because every bag
# must contain an even number of bags.
# Define f(n) to be the number of possible packings of n bags.
# Find f(24680) giving your answer modulo 1020202009.
# ----------------------------------------------------
# Analysis: zigzag number
#           Hint: Entringer number E(n, n) = nth zigzag number
#                 https://en.wikipedia.org/wiki/Alternating_permutation

a9abb769119453200ba2847880abed3b23cee628d2b79fc3f72b1a8d250072cd26675a9f95a2910b587d7c0719f99ec00d25
8826ed888b6fdc69daafb4401ad94a3355b559068e6d0890c3a0414e5f1e258fc352b5124fded244b6072af119ad970be015
cce279bf584b284986881a3a3d49fcb62ccbc55f26fb282cd6e900c06363589cd5273880beca21e501916a8cfc752b4ee84f
7459bf3e9805f988039ccb52a0da3f408a890fad65c38faeac34c241f8c6ea934a8f89ce1e7f89e470e052cda1340da4b3a4
575bce4d0763d668ddb9575b34bf85eeb11476d93c141ac19f0feec16a288f155b946b7b6d0569d93c480617708fcb0ef322
7a0901eb6de47c2d2d7c116aa07b33cb29f99dc2eaf5a6ae5039abfea7620257d2f847ff11c446218a2e6b406845ce79bc29
71451eb7760db5b4f53e618ee481c6f12e31fd8c4f9d9d758ba91331be926e557e73642d884e1ab578390b8a6c3c184366ad
cd52c9dd234023497b1baf4d79557afaed6ed977dff380c9ac867a61a67fa0b5a9d6252912be4b5dd9a68bef78cfeb6dbfcb
ea37ede02121697f2b7431b99d66b68cfc3faf674c86b754a9f412e1347b4bec59175361a023e419fe09140b87238fdc6823
1a056e69513440903ca078e6b21754f937bf71a350f76fad2f2661a67cc8599e140b25510377e17d2bbe5fd3c36905830499
dd6610f093afa80e0391e143dd468936

# When we calculate 8 n modulo 11 for n = 0 to 9 we get:
#    1, 8, 9, 6, 4, 10, 3, 2, 5, 7.
# As we see all possible values from 1 to 10 occur. So
# 8 is a primitive root of 11.
# But there is more:
# If we take a closer look we see:
# 1 + 8 = 9
# 8 + 9 = 17 \equiv 6 mod 11
# 9 + 6 = 15 \equiv 4 mod 11
# 6 + 4 = 10
# 4 + 10 = 14 \equiv 3 mod 11
# 10 + 3 = 13 \equiv 2 mod 11
# 3 + 2 = 5
# 2 + 5 = 7
# 5 + 7 = 12 \equiv 1 mod 11.
# So the powers of 8 mod 11 are cyclic with period 10,
# and 8^{n} + 8^{n + 1} \equiv 8^{n + 2} (mod 11).
# 8 is called a Fibonacci primitive root of 11.
# Not every prime has a Fibonacci primitive root.
# Find the sum of the primes less than 100000000 with
# at least one Fibonacci primitive root.
# ----------------------------------------------------
# Analysis: brute force
#           Hint: see the post of ving

19da61e136e8cd7e6e3abbc11212e0c7b57f5a54b85af30ab291b0d31641b545bc90475ae88e60a24db39430885ba4b45fb5
0b0086b913f19dc2fbda760d4c6d1604ff93cd34b59deb8cd460790bfe336cbe42bf4faac6815fdbfb24ac071bdff2e3aec4
66cda9b5f335cf9ad1686b536ef70f8e0407a29dc5f6a531c346452da7aca4fa1a1286f37e54ff72d8f1a0084d0c08326119
a4e482f87d94e0053dfb63659ac4d3461882d5aff76d47cd446af31bde70c6b824b58350145abdba024f72e7566f12f0f017
5c67352a13e48ec0d4554919bd4652df72d9b67c6fa699caa86dc2fd2bf5cd2ac37bf18f071894afb9397c342743c8d43218
e6d12d4b6f4b7c2d2d7c9f7010d72a035f315a1d2408ddc511e8ccce1a7504d42c291e11ab886709e090c53ed316cb37ea66
0675d781d3e128f1996dbd84c83d18beed0173992ef8dd85060f641b2f8053ea4c94447fa5fc73abde495a87ed1704cd01bf
0b4877c8b0566cfab5a08a1c6e933ac631a454adbe17a9502ff3b6ce1d5e59fa3c31b06bae04ee50c363ba4567d899b52c59
b56b01fd864b57887b793859718c5e2f2e6458c8ec34af22d3f22260eac8ecd1b9766c13ca4664ae7090aadd63691a035491
005033f879d96dd536c6bb4f21c4a5f8fdc1018f5973b54c24cc97c5a901151ba4094a4e958683027087565e42be405f9693
cab5eff677cf10ef0163f388da62b5037c2d2d7ca9e2d693740e5c7ff0c719580392e627ff602577be5f0d0c80a6356f7efc
23dd6c521698fb72d99183dcdf98ed2cbcae2e859eb79fc40e1f79c089a934cb2091ae00abc73441b80c32852ee6b21215fe
3179502168aeda98301b06f24480856921271a02f410b338ffe8f76ccd55782cb042d0aa249bb2c8a07d0c91ba62915f4672
3a3eff3e35a18528e378df510827f0ec41b9484dab642281c8f1b889720f313ca374a611933934c982d70e71c7225a706add
b095a960b6ba27edb7276f190798646d992ac32f1986548e0cafec1bebe4f6a087e29124b2431b9e0478fa238da82b3d2984
5bfb62106548b44f56f8eb5013bfd7b77bec5b748845de34f253

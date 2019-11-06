# Here are the records from a busy telephone system with
# one million users:
#    RecNr  Caller  Called
#      1    200007  100053
#      2    600183  500439
#      3    600863  701497
#     ...    ...     ...
# The telephone number of the caller and the called number
# in record n are Caller(n) = S_{2 n - 1} and Called(n) = S{2 n}
# where S_{1, 2, 3, ...} come from the "Lagged Fibonacci Generator":
#    For 1 \leq k \leq 55, S_{k} = [100003 - 200003 k + 300007 k^{3}] (modulo 1000000)
#    For 56 \leq k, S_{k} = [S_{k - 24} + S_{k - 55}] (modulo 1000000)
# If Caller(n) = Called(n) then the user is assumed to
# have misdialled and the call fails; otherwise the call
# is successful.
# From the start of the records, we say that any pair of
# users X and Y are friends if X calls Y or vice-versa.
# Similarly, X is a friend of a friend of Z if X is a friend
# of Y and Y is a friend of Z; and so on for longer chains.
# The Prime Minister's phone number is 524287. After how
# many successful calls, not counting misdials, will 99%
# of the users (including the PM) be a friend, or a friend
# of a friend etc., of the Prime Minister?
# ----------------------------------------------------
# Analysis: disjoint set union

016214d87d7062bf6431d3406ecf3be1b3a62c3050e07bba43da9417dc87027e9d91b27a2142fc73722a5de4ae2061cdd81d
0130ff8404b4ebdb46bfb7d5f06c20f9f9e0967bda6f07ce0c999b53e3572b418d500272af5fddba28046a32107355059b69
2db0b94e118c95d286a66ff0fe11ecd2c32e6a8468b508ceb00a6edfe7b10211054e9104aa283c9b129516951910383badb9
fecc7fa183be2eb4198309c1c79b95d466d7e1ffc3877c05a29406a4df4e4bbba3d6459254bee33fb33c869d9ba578819b07
a35698e66ba4cb783be1e963b6f0f37efd9ee1d7e79a830731104654958bef2afda862571bb43e6a774538d81b990b3dde75
22c3483bf0287c2d2d7c8841bdd59bc07c653d729c2eeccbc0336f5073f6a34a4865e00c61291467bf8229e0e0ed783018d8
2646a2e34b73cfb1ed45bcd26091c8a81959c24a272d152aeab39be7d0f91097fadc35a5e86a827d9eaf8726d83aa8dfb437
ba3b4c5a742dbd55b40181e48ae69b07d1aac629861324f7d0479312688941c54f5c58524e844b42e18a10748ad4ad7a15be
6a54526db692e7d35912aabf71e5d9ae63966efbf380964110019363664d29d0f5632d5d917031708689aa05b288b861fcf0
1b20f06445ddaa76b154643fa653b214046323afe9b83e35f35853a11086d639c3b5848ecfd6bf80e2f81281b577e4b3f580
a2e97a63dac1dd9e1681ba63a74194fd7c2d2d7c2dc95c7fb44dc6e50f55a3e42d9ecad9315275ead6c9d7713b444525b31a
621eda052211d4af5c07ce67dd82dc0b2b1c2b9bda1368c627923da78b7223bda2aea5e05f5deec59dc9942cd99807d4aadd
23373ee43caae720a430b7aa886505c841f47764ba12eeb0437df55c1797f772599cce8d4c4b70909d7f82db046f0606f835
eb84a96d2cae85b8371e468075416a32d801753d9aeec9e4c74e0034c9a6e15bbf3a7a43de33ff3fc554bd59f23cadff6abe
46c823aff700440d70eecc45d8f88c18a61a994939a72c480760fb0374d8678f2b6250e2d76044a5e4aaf1736cdc6d3ed7d3
feccac835a446830b99124ea0ff874da7644ece73132866bbe83

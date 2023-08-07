# The RSA encryption is based on the following procedure:
# Generate two distinct primes p and q.
# Compute n = p q and \phi = (p - 1)(q - 1).
# Find an integer e, 1 < e < \phi, such that gcd(e, \phi) = 1.
# A message in this system is a number in the interval
# [0, n - 1].
# A text to be encrypted is then somehow converted to
# messages (numbers in the interval [0, n - 1]).
# To encrypt the text, for each message, m, c = m^{e} mod n
# is calculated.
# To decrypt the text, the following procedure is needed:
# calculate d such that e d = 1 mod \phi, then for each
# encrypted message, c, calculate m = c^{d} mod n.
# There exist values of e and m such that m^{e} mod n = m.
# We call messages m for which m^{e} mod n = m unconcealed
# messages.
# An issue when choosing e is that there should not be
# too many unconcealed messages.
# For any valid choice of e there exist some unconcealed
# messages.
# It's important that the number of unconcealed messages
# is at a minimum.
# Choose p = 1009 and q = 3643.
# Find the sum of all values of e, 1 < e < \phi(1009, 3643)
# and gcd(e, \phi) = 1, so that the number of unconcealed
# messages for this value of e is at a minimum.
# ----------------------------------------------------
# Analysis: brute force

aa8ed1b7ea177fcb20b52a23cdb4f8a5f485554a387574f01baf38dc2960896cb381fa0cad59395b18034f640c31af8c5eca
b226d8808b383fdfb95aeeffc7e002c885a83ce5bccc84978397a414e96ac60a5068ebd0c2c3079dce7ed8ba3414622681ca
43ef8e1b6c88f96187ce1ce84dc1bb0a6dd2e3f5984e72bddcb817e6777a343a4266a2ac85b33d145d395a196dbfd87f34ff
67a29bd23f06fe50e61b1d8d197fdd37803d30e5fcc0bc6152c88532f5cc543e04b9ce113a287cc5e709ba2e4e58e4a5e733
584fa2b89ac97a159f7f39e3a6d2446d9eeb27d2f41e53ce8a8a2a9d5407b95ac0e979300edb57799a5be9c2d8cdb581f661
6f6d39d475b27c2d2d7c6f1f8ae0123a60dcd0d901357841f38f23ecdfca8c6a57806d947bc103b181c2bb8c7900a9db657f
40f8126e0f7c10c2a8a0da28e36e391f538bf2a7600518b2d7b612109f7136d6faa179f4e1a21f6c47c250d58e9ec2500879
804a5e4b7f3d1ca4414dfd5247c222ac3c3eec1a57d78546c072ef41eb85d1d7b25019bcdfa440b7c8038653f2670f834fd1
edd963e12f5a5b82aa3b0a2884eee30c7c95570dfa6d27f546c95460525245f613d8946e454f487ada4c4fe5e4cd1672618f
3ccc3e2bf849837ae5217478ff529001769c38b770b479b0e49b9861fe53749a087851494df3cca9ba777a2fb8d973242d81
621e6b52f0aea1f70063ddc66ff291c77c2d2d7caa631a295731ed76f3715f1c71254842e43d4bd3f4165e482ee7b7cf5dde
45098bd5b5d9ab89dc932247e581f738cbf82c6ee8286c40cf3c318a4ad25bf57a0e69c1129cb7899992b371205fcfff0e22
e89b9328fa8d5e84c11629b53dcd6a1d6d180bf1a392b3cfefbae803049d462ea5828f04d6aab8e48a34d7b02a521e1a046a
9fd9ad178b34d9a5aaa3a2fb8c89d05354cc5437e4fd01cd1e65f64d1182f9791dde0e51d4e298788eb896ca6d4934a22681
063bc8d4c888f0a1be60cc110d34c1446e8efc2a31e44786f03dd783b3e1ce5e32b38bd36cf2c868de24b10a6ba98fd9164f
1e18accece6f9a2828f707af0e28e6c9dd65682109990c7bc5d6

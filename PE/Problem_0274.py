# For each integer p > 1 coprime to 10 there is a positive
# divisibility multiplier m < p which preserves divisibility
# by p for the following function on any positive integer, n:
#    f(n) = (all but the last digit of n) + (the last digit of n) * m
# That is, if m is the divisibility multiplier for p, then
# f(n) is divisible by p if and only if n is divisible by p.
# (When n is much larger than p, f(n) will be less than n
# and repeated application of f provides a multiplicative
# divisibility test for p.)
# For example, the divisibility multiplier for 113 is 34.
#    f(76275) = 7627 + 5 * 34 = 7797 : 76275 and 7797 are both divisible by 113
#    f(12345) = 1234 + 5 * 34 = 1404 : 12345 and 1404 are both not divisible by 113
# What is the sum of the divisibility multipliers for the
# primes that are coprime to 10 and less than 10^{7}?
# ----------------------------------------------------
# Analysis: brute force
#           Hint: 10 m \equiv 1 (mod p)

068939912fc159c566fab1c9faf3b3546d6abdad2e80e03a08947c9839526ff46cf4ba1b45796289151ed89c9e4bf971ac3d
16082415fce6a96d1225e0124ddb93b1aaace0320d22aa0f874a3d9c86787c488d4a30b99910b281cca2d960df38f94f47a9
d2ec5892d01b46d714b1a574f783406c5a2bed04a9872764234b5856dbd28f5045bb39cd037a0deb1be4a877b7afe375ae7d
91408b07aae9e517534f70b99c51fc8126043925b8ec8c8e2fa472c5eab67bd696192b37e6d146cf990d350afe6f16ce49fc
9846e35c8c4b5451deee1f4140658d8a943665536d273bece06041b0826e831d5f0ac2254b31877401209b9cb55ef749827b
b10ed3ef807d7c2d2d7c6433c262d9682ae50e2e8693dbeaf1ce5643e225dde462f636216b8b83432f732b5c664cc42800a4
9d2b1887e26c78a21a22c40c53422871647258fabd7b04427ded2c2738a28752c2d7479084ec552cde187a6aff23be9ae13e
068e2cb013c6fd9bead2029096a0aaa95316809384c76da262abecb315cd27dcbeeeb1ce85a3089dd7c5e15a99ea1e480b46
6f591b304e6430d7667098304dd8f758328f87325fb20a0017528b0508032f0edc130f202ae73b8bfb5952fa830575e5bd4d
940ddca31e71b53503b1df6b1d24f6994fe8c4ddcb38a9451d70796deebdf61c0f06d493da25d391f82897282cc59bee8725
3a8fdac5966c2fcab58a2290b2ccb56b

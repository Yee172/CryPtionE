# Consider the consecutive primes p_{1} = 19 and p_{2} = 23.
# It can be verified that 1219 is the smallest number
# such that the last digits are formed by p_{1} whilst
# also being divisible by p_{2}.
# Let S be the smallest of these values of n.
# Find \sum S for every pair of consecutive primes
# with 5 \leq p_{1} \leq 1000000.
# ----------------------------------------------------
# Analysis: brute force
#           Let n satisfies that
#              p1 // 10 ** n = 0
#              p1 // 10 ** (n - 1) > 0
#           Let S = s * 10 ** n + p1, then
#              s = -p1 * (10 ** n)^{-1} (mod p2)

c8016128faabb59542e11f604f725b0e531647bb1e8b36102d12501b91cfc367047d549b93fac95b327346c00aef23f17f18
cf927800a57b280502c5c4e9ab141f5855503d1271f7d5e4fb216e44393657cc1a5b631237d5bed921313f9450f0a03ed655
360672f3ff699b6aa267a4b3025452c45300af5fad188d1ad15db5f814aa74a2b6f541da53c46a59872d83da9c06f0645bfa
966011216d63037bd9ce0fc25d678ad83f71f06fe53abf253fc07e0b2fd385259adb01a9c248a68f0626fd7022040a40ae49
795ca127b697d09873e4a9f12ee90115ebe854575890a9d1dcd3ea0245044306722b628184e59f8a6a3f09ae29b3e68a99e5
586f9eb876fc7c2d2d7c8416d40d22e6ab8ea28e5b9d12692a980ea2c7a22f4e53809f2cf82308ef419bff69eecf6940a870
adaef9e6212206800ebe6228e866e7b008807534097dcb6f44ed6678cebd3e46179c0dc52b6dbc68a860e79c0e902ada1841
655904e18d24487d3920c42b9084fd5a3f03bb3cc62ada771e084de269c74d89bf02daf186e32591601ba6e3ec40efe732ca
b62487c2b652692a4c23a3e751737720772f740d6488b1dce62f8cad7b632c2b979027ebac41cd3242305187f78788e11635
7637c19694783043959574b06058e185025429483ef35e29203a2f04f376e6584c94f724b23ac9b340bbb945007a3884b3e4
5891bed4e5325d513769bacd2de290f9

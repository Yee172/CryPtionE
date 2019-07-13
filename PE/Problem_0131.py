# There are some prime values, p, for which there exists
# a positive integer, n, such that the expression
# n^{3} + n^{2} p is a perfect cube.
# What is perhaps most surprising is that for each prime
# with this property the value of n is unique, and there
# are only four such primes below one-hundred.
# How many primes below one million have this remarkable
# property?
# ----------------------------------------------------
# Analysis: brute force
#           n^{3} + n^{2} * p = m^{3}
#           Let m = a * g, n = b * g, where g = gcd(m, n), gcd(a, b) = 1
#           then we get (a^{3} - b^{3}) * g / b^{2} = p
#           Thus, we get g = b^{2}
#                    and p = a^{3} - b^{3} = (a - b)(a^{2} + a * b + b^{2}), gcd(a, b) = 1
#           Since p is prime, we get a - b = 1, i.e. a = b + 1
#           Therefore, p = 3 * b^{2} + 3 * b + 1 and we only need to check whether p is prime

b3703d52bab1e49e8cd4f56b562c79616db6494d83544e659f4345a86490708fd1eaa5ec4835afed034022043b1dd3e299de
69ee487335c1eb17b6252e4409b8e3384dbf0306ad59c43f45d2e7ef99107097f23dd45db3e858861815cc81e052f675e3ad
06fb36e0e549acc5318afd71b69baa8da6994e94c0fd8c5cf74958e69ac4830932ff444d469247b1f06f0343a39eee80d79d
e1bff14dee8f883cfda3f0319a3969eb0d2d5713be673186014b268bf95723e32419ba80002ad55ace8b671dc7884bb2afcc
3651a5e273956a98b8802207d40ed4d9859b4f3b1ac92c58c842a14f14706f950a3f61ccc8f46ffc65591c925a1c72ec1a4d
722b55373e9d7c2d2d7c3d049076c4ce50ad24dc5378bd049045960ea5d4dcd6d8253f836d0e7345f1656891fcf999152928
014aaaa4d736f1643cf02cb1d319daaf974d82eec7c8348bc43a128e439f52914e6ff2895d2be2d89b4b51a3bd932b97597d
b400c727fa09cc205a47930c49cb6782f06377e3883a7c641bcc388b954d182da7aa3ab31b96ee1fa534b1cac432bd1af338
98c7c7ff7a83134fa3b11f6190dbd78631bf1cb96f09737a896dfda2bd60acb4ba71d6668cf2a535816ddbea5982929b7211
545b11301608ffd19440e91d84e75e929d5f856d9199d9981952563a11c776409253081357d4a9f7bfd5fcf19daf27f66fec
51bd31f1d69e72e0c6c4fa63f2720ef5

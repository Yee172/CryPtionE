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

233514a97a9939711fe7d41a66628e96e07de3aaa1d70721a6de99d97bb7c7883acf14a79c85ed5c6d304a0b9ebca2da3ccba6502ae1d210aa717558ce17a6e903b0383af4b7ab8531f8cf683ce25f1c4215348eb765e8a7fb4793e47b198341e66bee3aa45701ac65d951a490b61eda582c2df11f69334128b38298b5013ae8081ee21a36beff63e3fb4f0a94e2ca42dece196891362cc54203b4b20f6c631675c0006fa4d7f5dca244b2565b0aa6722f183a04f2b4543ba4e29ad570430491a5b248224beb0106db3f6e4b3b87a17a7db26e72e14d93eeafc7298283e3c4e0ccf705ab5fe64b2e94189693aaf24b0b1675136d2a156065e84540e35321b6617c2d2d7c1b0c7e1c85c5379526eaf64d9250daab8532342113b4d20e6528dd6f11883bca954dd0995431f67ea481076111994e95c386722c4db62b09f211531d6d4366e48b6223b17a8c181dc26b3f63fabb7bd7c6e2d49b62505315a60857b193190c69c9bc55d9c3e1294d2579c95d33cc8ea66cc89ee4ca3de69317111430d33417246fd73edcd089bc0e0c689346a4888c79302ac70f42156fbd645c4c44817a676ed633ab145130c9badc111b91fb1a82e619ea1502bf6c763b667b73f1b8a7e3b26f1b35aad3a2579242e33fe87549b511ff7f98f9f8d7404268b2287298741c21bab4c9eb63adfd121d46cc9de82f0f137ff28fc6064f19808749d30a2a8d4d82

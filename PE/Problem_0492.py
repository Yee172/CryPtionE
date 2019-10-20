# Define the sequence a_{1}, a_{2}, a_{3}, ... as:
#    a_{1} = 1,
#    a_{n + 1} = 6 a_{n}^{2} + 10 a_{n} + 3 for n \geq 1
# Define B(x, y, n) as \sum (a_{n} mod p) for every prime
# p such that x \leq p \leq x + y.
# Find B(10^{9}, 10^{7}, 10^{15}).
# ----------------------------------------------------
# Analysis: linear recursion
#           Let b_{n} = 6 a_{n} + 5, then we get that
#              b_{1} = 11,
#              b_{n + 1} = b_{n}^{2} - 2 for n \geq 1
#           Let P_{n} = x^{n} + (frac{1}{x})^{n} for some postive x with P_{1} = b_{1},
#           it is easy to see that
#              P_{0} = 2,
#              P_{n + 1} = P_{1} P_{n} - P_{n - 1} = 11 P_{n} - P_{n - 1} for n \geq 1
#           and most importantly, we can get that
#              P_{2^{n}} = P_{2^{n - 1}}^{2} - 2
#           Thus, b_{n} = P_{2^{n - 1}}
#           Also, from the perspective of matrix multiplication, we can see that
#              sequence {P_{n} mod modulo} has a loop with length at most (modulo + 1)(modulo - 1)
#           Therefore, b_{n} mod modulo = P_{2^{n - 1} mod (modulo + 1)(modulo - 1)} mod modulo
#           Then, a_{n} mod modulo = (b_{n} - 5) / 6 mod modulo

04c7798ced3b778642c93c57fd1a06a8c73ef7464517b518772368f590e7a4ee2ad309fde85090450a3de9abca914e74f4f2
1a950864ef13fee0e3ab34e6383867315409983cc76b608c4ae2e401700c0f9bed2f29b03668af07de28cddbe16247b631fb
52d356cd78d3a65b7f5fb45bb10c94bb71323a3542ac144b5c424e2476070c8ed312602ae8ec77aa523b37cb0b2ed6d2d44d
96e585acc28b5fd0c5b2890c068f4851a53aa94955ab01c44add48dc596c149715fa7edffad951ff697788db0861a1b7481a
6fce3dd20014729ddff260be827d036e4951456ac1a12d9495d1751fb37688541d31194b6866665a034fcf18a63199cf55ca
47a9de7468287c2d2d7cc18927295b00f3f4df24ab370882c6a8dcbd2b8e3b5c4f6fde6c18947cc922c5dcafdbe9fa8bce00
f6722b62b627715f99a5506f92e5e095d321535db0123a4efdb03d87c7a412fd54a137eaa7ad5cd21e1a5152e5dba34dac86
423f0585ca58628cf0c6f66b6b03fb3fe6bda9d9c29c4b7183d53477552d4343e92c33d518b0107f6df1078b43496c391a3d
3fd6fa6ed88789570d34517b1618ac6c2ebf5499d2295429e2ce2dc42d919ecabf66fe18206918e51636d50ccb39aab39474
44109d0d6bd4c14cb8af09c0b61314745fd6a1adb3f45091a3aae09e882f1193396c74246469eb456ebfac9b2b7f1c64b899
f76f0e82653c18fa3525a70f220b4cf07c2d2d7ca511eb1ea5889315ec44eb36b35bf6e9210c2a8463b3b4a2375396e0a627
7c93f79c0ef654132eb101bc3e1f6fd16d17a922aeae9ba0bd9adf8f2f0cfe6d4959e15d80632f72e9889e140cb383efa89e
6eef62b27a973066426bcdeccf7abf08d7b08dc112af25e2ced1dad818e2b3c31e6c558adf9484a5234bb3895c1429ad760e
deae4d66246e684b3faf07bfd6b5b04db89430dedc4ab4eaea49e2299c65dd989e095fc6216e65243a662f4a96b2c214b574
eb77c6731174bf246cc1b8041cd52e515cf2ded8f6aaff3f054e05e8f04b437d418bef7d1ebbe51c66eed33024cba4458a8e
9bfe081c84c68906bc2a0778a6dd134de76791559c6a1b62f2eb

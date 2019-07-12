# Let y_{0}, y_{1}, y_{2}, ... be a sequence of random
# unsigned 32 bit integers.
# For the sequence xi the following recursion is given:
#    1. x_{0} = 0 and
#    2. x_{i} = x_{i - 1} | y_{i - 1}, for i > 0.
# It can be seen that eventually there will be an index
# N such that x_{i} = 2^{32} -1 for all i \geq N.
# Find the expected value of N.
# Give your answer rounded to 10 digits after the decimal point.
# ----------------------------------------------------
# Analysis: brute force
#           E = \frac{1}{2}^{32} * \sum_{i = 1}^{\infty} i * ((1 + \frac{2^{i - 1} - 1}{2^{i - 1}})^{32} - (1 + \frac{2^{i - 2} - 1}{2^{i - 2}})^{32})
#             = \sum_{i = 0}^{\infty} (1 - (1 - \frac{1}{2^{i}})^{32})

449f627a8a2f5802631a265823fc5f0cb7e37d260e54169b9efad754a64990324c12c6380a10380f2c23edc53af1812acc3ba6fa0923dc11967d48785de86773d3d5203f124881db6c53a9537ae16359a3eddd847826d99df9a99a716f530d108893c24d3e37293b7418e2b22a7fbe0353c3702483dc0bdfefe328f76146f58843ae099cfcddc9be65719ca1a902310c0004cf4dbdb5cb0e668f8ef12830722cad43b2dfee9bf36d8b1bf70d431cbef52d1b90fbba4db52208010c91e324999f44902151c016f6211452510d0547858e434918ba719874ac2ce4e6af3a5ee4bcf568949201569e08352b0162febe64fcc987a11344df9d90bca84f242355746b

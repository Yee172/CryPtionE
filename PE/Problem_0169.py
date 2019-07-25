# Define f(0) = 1 and f(n) to be the number of different
# ways n can be expressed as a sum of integer powers of 2
# using each power no more than twice.
# What is f(10^{25})?
# ----------------------------------------------------
# Analysis: brute force
#           Hint: consider the extended binary representation, where each position can hold 0, 1 and 2,
#                 then we can see that for each odd number, it should be represented by ***1, while even
#                 number should be represented by ***0 or ***2.
#                 Thus, f(2 n + 1) = f(n) and f(2 n) = f(n) + f(n - 1).

404c2048cbec7d9d2eef368c4b5d977c3c3aa3a5e302ebb30bae1dd76bbe1bcfa943cbe2fd04ba1fd33c93f6f0dbc5726786
4493430ec5f1b71b25d1839e47404a7d3f4559933a1da3e828348dff916dd5aa223832deb1038808c1186a1267b46a10a0e1
5d76fe80ab4f21856c5162403ee6b9831d95b56d2ade0646f99d2e8b30f4b0708d14e56141beea97b9f360b51eec8a263b9b
81f6d2b1185b253f9499b550a9acf0f362f4d5d390c19dc9eb5507db491cc5482757d84d5ff2d6806ab0f1677e2cb8ffee45
c5fb09033e0aeb29bfc78c419057153732fb25b0c73f61d5315e9ac47e3381639670e7f1b52772194c513870edf75d8c8793
018946aa945f

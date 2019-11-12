# A snowflake of order n is formed by overlaying an
# equilateral triangle (rotated by 180 degrees) onto
# each equilateral triangle of the same size in a snowflake
# of order n - 1. A snowflake of order 1 is a single
# equilateral triangle.
# For an order n snowflake, let A(n) be the number of
# triangles that are one layer thick, and let B(n) be
# the number of triangles that are three layers thick.
# Define G(n) = gcd(A(n), B(n)).
# Find \sum_{n = 3}^{10^{7}} G(n).
# ----------------------------------------------------
# Analysis: brute force
#           Hint: state transfer matrix is
#                 3 1 0 0 0 0 0  1 layer  with 2 outer sides
#                 2 2 0 0 0 0 0  1 layer  with 1 outer side
#                 0 1 3 0 0 0 0  1 layer  with 0 outer side
#                 1 2 3 0 0 0 0  3 layers with 3 outer sides
#                 0 0 0 6 3 1 0  3 layers with 2 outer sides
#                 0 0 0 0 2 2 0  3 layers with 1 outer side
#                 0 0 0 0 0 1 3  3 layers with 0 outer side
#                 According to this matrix, we can get that
#                    A[n] = 7 A[n - 1] - 12 A[n - 2]
#                    B[n] = 14 B[n - 1] - 73 B[n - 2] + 168 B[n - 3] - 144 B[n - 4]
#                 and their characteristic polynomials are
#                    A[n] => x^{2} - 7 x + 12
#                    B[n] => (x^{2} - 7 x + 12)^{2}
#                 Thus, we get
#                    A[n] = 3 * 4^{n - 1} - 2 * 3^{n - 1}
#                    B[n] = (18 * n - 138) * 4^{n - 2} + (4 * n + 26) * 3^{n - 1}
#                 Therefore,
#                 gcd(A[n], B[n]) = gcd(3 * 4^{n - 1} - 2 * 3^{n - 1}, (18 * n - 138) * 4^{n - 2} + (4 * n + 26) * 3^{n - 1})
#                                 = gcd(3 * 4^{n - 1} - 2 * 3^{n - 1}, (42 * n + 18) * 4^{n - 2})
#                 (when n \geq 2) = 6 * gcd(2 * 4^{n - 2} - 3^{n - 2}, (7 * n + 3) * 4^{n - 2})
#                                 = 6 * gcd(2 * 4^{n - 2} - 3^{n - 2}, 7 * n + 3)
#                 (It is easy to see that gcd(2 * 4^{n - 2} - 3^{n - 2}, 4^{n - 2}) = 1)

3bc0690995b980aeccdf0f3b5768030b51ae287a1c2c097e21878c21b03f133eabb331814186cc9e74fe3f1dce826610bb16
afcc922e3f491b4856b39c5ecfa4567afa2ef5431294841502f55e2747656e55e0412a997320c912e9db8f6a4b0c38604450
5f3931ddb5d6ff8afe1633442289b61fa9f3dd8986c75655a659a2455490be85fd5f71515bafe84bb986304d6a2c686a38f1
c85ed1a4282ab0a2da9a630e9159bc424adc6ed3022b262afbc36eb5d67e5cd1bd05bef4cfc82319b6ceb3311e6d2c6de7a2
56e3ec44864c25fd0fbff7e1e38a70a35c44f73bf036698218aade7a7d1b8cb6e9a9a71b688dc4e7f8ba728d93a9301a626a
88e7582783c17c2d2d7ca5246085cf4e85e67f937cf5362d894038382259db874790783e04d7a8635e423b6c21de8f36916d
82b23822914654a77a8447b169a7f94c6532951b165e9dbe8d9ea158f1f541fae7001d3a83faf1f6872d93ad19f6210628f0
994314cda2f9cc466813302f69c16bae42c35747d32e729f6db985f6fc611ea8956eed4f6954615a4d779dce15e505cd6082
ff0d80fc08e8e1b0b700c3cd209c35baeb650245177156f3f613198fa3cbdc7a6e37ff8fe6eafc6ccc8804b86a22973c7ff2
9486926dc94287f812d307d33ec21ed3ecb4a11689f1e8142980425dc9100bcb1ccc4477c7abf096c8a63bfaa3ede64e8a3f
f4c84e8effb092809243d84c47d038b8

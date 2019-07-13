# Dave is doing his homework on the balcony and, preparing
# a presentation about Pythagorean triangles, has just cut
# out a triangle with side lengths 30cm, 40cm and 50cm from
# some cardboard, when a gust of wind blows the triangle
# down into the garden.
# Another gust blows a small ant straight onto this triangle.
# The poor ant is completely disoriented and starts to crawl
# straight ahead in random direction in order to get back
# into the grass.
# Assuming that all possible positions of the ant within
# the triangle and all possible directions of moving on
# are equiprobable, what is the probability that the ant
# leaves the triangle along its longest side?
# Give your answer rounded to 10 digits after the decimal point.
# ----------------------------------------------------
# Analysis: integral
#             \frac{\int_{0}^{leg2} \int_{0}^{leg1 - \frac{leg1}{leg2} * y} 2 * \pi - (\frac{\pi}{2} + \arctan(\frac{leg2 - y}{x}) + \arctan(\frac{leg1 - x}{y})) dx dy}{leg1 * leg2 * \pi}
#           = \frac{3}{4} - \frac{(leg1^{2} + leg2^{2}) * \ln(leg1^{2} + leg2^{2}) + 2 * leg1 * leg2 * (\arctan(\frac{leg1}{leg2}) + \arctan(\frac{leg2}{leg1})) - 2 * (leg1^{2} * \ln(leg1) + leg2^{2} * \ln(leg2))}{4 * leg1 * leg2 * \pi}

394219b067056c2f8f734d268ef600c6e77a7626379c812e919e9de4d17c7277ddcc6c2f089128bbe7905bb4c5a63ee3e9cc
af3c61c2fcb234590eb4af0f95dc713fdb63b0c88f5d6fee302be57479f8acc415fa988e02daf6d978f81684fc151c22d638
b84e1d3f3ae91538835fcffc32d976b87ac353d628b302bcd4facdd0fff5255a16bccb3e21b98eb0a18b5477d7ddab199f53
7e025582c39ef3341f4d53fdfb0f5fd2efb3b8fb0fe688e4d2d92c57c630e1ad04daede683969c424b7c5efd2add197bbf11
714767a173e1bf1a892192d9044ecb6506ec3acccb7bfd3b8919e8612794139bbe1188b59e22f69ffe5843b5acd249a82c69
d027a38b4a2a7c2d2d7c657e8c7b84a0855a29fb02976d72b9b2a63fff9a20826f4161876d2d2817222f80105245bf8cd5ab
bf36ec989fb3b0c20bcc116cbd7f2e8648febe94553414f2bbd6cb684a8f7a4dcd2ac8762bc1188d226ebecd9214943c533c
b76af517bea94e804d5494caf1efa4f876663eff2a1ad82aa51da34be88d4234afd849852a1626c768f2206b07d2c09ab1de
957fef9fc8eb366869b27ab1e13eb9cc9475a041a219052484ef08f117b34aab9702f5be8d80f0d2a9d35e43fc2ad316fd62
a0e7805e093eadae0394c60d1353edd396d2869d150ffc513dcaf270e79e60c6aafdffb4e5b27afaae78849177f18efd3844
cfba3821fc21bd90b0ff0ad32a43316b

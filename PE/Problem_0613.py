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

c0af19a3b5d74764cc046966480640d9e6049999bcefee71e854a876f76b87f452f361f17b6179d8f9b2206e24ebdc9029064ce10d1f12a2895e4f39aa2cc351bb487d9986293f7752767616963a5aee7c8b5d9f4bf66915d882a074cc66395cb53d1a6d58800f20cc81965eb4ecafe75a8e1b87e3bf89b636af3d0a91a78f3e637f77a21b0dea4a0b0f52f6d8df7878ad3fd365853126913d81c1209a2c78658f5adf0651817ca051ca6f56d6d220bb8b6bc0442c62ad2f3b62b92d3d28c988a1bd0ebf4912503fbd608741057f73dd6743a470f6118ee3068ed35571ff2779cea6746e3613f2632e2ed68e34ee8d3431cabbd408b25ad092c37bfaa517ce0b7c2d2d7c233355a31778ab59c565fd9af6872fdf41b623436dec7769820f729c2523dc8c46db18d510a3d3fbe20427c7aa798b0d12311d7aef179b2a7da479979a876cf8dc44f8a14f6a63b5038af3c1216711d59315e37c9aedc594fd1e01b4fdf969945f2273b91195531cef6567761d1d6db7e60f5741f03ba73da5a81111ae47e93140838009216f42367eb96e340e423cc8db740d899578ccaf88bf66fbdb22a5bd3694fe07c4f52c68639e04bf2b57e6617190931bb0aa99224fc87768dc9fdb9e68396fd7cd26259b65a8cd530a65448a49484cd095ad015a82d393a28ce154f60969d2486d7323b772945f677ae05874251f82f96d8917d2d533a8299d99e873

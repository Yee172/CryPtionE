# Define f(0) = 1 and f(n) to be the number of ways to
# write n as a sum of powers of 2 where no power occurs
# more than twice. 
# It can be shown that for every fraction p / q (p > 0,
# q > 0) there exists at least one integer n such that
# f(n) / f(n - 1) = p / q.
# For instance, the smallest n for which f(n) / f(n - 1)
# = 13 / 17 is 241.
# The binary expansion of 241 is 11110001.
# Reading this binary number from the most significant
# bit to the least significant bit there are 4 one's, 3
# zeroes and 1 one. We shall call the string 4, 3, 1 the
# Shortened Binary Expansion of 241.
# Find the Shortened Binary Expansion of the smallest n
# for which f(n) / f(n - 1) = 123456789 / 987654321.
# Give your answer as comma separated integers, without
# any whitespaces.
# ----------------------------------------------------
# Analysis: brute force
#           Related with Problem_0169
#           Hint: denote g(n) as f(n) / f(n - 1), then we can get that
#                    g(n) = 1 + g(n / 2)              , if n is even 
#                    1 / g(n) = 1 + 1 / g((n - 1) / 2), if n is odd
#                 denote h(p, q) as the smallest n for which f(n) / f(n - 1) = p / q,
#                 then we get that
#                    h(p, q) = 2 * h(p, q - p) + 1, if p < q
#                              2 * h(p - q, q)    , otherwise

3e120318bce917d85987526745ee470c9fbba09bd64973362c07538a3711b71f560c7db9c6dd4a746aaa6197d8430a403166
c13ede137cefffdf012a267e4bd352e8f7adfcf55ecdec52b4dd33f5118f2a3fdec21fda683a19c9499e6ae4c436ae5d427b
c5d80b61778a90d2c95e625347d186251d4a5d215fe49eb9119f66e8c93f66a7b7c15561426a4e4f154bbc76f8cc2f1f7c48
27003c932969c360988f7ccfce80b7d0cf8d5291aa4f1106b97a2c5d133733f40f7bacfa6dd10484190711c2d713b391083c
e842bad132588e29c54c392fdd6ad4ee072bafc4388b86fbc44a70d03d29a0cb4b89d6dbef18e99419ef62f64922454f69d6
afd65907f70a7c2d2d7c9b91376a1c1bee491c807dcd18e7b2939b20d0a8c6b8c8736042588a1bda4873811a5250f365f0d1
e1db688ce036c4296f7eea4bc6887d7d149abd3f7359172d3a676fc132a13343a9cf8babb17017f022b1295e93e9a5ddc4ce
2e20b91b8fa70f9ab042fd1365553432b7f00bcfbe30110cd1ff643c48ea62db98e8ef36599ad185519b81ed52273e8e7fc1
6ae8cd27c410fe3f8dd50a01cf7ae51a902384b356069645f6dc6e52e66791a11fd3ae87fe0d43e61ed89f8f2a4ee53b80b2
932852ec3307ebd29611edde409d9b07dd4e13bd7d481e56001e28ba7ecb9f8991b4fcd038aa15fecddda63793c1ed8df450
0cf3b30c5bac37f764ff1b4318dce2887c2d2d7cca94a0a5c893f08d51331674c127e8753cca2b8215c8cf2e893394d7d3c2
580f5353921661eedba74ceccec4dcb579ec1af9e4f642cfeff4cc8a9f5b419d03ab0d1beefb70f267604c4fe324a83eb092
9992bf51f2c6e138cf0b7e690c300f4e279b920a3066cd9c3a5d4817d471c5c6fed5f6ec717e702dfe825405c4f46017b051
15288fd758ea381c416b70fe078d14b3d1acc79608cd4580d1dcd7959ab310600ee7a0a0b07422279eacfd57eacb9fad6e10
0d20d549db75e364706d9e4bd90534b61bb009d23c7acd9995c600a4a9d56a1409fcde5fa4c255ad2f6b5745d7330ad0f0b1
33e4400e9bf9640c41c80c7914a6bee4be96871accd0fd45fc12

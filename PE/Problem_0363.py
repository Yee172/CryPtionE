# A cubic Bézier curve is defined by four points:
# P_{0}, P_{1}, P_{2} and P_{3}.
# The curve is constructed as follows:
# On the segments P_{0} P_{1}, P_{1} P_{2} and P_{2} P_{3}
# the points Q_{0}, Q_{1} and Q_{2} are drawn such that
#   P_{0} Q_{0} / P_{0} P_{1} = P_{1} Q_{1} / P_{1} P_{2}
# = P_{2} Q_{2} / P_{2} P_{3} = t (t in [0, 1]).
# On the segments Q_{0} Q_{1} and Q_{1} Q_{2} the points
# R_{0} and R_{1} are drawn such that
# Q_{0} R_{0} / Q_{0} Q_{1} = Q_{1} R_{1} / Q_{1} Q_{2} = t
# for the same value of t.
# On the segment R_{0} R_{1} the point B is drawn such that
# R_{0} B / R_{0} R_{1} = t for the same value of t.
# The Bézier curve defined by the points P_{0}, P_{1}, P_{2}, P_{3}
# is the locus of B as Q_{0} takes all possible positions
# on the segment P_{0} P_{1}.
# (Please note that for all points the value of t is the same.)
# From the construction it is clear that the Bézier curve
# will be tangent to the segments P_{0} P_{1} in P_{0}
# and P_{2} P_{3} in P_{3}.
# A cubic Bézier curve with P_{0} = (1, 0), P_{1} = (1, v),
# P_{2} = (v, 1) and P_{3} = (0, 1) is used to approximate
# a quarter circle.
# The value v > 0 is chosen such that the area enclosed
# by the lines O P_{0}, O P_{3} and the curve is equal
# to \pi / 4 (the area of the quarter circle).
# By how many percent does the length of the curve differ
# from the length of the quarter circle?
# That is, if L is the length of the curve, calculate
#    100 \times \frac{L - \pi / 2}{\pi / 2}.
# Give your answer rounded to 10 digits behind the decimal point.
# ----------------------------------------------------
# Analysis: brute force
#           Hint: Q_{0} = (1 - t) P_{0} + t P_{1} ...
#                 R_{0} = (1 - t) Q_{0} + t Q_{1} ...
#                 B = (1 - t) R_{0} + t R_{1}
#                 Therefore, x = B_{x} = (1 - t)^{3} + 3 (1 - t)^{2} t + 3 (1 - t) t^{2} v
#                            y = B_{y} = 3 (1 - t)^{2} t v + 3 (1 - t) t^{2} + t^{3}
#                 When t = 0, then B is P_{0}, and when t = 1, then B is P_{3}, we get
#                    S = \int y d x = \int_{1}^{0} y \frac{d x}{d t} d t = \frac{\pi}{4}
#                 => \frac{3}{20} v^{2} - \frac{3}{5} v + frac{\pi}{4} - \frac{1}{2} = 0
#                 => v = 2 \pm \sqrt{\frac{22 - 5 \pi}{3}}
#                 As a result, v = v = 2 - \sqrt{\frac{22 - 5 \pi}{3}}
#                 L = \int_{0}^{1} \sqrt{{\frac{d x}{d t}}^{2} + {\frac{d y}{d t}}^{2}} d t

0ed253fd218321d03ce5445fc28388e2f43160edb3b6c2c24bd72477cfcf7cfbb507c43bb9a0560116068431a36a2b879583
ef779e3d3ab9eb8897891edca91d6000a4e732ac2604bca78ac8455dc899e3e0f9c160a24bc05aceaf8e970463befafe9a78
95f32b18f428f6c1138691ec2c49107c083a98a467f8ca741b1d7d0658b9be1f2c10a269fdf45bf0e344d69469cb55555dee
3817876c0b073c6b96bd0f7f6615b1f8498314fcffdb21fadcbc599591b6489cef1409e8ae464532489225e5134aac079fa5
49a775733b0a0b3abaca1455d647b7d8bde0baede624100134ec429ade4eb4820597d67366049b7ad6386cffdd15c6798e00
119dca21397c7c2d2d7c17873eda50fc020ee1aef707bc90ae91be8f409f03acfcac587025ab9e663d94b69650ff37da6968
a844f9cdb942752e56ad81575e69d62685b47c72e1dee4447322030a986bf56a1d38e4567cf651813e77e44b900a75eb486d
c6112ff5ed6ec9afaca2e997a5f4723894c32d8e41a938578bb8953b881bb3c37138a6050b4501755c3badc711990981dee4
6d61aaf790bd71f821799c2516e99cce47976f8a46fddc181de2a6b98d0c2291237a31eeb01bf54230d9693e84e9b5e159e3
2093903ba3864491925cc3820fd6fe717d0f082e378975b1c5bdef5c31b93e1ff42e07cc24e87ff43dfee3ed24976916cea9
5328cc3c28057b4eff66ef65ec93035f7c2d2d7c33687a77d547c02a5143921eb2a960ff4a3fbd61da81206ae7de87b98e8e
0665d04bd2e5b463a6aefb30de766d76812a829c5d10df114d65f826603346388fbf0778d13214949df6ec3f3fc529ba8bb8
f1c18ddbb68364cdce995d71a5c44446fff9508965cbc551a7efc3065704ed43e768c154dedc36cc6904f3c8ae23663b208c
e2cad843601c39fd2ac6cd8666ef907dd77cd1295d436b2ab9dd5e56af72b4c537c7d972b71ea0070889d3f1562a8ef04e88
72b64f279cf0a91d4171aa902e0997580a23bef4c932a7edeed705ede89ca0b851d73d287ce232770a4526fbacdf991269ce
eb6a71ef2f8b3115787525faf90c6f650743bd1ad1c8bde3476d

# If we are presented with the first k terms of a sequence
# it is impossible to say with certainty the value of the
# next term, as there are infinitely many polynomial
# functions that can model the sequence.
# We shall define OP(k, n) to be the n-th term of the optimum
# polynomial generating function for the first k terms of
# a sequence. It should be clear that OP(k, n) will accurately
# generate the terms of the sequence for n \leq k, and
# potentially the first incorrect term (FIT) will be OP(k, k+1);
# in which case we shall call it a bad OP (BOP).
# As a basis, if we were only given the first term of
# sequence, it would be most sensible to assume constancy;
# that is, for n \geq 2, OP(1, n) = u_{1}.
# Consider the following tenth degree polynomial generating function:
#    u_{n} = 1 - n + n^{2} - n^{3} + n^{4} - n^{5} + n^{6} - n^{7} + n^{8} - n^{9} + n^{10}
# Find the sum of FITs for the BOPs.
# ----------------------------------------------------
# Analysis: lagrange interpolation

02ebf5f299e5530e30fb3400f1c0d4a04e99ee639afa9e9bd4b6151cbb78e85cce654ba494c4b3d9ee3c2ae4b596b10766510184e54cde4ac462e3e1be64e5805876a96ef355b869a139f85d20a6e9f4cffd50a773fce807fc69e487158aa76f7053874cc8cb349d024f4962803476b808e7c8cd7685c11333f2f9ffa28d400f23b6ba477d27f7d8d241a7f2321038047882c5d8b7225d48ae110a7c499bf5a0c2e22a3ede8e4c4f91c535176df20915ae53fc07702d1dfcd894734c150762d77352534c3bdf03b294243451575addf6bf1a27d928865986535f0daff10b43d19a6b9f73899c323865a29485b4e441480652639e2d3ede94a38d6d44a7dd98cf7c2d2d7c0425872167d70164e2d92c7466e30cb51271b3dc660404397c1d8b8fcaf85353ecb6acb71f74dba5f21327e33d28f47d60c1db0f1024160429a151bd40aa87205f7e0a4c4496f7592c30bf7aa674284adc09bee87105f3afd3b2d51be52ad04df73c9b2a1d36cd4eb9035e22852b472e3e7f0835c0e98d7c58cc49f550b6d6a6a97b7440f7fa6a4115c4a6366e38ef4d7356a5dfeb1d6cee018bf241f132ffb0c011a5f73a33fac95b1ef0bd8aa3fc9cbc0dca41c622fa9ccfe700db23c0ce1ed56e8e854f10563dc68a8c5e5dedfa4e449ff9d86105bc79fe7fa62cccb3e3a4cb6488de7c113da49779e8e88cf8bd6987d84b8081e8150e76cbb74c89c988657c2d2d7c06ece4753b67cd4e97c64f923a484758fd7fe7574e062a389291a9e787a3d00435146336ddcf769e19b97ff97e62acfd4bcda35b28a93858698010bf765a7a38050d6bd72c475effdf0978b2c98486481a3cf2eff935dd87edf224c3d8ae1eabd4e8487e8af07822501687ec2d4b0035be31b97136f838cc396d84ec73fa4cee81334bf62e3ebe38e373d9ea13b3f7bf48fbc1a8ab72265513fe6212503d8944bdfbf7829e6b6349d881c3752688d41a01b8c2cd21cdefa1ef30ad9dfbca712e4c04669b09edcf5e9240d333a6627ecf4fdcdbfab0199a6bd4770fb7d07307ba495220987c9e5c53a7edca4c24bcc534fe446d8bab502f9a419df97bb9298fa27c2d2d7c2361989fe0264a3de0c12f5f62f6ccd0c3a56615a031b30d2cbedc9cecd9c2a8baef9ed5de962e11bad8f199bf5a9be2313c0f1cdf1ac7d80b2d8cfa4896727fa3fdfb81ae72090ce22e351b99f3bb0004bb6f0a655eb16ba019f8cf67141a39699e4fa58554e1fc7fd94e500833da30f0f85eb9c4105497eb234580ec57a224cd5e9f5ecb2b9da3b4dacb6746d0d8e228edfe78904f2414d293f02f17ff43592dbfa1b67389dd674c6401dc7a9cdf9220a9d1f3c185ea02bb9760a4c988036dc5abb01be702d9e0663f4295f073053c69cc4117afbd3b1dd7fd4813b7cc5f86d9fb7e328fa9ee93edcca62aecaa8ee86ceea50c47bcff14157467ba1201b0fd

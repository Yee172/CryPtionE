# A positive fraction whose numerator is less than its
# denominator is called a proper fraction.
# We shall call a fraction that cannot be cancelled
# down a resilient fraction.
# Furthermore we shall define the resilience of a denominator,
# R(d), to be the ratio of its proper fractions that are
# resilient.
# For example, R(12) = 4 / 11.
# Find the smallest denominator d, having a resilience
# R(d) < 15499 / 94744.
# ----------------------------------------------------
# Analysis: brute force
#           According to the property of phi function,
#           we can see that we should first find the minimum
#           consecutive prime production satisfies the condition,
#           then enumerate the multiply of the second minimum
#           consecutive prime production to get the result.
#           Hint: Based on phi(n) = n \prod_{p | n, p prime} (1 - 1 / p),
#                 we can see that
#                 phi(n * d) / (d * n - 1) < phi(n) / (n - 1)
#                    if d is a prime divisor of n
#                 phi(n * p) / (p * n - 1) < phi(n * d) / (n * d - 1)
#                    if p a prime that prime with n and d is a prime divisor of n

c0d4404815202874086aedddbd5a91d6963235d8ac3840201c782912df2fecca966c343ff3f69864ba2b98cc89d1cd117faa7a15ad1964d9842f9c565fdfbfd21b1521388ecf91acc69f43dd773b1214bc46cdcbde52e39a59705a8b493104e6d5b7f155a0ac7d2a54b62492fe1fbc24cfd8598053399383af00443e48b3fbf32a587fb54e82f372f0b7eb2cfa84c334d8a24da70d27509e225a5ccb0d4bb08ed9a4043c28f16e92d86df74097d5e032ce6d2dd5dd7b0eeabae9b6ec022349c2c4f9000cec93b18c91481a887a9ad24bfc1df21db418460126fbf262fbaf4929f449506ad72c328c60b2ac306be43fc04fed4483936300cff32f7cba2bf575027c2d2d7cc7e8679e8360afc092063d9db8473d2f1618b501788d398b87702003b18cdc8c0d8c88da2d13bbfd35eaed521e7b978d7dcb19474a8e02c765722014d6a324529c32f35be58a3a52ba88a5dae9d1f7ca2b61994938e701f770bb252707cfe9dbb3d21689cb700c8985c517bd13d15a0316f44ec58f1888cdbdf8ce763f168ec935851008935e5e0dca79e0ec6ec356ccfc9fb8f57a5b8875e797bd1819ba78a6da96f668e75dff2febfe94b67c9a9859aa1366513689fe36d3584a089bcc61e996499e78d626cada38c1d6d8eabb309e067c5db6559bcf77c88f3b49c9b5afdd1fd93738de66121d71d28033cbeee656a826547fac121235ad6448768e0aea39

# A and B play a game. A has originally 1 gram of gold
# and B has an unlimited amount. Each round goes as follows:
#     A chooses and displays, x, a nonnegative real number
#         no larger than the amount of gold that A has.
#     Either B chooses to TAKE. Then A gives B x grams of gold.
#     Or B chooses to GIVE. Then B gives A x grams of gold.
# B TAKEs n times and GIVEs n times after which the game finishes.
# Define g(X) to be the smallest value of n so that A
# can guarantee to have at least X grams of gold at the
# end of the game. You are given g(1.7) = 10.
# Find g(1.9999).
# ----------------------------------------------------
# Analysis: brute force
#           Hint: https://oeis.org/A032443
#                 f(n) = 2 * 4^{n} / (\binom{2 n}{n} + 4^{n})
#           Hint: Use Stirling's approximation

0cc61a527568c12ab7312cc632a88b5deba18c82d8a6d22e89d0341ebb72d6394d17471f436f5229b63f5c2ccbea0a962eff
c8d799fb957ea5918389af11a9a32dd4192a4278fc1f8eed1c4e9db36657c6e70aad3b5afb339decdb786e3858210868385f
b390411f9ebccb30e5cfab1ab560cf6c60fd79e42db94d74e3fe856695995ae13bda41509ffb42caec475d0a49f83eae66cf
b9b437439a7bea78276a873560de16ccc8424e0a3a03269c5922ae6df7366d6c629e777f6e1e9a7e717c141649f7e0ba488e
bfb5cd41465dd0bc4b78b0b697fd72ca2b0db0415417ae97aa54127bc5673c9e74ce7f07435d9b1b1ebddbe6da798eced7d2
94311138f6e47c2d2d7c65d3e14ccb11321b4acfa7c144d6bbdeb40eaf67447dbcf477c956db4aaf28184da718506907c613
cc3eae7a0c584caf8403bc4bda353b7aeb0459b6db444621117d18c98b2558e9b6072f723b35ba96ed7fb1b2e4187932b9ce
bf9d1199e282fa661dd12d384ffd23119c9e255af82a2bd69840e866080924180174e4fac1b44c1de4636cfaa7ec5d754ad6
dac95c6209003af4c04390c04cc9cb5b5d3d2bc59a11aaff04ac0cee4d989e766467faf8b592ffe323c505c18241dfa552fc
1b44382798aa5f62485411f665be99b4e2ad93a8c8059d2376057434dc216985c209b75734d0eaab2898c083c8ada6cd09ab
fd97774e4d295a129b1157f368b41f8e7c2d2d7c8735773481b7cd3e79f19a12ea0c66634a980b301d6594a00dc764b135e6
71381b8c0e7e67b38cec87fd8a37ba7c84ea1937d04ceb82a6a01646fc17bc2d67d398fd0edb350a6273b2b83c1fc802ac38
d1ee8586b248aabeebfcf4291ae97912a738163e1cb3109dff8185b841bae79f96a8d368e8e54e702dbdf18b38675f6a7569
d437aa9e03c668a5547fe5f9a52bec9a14bbfb310f1723862736d9b214e5e31f8e015a2f19a1fc64206a018dc1fd8d8d8a0f
a8be3459de4f5c79366ea15bc066bcfe4755fb6e4bac4928f8586ab51458ce63e9272fddbb543ade8d98175f6e377a8505f9
832660ba2bd91dcf5c81e53dcf04ebd5d5661824e749509e5127

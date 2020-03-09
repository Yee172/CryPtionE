# In a sliding game a counter may slide horizontally or
# vertically into an empty space. The objective of the
# game is to move the red counter from the top left corner
# of a grid to the bottom right corner; the space always
# starts in the bottom right corner.
# Let S(m, n) represent the minimum number of moves to complete
# the game on an m by n grid. For example, it can be verified
# that S(5, 4) = 25.
# How many grids does S(m, n) = p^{2}, where p < 10^{6} is prime?
# ----------------------------------------------------
# Analysis: brute force
#           Hint: from   R to B   needs 3 moves
#                      B B    B R
# 
#                 from   B to B B needs 3 moves
#                      R B      R
# 
#                 from B B B to B B B needs 5 moves
#                        R B    B   R
# 
#                 from B   to B B needs 5 moves
#                      B R    B
#                      B B    B R

00ef0a2d244a8e4fb67cf6fb8c1577f5c96d15def5fe46b1a1126b938c835091b26cb9938c2ee18175581a3f2423dc625cbd
c9d178c4e3a9bf10e5be79d3faf375aa829d7e08bd3f731ebc54d1dad6afe5ce6767264997e340873acc9730dc068858c004
f76ebc306e73a1fe453db0a5f4c84180742ba6c910010be81c8d0418e2cfb6019b64f1fc596cef890e3d76b13f4d6a8b4524
4290b6439b694188f7eb4571a8e75047e7dd4f965e0ecfa3e3fb465c0f0ce029c58d884274af4165f4ed6f31b501e6ca2c3c
95a1d46ddce8493d44250c309bc095b6225be2fcbcfba5c89c66228621fa27f51cddb223fa56de09365661766f7030b0c13b
3d3f3a53ef697c2d2d7c35607f50e5d3751ad120515b7de664e7ea3e7891ebb92af3792430ab5554b3d0ad18c08cda961e28
53987760f3a31ec1a12f7283f48cb1c4fff34470a9edb70f406a4678c4a281cac412f36889421bda3391cc3ed52ee879ef2a
e17c844b5a7e1efe958220dfcfbc22c2c0c5197d0805b9d759aa6bc9398fb2f3dc4bc62e6f11942e107e3da973ef88ca6979
61a1fa9859c9c74acb408d3c1626fc594c1871e8d589446b367bf24a589a2b4ee10a4c957fc4c02403f80613e84764bdbf4b
6dd7085f73f8f65c57a365483ed9b89d8885f7244e0ecada5989ac7486b406cef1684240cf1cb93b1a6899eb994ee2820bab
b3a3453bbed30ec2519f28d97c1a983d

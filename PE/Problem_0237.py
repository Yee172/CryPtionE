# Let T(n) be the number of tours over a 4 * n playing
# board such that:
#    The tour starts in the top left corner.
#    The tour consists of moves that are up, down, left, or right one square.
#    The tour visits each square exactly once.
#    The tour ends in the bottom left corner.
# What is T(10^{12}) modulo 10^{8}?
# ----------------------------------------------------
# Analysis: matrix multiplication
#           Hint: only consider the last column of each 4 * n board
#                 1. --  2. --  3. --- 4. --        5.
#                      |      |             |
#                    --       |    --     --  or       --
#                             |      |                   |
#                    --       |    --            --    --
#                      |      |                    |
#                    --     --     ---           --
#                 The corresponding state transfer matrix is
#                 1 1 0 0 0  state 1
#                 0 0 1 1 1  state 2
#                 0 0 1 1 0  state 3
#                 2 2 0 0 0  state 4
#                 0 1 0 0 0  state 5
#                 Notice that only state 1 and 2 are valid, others are the middle states.

9ee723fdeae3f6ee566eb4a974eba1bdb1fd98eb272f13b11faaacf02f96339cc6d7290476a227f8b0c8364b2c8840a4ab44
cdff6342cdb2aaa220f80526eb34d403d8072f0f769fc6bf91da73cf97eeeee4186741e93ab5b3a958f54a7e36b21098474a
9ee8085baebc643929d4a6e534638fa0140590894229141e76b9894f1dd95645d32935092f565bb5a3555880c6135a840c17
9763b3f4d0a983e9fd60dde5da966c95452956f7d81e8f1ce11460f3409c251796631e8a176bda3cd1b44fe2ae66e9bef2ba
f1f54442a8bdf5279783ef1df0928131caac40af901f2a6c65d396e9fe46ee670007d3589720b0a65379bc3086d7d19f9b7e
0b06312382b67c2d2d7c07d7f1a56719e3a78cb0c139e57fbf4189990c26f5d6d740cb945733af63b5b87a22f449fbc6b8d3
cd9deaeec0fbd4c2005116c2f5e5c1be408bf32c3506812b558720cbca0e104338e8e9885f4f2ff85902d21ea6fa1827463c
4477610e7cd76bc1fa4003dd3bcdbf5dab8ccb33550f7fc0bdaf2b150ff1f1742593409103d19a5d684c08936c22ec0a2049
959bb0193085c18dc6f6cd0d305c5515971711af50dc77e14ad869af15c22f32484896e1a868716e6b5824b053d320856f86
85488a850c0707255d1f71a83600407003fc4a5cc463c5e884b30634054a422638513ea8a2e4b8b54604b1e6e677d5b84019
c27be117b7b9bb30d4bfb1f2156563247c2d2d7c780140d303adf1c910e2f5c942e77074ac3d391166421f300b21583c8b2a
cf37aafbdb719091cf366d002e7956c4c5effcb55ae5ddb3a84c4ae50ff127dfcd72a6f7928d1aa588d33e9d44621c02cc3c
c5ec87b54018a3c540e63caa1dfae5ba6925f351aa61df87514c86711ea93e80c4941029ce67c56d312f728a79c6f767a1af
c92ed5b80f42e01ac60858b835510919a9fd984158ee8927edf3f551dfbd93492189a7fe7e2458425547f17d4fdaf2bdae93
06f93b3e444016ddc12d580ed2a7accd263d0623ec3ae969e64ea84d2bef25392439945557fadd1b052e6fba9ca36263e8a4
67ce53f42653a5b62675104ba10e80e743c5c503361a3c25c348

# Consider a w \times h grid. A cell is either ON or OFF.
# When a cell is selected, that cell and all cells connected
# to that cell by an edge are toggled on-off, off-on.
# The goal is to get every cell to be off simultaneously.
# This is not possible for all starting states. A state is
# solvable if, by a process of selecting cells, the goal
# can be achieved.
# Let F(w, h) be the number of solvable states for a
# w \times h grid.
# Let f_{1} = f_{2} = 1 and f_{n} = f_{n − 1} + f_{n − 2}, n \geq 3
# be the Fibonacci sequence and define
#    S(w, n) = \sum_{k}^{n} F(w, f_{k})
# Find S(199, 199). Give your answer modulo 1000000007.
# ----------------------------------------------------
# Analysis: brute force
#           Hint: https://www.jaapsch.net/puzzles/lomath.htm

8f202bc3ac25bae0e289a8c57fbf0f613bf0474b02c1a27c4953d5424810ed4a9a054320863de6236f25d8df2c0b0610b5df
10767f49b6c0476abafa3f4d0a88a68e9b710358da8cdaa6b15a9fa5d6d92dc7cd198a7d46c5befca45f6bd24bb1e3dae5b6
11c128f0e2cad2996cf534d607f2bdeea359ce363b13536a939063b2d717a0b4a5ac8b4725b6330fff74d64256a1662984e6
fc4f6c5737b5c05acb6d7a6660a382b8f82bc323b5fd99714448499dffb39043af6b5a7037382568fe408d1f952854104292
ed12e51daea1f305b8f540f076cac49f92216d36301fd4e9b3677c26b83af85bdb962cf7459d1e9dd85a6c58b4b5b55b1214
22cb524b07007c2d2d7c19a49982ff797554986da67a34ecb77d18238ea2b7d1dd22f571db595f9c367b5b5f823c16121997
a9ecf158918098d8c378ef976d1261433685c3f065fd4fca4a49a7ab024ac3e89827b5f0b78fdc9682b55a045e9ca4049326
40f4af4e7fa5859c58cc054e655d9bf6e1813be663017fa428c82a4cfdda98687b8a11037697246f5c4955bc411093ec7e02
d9ec5d3a2828cd72121d7c368146d80db57d3926040687de709c09465732de7644e20fc7b209ff7ec498fe0a1eb8970e64c5
075aa9f33ce992d73584dee877ab90b989e2cdd1adcf110e44dec5cec5b55769db69cbd92e51d2a7116e554f093ff4279c08
40c5f98d8a96bd614ae6dad77db5f4387c2d2d7c6ef0333f61917d1d14b038870ad6da6747f20d05d5eb4713928a3a0f3e2a
e63d4b6b5a173154dc09aeeaa91aaa8ec2948accb633802becf486b4decb0d2c8921161aecdfb62b4214164dc2d6b821a856
0f7b69eaf8aa2916880e6fcfa660967cf708bc36c211d5bce583a907efa8ac32627a7dffb70caa3e94dddcdfa451289dd05a
5d882562fce0efc93c4db54d59afc106820bfec901901fe41045a339e20b2a90e67c954e18b9c0c2bd71399118c8a887ac4c
9f8066ae0562fbc003377a25debba07678c728f285c996f0b9e7ad90c63c2e1d6e2c2e0dbaf9dcb2bce3f7d1a1d6ef6e523d
45ebf389bf07ac95c3301fc8d6cefcfb816a0b7d93f6e9deeec57c2d2d7c1449f73ec683f170abf9617b0ad20e9e26453876
4dd9ed8e8a065765dc975b2a1fa19beeec1b7147118a67b67c0d3ad79f132eedde7a1611f3b8064a4adbd51de7229d65ffd1
0569fe1d066dac3ee2c2fd79230e7263235a6273797b9437d68ecc189ca5cd1006ff82d89f4fb0ea8211b78e54830db0df48
9a5d3de681469e481875f5664cf658cab3ef0ab2502bd57cb6c466e8dd2fedc2822288d1899d7c20a60ff6e1dd2cfdc51a8c
b8352d75869976d737e230adb5da164257a36c27245cfbacd3da0be8b5e9967a42b9219d9e690ce69c1f0a099285ba869e24
978c24a359b23f10350b11e134e7339c08dd32ff7873117e93c7bd81c31d6fa2c330bfeb7c2d2d7c6a9fe546905ea59c1606
809d578b7bfad87c504970e176d141d3f442ecf59f8b3dd691ffece3ad84543511afdf21d6b5a53421e9a3ef5fe59d822058
4282aad9fca7a3e9c2d8afc7b5225ad8b27eaa30aede93398602c96108ac37589226b74dd8932b365584828525b56d31427b
0a3da623d49e8321002f16fa665ef6504afb389697a6bf3e07af56668b2f5031244c5ab3e02269a13e9b9122f08f64d0fbbe
cbf1545b562a303eebeba6dec01e89678e7ca09bd0833a9f5f0c7515e31d79e8b04d2dad4dfe1e66ce7aa6787463a84e3eb7
e11677cf6e11ae5e819e64c23d57e4d5a07b3c33714d54cd1aad81366c1febc1e86fc19f94dc3800ea8b9f3f66c17c2d2d7c
496fd73fa5576c305239759602fdb6771fb1cde00bb2fb08394e60d5ce2f0317160ddea8191584fffadcd5658d27d51eba4b
9aa3a3254fdb20604fb93cd3115462bf047f95f330c0ca95684b95abeb9b6003e47b033fdb6e54af12fd2a6a7cea58334c21
eda7c6b459f68f4ffafc01ca40476d01681eab16a936e5000a34a7e9289feb5a428e33802ca67b413cea455da0844f48c7fd
a953b0c142a173ce4cd39c50df99f3673c473775b5110dee855a68e6189653a899bc79f92e228de539a25837061fed4aab2f
96946ff3906e713da1e65cd2d98478e339d72f8b93f080c74b526797e60f53b5fd7e8d05098dbadcb09e0a60661836f2b36e
a4e5e08949fa7c2d2d7c539f81a778bfafbcfc93cb0c30b594620b81bd002574b5ab7fc3835bdfc635b3b35b7a167e18e6e6
c9ee11717f3c94674dce1222f47da60d9daa99dc53ef909cd211294430503b2eb3f890b1530c8a3634139d550e54572190ef
b20481ab0f7753582749a638f245cb04a65cc8f240fb82822cfb91e10b4a737838fc46eb95edc5a0568e8b88ea63d73ab751
3e0f84e8d7913a6fd9567cf8db482d5761607ae11f1c9b9a0dfdbff1bd25621cfe618b5cd4ee069d6017c0a49092174261ea
35b80484228d5e6b105f86fde26e0270293ccabf4f1fa9433a975f13f91f0b05c3776577334e9a55f58c8910cf4bca281fe7
3b72440d4f5f3a8a7d7186e6cbf9507e7c2d2d7c9186781cdc7a348e49dcd77b8902a327374b065ffa9e662b433530eb2f0c
992b7b0b17f439bbd389323f55f7dfa949732c905897afac803ffb4887ed5dda21f6ab08e1203d6135975142bc4f59ce2987
d77b9b86c62c6e137294bfcfed93836f633b4fafd67c21c4fa9f510c60d859705de221cd527f3de3c09cf5211e2a4ba5f716
d2988e85aa3a3044c359e3559654ba6bcf59f66cf9e4ab2f310e8b6e475145f3fa0ce1aaad040c43ada780ab5a9651226508
328de369b471dcc4251031bfb50c4049c92226f63d613cbd9e5eb9235130a8961fe90a784a0bd75038e283fd0c321b9a12eb
4c548e7e61d809b05e9e0c227eb093fce52540452d062a775d8f7c2d2d7c5d99656f07968d6fbe24a56340c06674152dc276
0fb9f475de48d8aaa278d6d7d30e87bd36e1af465373d106684bcee3e7d377f18ac9d1f69d60a20a32c2487ca6eb9f4843c5
7cfaa8c72e8c8427c0126ad5d97cbfe9eef29c6460cedb65df540c9d547cd8a9b9f41e35aacf88869005cf9b2f9b469a273a
e857bcc052cd211be515d63c35c797a45bb4b2ee26a973f52f87714f2f35a64e15df74e7a6a66ec1b38c87841d2bb0335e74
b09bef4c754d47957cc939d3ff9bd44e6f61070a5e22d7ff016c44f1431a3ebc521d2fcc8d6d4baa0dab1b92b15692c5bb64
6f9c2053003da235eae3a46f3128d0bc605c4c6d9500ebb0adced1f90595852cf8e9c1f67c2d2d7c06c8950548f3f6b47e6c
0cb5f69eaedd0fb2bfeb7d7872cde607653e6ff6f26885e15c9a96d2fd1ec4b5c4cefcda6e0c5e5c86d5e60e3dc42a7e808f
b0c998a0eb29483d39859363b11ec987cd51816a94fbd3ec5911f8dc55bed8c4ce9c113e128aa1ed5affd1ef1959d25660f4
c42ed2afc530929c2a23b9dd21c3a00dac3208822fee1e8a957818892efee89b813256202fba18d2a0173b6eb343846b001c
7242717836f695d8312d3f7de46291f2ddbd71fb1e9801593155b515a529f845be85525374cd2e542618e2ddcd7bfb6000fc
32c2156f69ec4287c7315f6499f5a5998882fb2c4548acf836788f39bc2a77317bc3e510823f0da505f6524b1c417c2d2d7c
742069e0d8449a0973cde84d3231418e75fcfd53a2d1d37f4e9a37727d61d97075c0588e4bac84f39e2647e5e55c457a9174
490dc7da4dd7f27ad6fcbf03f493be93b3d85fe28acffb73033fa0fd7e52c562a99e2905e34ecba865a76a921c07b7a3a42f
c45a240ec0a49153f12877211c0a9488b6dea60ecc277b76b00363d2bf6ea4ad8312ab0b9fdec6872e0ec6732bf8bd5cd615
f435bf430b809a067e2fa21e7fa8e7a16cc9e3fa01fe10362d390c19ad09bc17ad0b228ab2940bbec517a1acf3ac62e9e2f6
c1dba79be8dd8636646ac6ec84b4adac1f5440910384168ddf948eda960610c2b2c0437b88fd01988fdf5d5cf59b0f27ac7b
2bf2cf9b5343
# We shall define an almost equilateral triangle to be
# a triangle for which two sides are equal and the third
# differs by no more than one unit.
# Find the sum of the perimeters of all almost equilateral
# triangles with integral side lengths and area and whose
# perimeters do not exceed one billion.
# ----------------------------------------------------
# Analysis: brute force
#           Consider two types of equilateral triangle: 3 a + 1 and 3 a - 1
#           Notice that 3 n^{2} - 4 = m^{2} has no integer solution
#              while 3 n^{2} + 4 = m^{2} has integer solutions
#           Hint: square of an integer % 3 = 0 or 1, but can not be 2

05c1f3b11d41d4e7f61bdd664bd2473061c092d5123fb8e19c2de623e8ae0833a4b56d57aafd46fa7dc40551c8687acb3e8fd2c8daec538d47e428a4a218b8bf7f3c2ea81d46de6872029e1deb35751e80180a03f247dec0aff6239f6343f997c53ee55c35cee3fdf01edce53b78735ef86d66766b0f4ee369113eaf177d0165640a75dc7dd62e17e34a98d474855a64013a126d022428ecc0fc0f6933f789fe13ca3cd9e00f75bfb7e14746d95502b33959a3bb73d418c37818585a6b9001990926d41ad90406cb04509c16955dcfa8e939fbdbf788fb040b7a1d1e331fd117297146a826fa9b238b1b7153b3c87d852fa2ab5945e838f7b806ac136de91c347c2d2d7c44ecdc1b0b9150ad1a71aac0e25c3c80b81e697752eaa10e5dfe5327cf23d0d7f6e957167bf1be7b91714166ee046ef8e5124898b621662c5a47c1d28234b634e058c3a02fcbf18656f638cb724648b01eaa4891a8833486cfd6ae03dc76e50f50432dcb083069dbb623021f1f72cc5bc277a04a14d3648051f4df9c2d0e5e380de2151c3017f3dd0cb3d5a9c16028c88436016e319eb64b206b9bcd599f9658ac473b9122441d4d1513e0750b8c9abed265a4e2f59bc58fe7e05b74159f5909e72df1ec3b1816ead1db7b2df33a1d4b421b6dfde3bc2df280248eb21366531da6ff6a8ce864ceb23664e99e24b07d885d553a7f2b3dedd84e0e63cc009a403f

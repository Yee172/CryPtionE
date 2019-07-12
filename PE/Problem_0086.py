# A spider, S, sits in one corner of a cuboid room, measuring
# 6 by 5 by 3, and a fly, F, sits in the opposite corner.
# By travelling on the surfaces of the room the shortest
# "straight line" distance from S to F is 10.
# However, there are up to three "shortest" path candidates
# for any given cuboid and the shortest route doesn't always
# have integer length.
# It can be shown that there are exactly 2060 distinct
# cuboids, ignoring rotations, with integer dimensions,
# up to a maximum size of M by M by M, for which the
# shortest route has integer length when M = 100.
# Find the least value of M such that the number of
# solutions first exceeds one million.
# ----------------------------------------------------
# Analysis: brute force

c4958d46e4c397d50fe08cdf4950984f9168a5ab6dd88e435471d11f8e0e3aa9d8bb3b814fe1dd87f71879165276ff74802eccaf30ab35774e646a3b6ead0c97e4086287b397cb7c59d132e1b09b0e246d9506668a36db3749c1a8001a818a739f47dc2e193cebc3f1b7d9e8e4004b6f4b7dbdf6c2938ef6fd27439298c03c7d754d061b1263936f84574b70995d54635e56fcf7bedcbdba8ae169cc39c1ebe4995473ff933658481327153ba919600eaf7da3869e2d1c6f87aeb6367eaaa483a396eb8dec118b2d35ebb1d8d5ffc4749b3fac2761d78b6c3b9e1dc0d04dc27488d74d4724624cab5fc6cebd7e929a807567752087b83de22a866e8bb77e719c7c2d2d7c0b15cd2235ba96fc8d2eac0f9d4948e9b5a980577ae1853379106bc05ddc5b5d25bdbc350c4a319d33b08d802f6d61e8fee1aa1c46b2f8c9646afdf6a5dfa84dcb483bbfc413cf4d220327ba43e28781b47b4c02fd427de985c6d3fcad37473f991c9b58fa81840f2c49dcd3887057e0190072dd6d0e5d2dc07c29a29743cad6ca01bca92e4213aad948f7ad83254fd56d5ed339a73c8cc255ab576705ac8a2842b5e8dc631b693d2e9454483efcab9a650c6adbc674ec4ed8d9c05026d8f9dcb4694da51e31299f40929f18346b53e52d843e7095eca48fa330e7c5ee4c9ca68c65fd05b43ae43977be1c56899204e440eb0f15ced133305a19676fb84eb312

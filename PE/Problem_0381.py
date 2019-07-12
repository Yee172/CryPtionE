# For a prime p, let S(p) = (\sum_{k = 1}^{5} (p - k)!) % p.
# Find \sum_{p = 1, p is prime}^{10^{8}} S(p).
# ----------------------------------------------------
# Analysis: Generalized Wilson's theorem.
#              (p - 1)! = -1 (mod p)
#              (p - 2)! =  1 (mod p)
#            2 (p - 3)! = -1 (mod p)
#            6 (p - 4)! =  1 (mod p)
#           24 (p - 5)! = -1 (mod p)
#           Then, we can get that S(p) = -3 / 8
#              -3 = k p - 3 (mod p)
#           => -3 / 8 = (k p - 3) / 8 (mod p)
#              p^{2} = 1 (mod 8) for every prime p greater than 2
#           => 3 p^{2} = 3 (mod 8) for every prime p greater than 2
#           => smallest k = 3 p % 8, such that (k p - 3) / 8 is a integer
#           => S(p) = ((3 p % 8) p - 3) / 8

05e883b4ca1f50b7b1e4d25b5a2817038e90b1295483152591557c8af42e0f751824c60053accd6e6c31c98ef8cd47fd21fd3a7ca3d866dd9249710e156130afc328d01bc9bd28d08faa5de706bd41d09881947548a275d5ed75062e965e2c6725ebdf1d301587467ef988cc06fb1b4e57aff58d0cf9e9d4dee22d0886cb6f7338abaca1a4de16764bf9b9d23faf428baf3028aa63a461f7799b9ee071c50bf82064ca0c312776e0663a4969c47a3c6123776893b478e0dd44ee8dea8d45110c2698add17cb7498af0a5bda92161d94b875fb8ae2af2df958449423845e89eedb2e0dae4265d17f532c252a0691df42d26de923411ecafdfbfedcf3c45a1b862

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

ad4a988d4d299809ef3748bd63ca030c6b9eb9f6f7f71fc28673da12eff7f163ce98994fb651f27fc1a45860156ca6327fe4
7075c0b7ab2818e6fb9c4287bda8ab6fb70c7a6d0cb5ad3896418547776a7068772210c55ee6ceb6fa7c4f8d19a9edeadefb
23ca4133e8c02b0929fe6ca7697c9ecbea363875fd5df4a066a5a0b9e5a6f324681bda846e6635c484920ea0a8fde4921493
7a6bf3e03854ac0d877143843b803f881db5da334f9015e6bcd2b6aa81ded3c5e18d0d8ec752a11b33a7bcd0e31cdd4c3acc
ff7cef610f16e44d422e8abcf69046ed31d1d6f20cc174ea7acc338039c6028f338d29e89d8da8595a187f1f656febd411b8
31c060ffe96b

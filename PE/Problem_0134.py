# Consider the consecutive primes p_{1} = 19 and p_{2} = 23.
# It can be verified that 1219 is the smallest number
# such that the last digits are formed by p_{1} whilst
# also being divisible by p_{2}.
# Let S be the smallest of these values of n.
# Find \sum S for every pair of consecutive primes
# with 5 \leq p_{1} \leq 1000000.
# ----------------------------------------------------
# Analysis: brute force
#           Let n satisfies that
#              p1 // 10 ** n = 0
#              p1 // 10 ** (n - 1) > 0
#           Let S = s * 10 ** n + p1, then
#              s = -p1 * (10 ** n)^{-1} (mod p2)

ad3602684d800192ee928e68d56744422e67f5fb5da2eb55852197759c6868d0b95f32432486ef4ac6cbfc444f6e228afac4f1ef0e9b2a9c10527f4f4854711bbe6027e35d8d79d1ae375c3bb327b5cc2d91dabbd7949aa11877d85f430799a093c5b91c05f5d161b3480cf8a1e8779ba989583bc858fdddb3855b4fe86f08771ff5407373f6d1b78c735e09bd3167dac3a9e95efea7b88c34b9273544fd81606d0d62a919a457bd368438fa194cc86161c1d1c1251780ca4ea395a0b6b09cdb745ec7397509c78193612e0055e125026048ef4599e00df638d4d827c4ee790f845386ba767fd13ed6a637a305b4bc8a90144977dfae66f311bd528f302aa0977c2d2d7c508e8f5e7cd98ef80989d038f1f5a4810870bc23edbaaac883434feb22e20b860883b3700426cc74e5a1751801de151a71385b6752796868c5d93cf4d1b5913084d569c888510a8d3cd40323705ae5a97efa0cd62ea9156b19ebfe4c770a068f264f56513ed7ead779ac117cbc83db91bce98a8c19f3288adc991f550657e033c7641e1f11a5ead074827becd3365f3705634967cb9555713c3fed4f46b120cbb690f0952157b4f948625fdb7e5292114779637ee78c2ebc5d9116ce2345515cf98ff9c4f9250d31fab17ba6db8dc5a8678ec7fc174a773d5942049a81230219e5b34becd5b3d2b258cd88764d9b4fdded5320d31d6cbe4df3db8c054cfad897

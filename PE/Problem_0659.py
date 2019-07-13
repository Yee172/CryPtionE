# Let P(k) be the largest prime that divides any two
# successive terms of the sequence n^{2} + k^{2}.
# Find the last 18 digits of \sum_{k = 1}^{10000000} P(k)
# ----------------------------------------------------
# Analysis: brute force
#           p | n^{2} + k^{2}
#           p | (n + 1)^{2} + k^{2}
#              => p | 2 n + 1
#              => p | (2 n + 1)^{2}
#              => p | 4 n^{2} + 4 n + 1
#           p | n^{2} + k^{2}
#              => p | 4 n^{2} + 4 k^{2}
#              => p | 4 n + 1 - 4 k^{2}
#           p | 2 n + 1
#              => p | 4 n + 2
#              => p | 1 + 4 k^{2}
#           We only have to find the sum of the largest prime factor of 1 + 4 k^{2}
#               1 + 4 k^{2} | 1 + 4 (k + m)^{2}
#           <=> 1 + 4 k^{2} | 1 + 4 k^{2} + 4 m (m + 2 k)
#           <=> 1 + 4 k^{2} | m (m + 2 k)
#           <=> 1 + 4 k^{2} | m or 1 + 4 k^{2} | m + 2 k (in the case of 1 + 4 k^{2} is a prime number)
#           <=> m = n (1 + 4 k^{2}) or m = n (1 + 4 k^{2}) - 2 k, \forall n \in \N
#              => 1 + 4 k^{2} | 1 + 4 (n (1 + 4 k^{2}) \pm k)^{2}, \forall n \in \N

9a527b9dd0456b6a926ac64fc33cde9758acf47efa78f34cc57d94471ad06b2e8e6f4eb764a5717274de4d6761c1c93b2d6d
e42fb66b378550e5fa816d7a2143e95be5c6ae5ae8c65a3ce3464aa5e4d73f808288962751ba424722eb1eb15f67e2e33a5c
742390f46a8f39ad895e92d8a401195dd0a5677bcb8c4af7dea0ccc139883b7aaeac7403b5b6ae91f25b239468d7a672175b
8d5840946029a0f6b9af0c706d422786373b1a7e418359490df0b6e4c4f35788606f6ed28f9ca2288b2cb5ebf8c7a59f0a90
c00434faafda4d655f9f240363f2297701c7141d741807d02f5b161dd829ea6768dcebc7bd06303543a58bc483cb4fb92149
b7b86d54cd1b7c2d2d7c5d82bf6ebd450fb6bff1ffed5676bcc530963709560752045a7b0dccf1c8ad8add177a14f9a99c49
e209c1fd9fe6d74c39d416c5697804abdf501c3c8fbf2c55a76e2e9d5764ef3f8affd2200740499fdf12f86ebb392b26c09e
73dfad61f673dca7f968d51b7aed399f3e69e8158cda2e564bc63646936b2a658e014f8c5d2c3cc6c9932d3a7dd95703450f
1479ae4f354f35261ac5d204d1795140e4bc26beb204813d45e0158111edb2d0f86106c35eb90d365f11813c9d7235a0a9cc
a02fa849b01703eb7a64981e918fd8d6c264522e0b8a2e11b25eb413bd3ca89c53f794985061822dd68374779058a17a692e
78312b727a1c11f3bfc429e73411646c7c2d2d7c7cde1935a0ab50687e9d654d876fd6435e23afe465dbf6cecadfca4b93b9
2b98ca40e2125e4beeac51f8b430df776746df1df425c4072ac30ea5782b3cd37d1e55c7022b3eff9acb22b81cf55e63754f
557b375dc74d4a96f5477326943e4278d9be7fff62d2af08bc754298e829b5dfff8e280d797afdefc97b210a7f0e766d584b
943c660f8409db801f81507fc22f6de38c607a1ac7fa79f2f9e66dd486be7f129051ed941b3a45841c771cde8445d81d143c
b5f6d4ebca7bfe55a6f1b320707a0ba2f07452b1c85564ed1e0d977bdce9fe511560e68ab833dd1802b85f42ba1ffe829cef
9c2baac5a5ca8bfb0424b8d67038e70dfb5d26f2c188d934d964

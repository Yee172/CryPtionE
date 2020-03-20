# A secret integer t is selected at random within the
# range 1 \leq t \leq n.
# The goal is to guess the value of t by making repeated
# guesses, via integer g. After a guess is made, there are
# three possible outcomes, in which it will be revealed that
# either g < t, g = t, or g > t. Then the process can
# repeat as necessary.
# Normally, the number of guesses required on average can
# be minimized with a binary search: Given a lower bound L
# and upper bound H (initialized to L = 1 and H = n), let
# g = \lfloor (L + H) / 2 \rfloor where \lfloor \cdot \rfloor
# is the integer floor function. If g = t, the process ends.
# Otherwise, if g < t, set L = g + 1, but if g > t instead,
# set H = g − 1. After setting the new bounds, the search
# process repeats, and ultimately ends once t is found. Even
# if t can be deduced without searching, assume that a search
# will be required anyway to confirm the value.
# Your friend Bob believes that the standard binary search
# is not that much better than his randomized variant:
# Instead of setting g = \lfloor (L + H) / 2 \rfloor, simply
# let g be a random integer between L and H, inclusive. The
# rest of the algorithm is the same as the standard binary
# search. This new search routine will be referred to as a
# random binary search.
# Given that 1 \leq t \leq n for random t, let B(n) be the
# expected number of guesses needed to find t using the
# standard binary search, and let R(n) be the expected number
# of guesses needed to find t using the random binary search.
# Find R(10^{10}) − B(10^{10}) rounded to 8 decimal places.
# ----------------------------------------------------
# Analysis: harmonic series
#           Hint: it is straightforward for B(n), while R(n) is quite difficult
#                 We can find that R(n) = 1 + \frac{2}{n^{2}} \sum_{i = 1}^{n - 1} i R(i),
#                 which can be simplified to (\frac{n}{n + 1} R(n) - \frac{1}{n + 1}) - (\frac{n - 1}{n} R(n - 1) - \frac{1}{n}) = \frac{2}{n + 1}
#                 Then, sum them up, we can finally get R(n) = 2 \frac{n + 1}{n} H_{n} - 3, where H_{n} = \sum_{i = 1}^{n} \frac{1}{n}

05f155c41d24f193eac717dfad947b6fff2bcc51dc6b577b15ace4e04e1f3e33b8b45f4c6536c49ac0e5302b15406e1e8711
d6ef6ea7b4e0d0fc84a59af34e72ff84fb3f95ef1c383688f8d58744a73ff37faa42f4faf4e30ed192be94157fb1759027b1
38ec3d008090374f844137fc22dab839a62aa98e99282e7d1c74b0ad08ee5130773b45fbe13b25e0a63f47dd54d8a46c8871
dc7bafeb9ca7525c510feebfdb1ea1b8811767b3d086d0f27b56ba9e1521a5394bbe91ade09f3d6ebe17a0640a852857a943
f9a4bb65b882477b18bed2cac016b6ee58d4d590acb15c74034c86c928e819d4cb98c04ff234d307c4653a07c2048c857b98
4751c84c9cdd7c2d2d7c5001262047eac973a59eebbf8e2fea6f5ba8def8a9e82badf3f8eb9f9f70eeed51997e380a8a5f58
7e7137db8eaadad0a2480f435518eb26c57d2fac528fba74a72142cbb0035180c0323758bcd7e8748637382107c9e8e8b656
a135cb44902bdb90043ade9bda4ece4850bdecc5d5b02cdad34d1f220044500d503f773ecf0a005ec7fb1a4de506070c9eb6
16fec9a5611a1418b9e8b02dc705a3862ec0398f73219080dba7679cb5ba580af790fa1588e33f76b96d827880f232ccb774
2c9ec460a9dcc6165d203ed17a01c0859461d7b7d8b1e199843a01844750d5c94c2552f299cda1970d92f51b511b2c146323
685e7a9ed3fc892d64ecc3b5c18935757c2d2d7c1f30c4af8101e05d529e493c9d4fb5eb48f12a7f32d9ad36af2908bb48be
4bbf5b748cee7e8862060d2ae23d10582ca78d39e7c21909bd61f2e6fbf0b4c1392c943781a1a20233be047a309463353107
1d2d9c5c1c6e5255f308327326249394226bc04a3edac061a7455b8c3374aa2947dc5a769f47d3f0ecf05468d98fb898d193
f6975f4d2a67bafa287451856b6e38bfd0613228b6c2274dfd28f5434461dd47a42ffd160683552cd03ba3e793c5c9f5fdc5
5bd34d7e98a3a3afa8b2fd1f2d670c1813fc4a50ce4627ff02015ddd9765c09aeb4605a78ce41ebbd4e48e50277d5c181caf
9690be5b16ca59541dcb47459536be0908f42e3599278066a94e

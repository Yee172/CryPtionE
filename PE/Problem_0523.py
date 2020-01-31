# Consider the following algorithm for sorting a list:
#    1. Starting from the beginning of the list, check
#       each pair of adjacent elements in turn.
#    2. If the elements are out of order:
#       a. Move the smallest element of the pair at the
#          beginning of the list.
#       b. Restart the process from step 1.
#    3. If all pairs are in order, stop.
# Let F(L) be the number of times step 2a is executed
# to sort list L.
# Let E(n) be the expected value of F(P) over all permutations
# P of the integers {1, 2, ..., n}.
# Find E(30). Give your answer rounded to two digits after
# the decimal point.
# ----------------------------------------------------
# Analysis: brute force
#           Hint: if the first (i - 1) elements are sorted, it would take 2^{j - 1} steps to move the ith element to the jth position, where j < i
#                 Under the condition that the first (i - 1) elements are sorted, the ith element is evenly distributed through 1 to i
#                 Therefore, E(i) = E(i - 1) + (\sum_{j = 1}^{i - 1} 2^{j - 1}) / i = E(i - 1) + (2^{j - 1} - 1) / i

7486cf04f68f900a442031c08b37ac1f2069e579885bfa48d684a6fb7579f638dee50fbd2b83ccba24ac13fa4c2595da91a8
0fb4f786356e7d84b61cfe402a67b16d260bae7af389f57665e02ac3ce2337f338a780009617b84cc95ee4cf716b482506b1
92f633e00fd64fadeeb6788c8c3a97acd3e7de6d2b7dfbaaa33d4d3c1651241700dc278c03dfac6272fef9441ba873f33570
445445cca59ca116b0059d338143079c1e7ea5d28ebfd470d95c1dc158c609159e96e3ff5f47cee1e2f2f8c16de37a92daf4
7b4c9c44b89e7a5501ddd96ae3c359feef16f42939221217ea673105d0ecba3fca477aec383ec54f2443fcd5b17219452ac5
9e34a47f202a

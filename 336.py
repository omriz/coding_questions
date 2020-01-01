# how many ways to create a max heap from an array?
# Top of tree is always the same
# 1) Take out the max
# 2) on remaining array divide by two to get the sizes of the two subtrees Selection is (n-1)!/(((n-1)/2)!)^2
# 3) sum the optional sizes of each subtree
# 4) Array of size 3 has 2 options, size 2 and 1 single option
# 5) find how many duplicates we have, remove that amount from the sum
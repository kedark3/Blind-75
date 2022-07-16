# this algo only works for some inputs because python integers are arbitrarily large.
# in each step we update a with sum by taking a^b which is a XOR b
# and update b as carry(shifted left by 1) as (a&b)<<1
# when b becomes 0 we have our answer in a.

class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            tmp = (a&b) << 1
            a = a ^ b
            b = tmp
        return a
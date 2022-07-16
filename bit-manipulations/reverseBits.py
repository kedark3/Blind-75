class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        delta = 31
        for i in range(32):
            temp=(n>>i)&1
            result = result | (temp<<delta-i)
            
        return result
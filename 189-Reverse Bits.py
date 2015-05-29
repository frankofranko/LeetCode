__author__ = 'HsinYeh Lin'

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for index in range(32):
            ans += n%2
            n = n>>1
            if index < 31:
                ans = ans<<1
        return ans
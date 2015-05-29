__author__ = 'HsinYeh Lin'

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        ans = 0
        while n != 0:
            ans += n%2
            n = n>>1
        return ans
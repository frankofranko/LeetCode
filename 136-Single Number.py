__author__ = 'HsinYeh Lin'

from operator import xor

# A = [233, 132, 132, 405, 233]

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        answer = xor(A[0], A[1])
        for index in range(2,len(A)):
            answer = xor(answer, A[index])
        return answer

# test = Solution()
# print test.singleNumber(A)
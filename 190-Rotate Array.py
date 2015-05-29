__author__ = 'HsinYeh Lin'
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        left = len(nums) - k % len(nums)
        i = 0
        while i < left:
            nums.append(nums.pop(0))
            i += 1
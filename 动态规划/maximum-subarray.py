# https://leetcode-cn.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxval = nums[0]
        for i in range(1, len(nums)):
            if nums[i]+nums[i-1] > nums[i]:
                nums[i] += nums[i-1]
            if nums[i] > maxval:
                maxval = nums[i]
        return maxval

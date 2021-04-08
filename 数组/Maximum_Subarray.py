# https://leetcode-cn.com/problems/jian-sheng-zi-lcof/
# 连续子数组的最大和
# 使用前缀和
def maximun_subarray(nums):
    mysum = 0
    ans = nums[0]
    summin = 0  # 最小前缀和
    for i in range(len(nums)):
        mysum += nums[i]
        ans = max(mysum-summin, ans)
        summin = min(summin, mysum)
    return ans
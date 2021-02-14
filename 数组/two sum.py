class Solution:
    # 暴力解法
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            temp = i+1
            while temp < len(nums):
                if nums[i] + nums[temp] == target:
                    return [i, temp]
                temp += 1
        return []

class Solution2:
    # 哈希表
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
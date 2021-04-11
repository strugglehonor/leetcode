class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        res = []
        for first in range(len(nums)):
            # i > 0是因为第一个不用排序
            if first > 0 and nums[first] == nums[first-1]:
                continue
            third = len(nums)-1
            target = -nums[first]
            # 第二个指针
            for second in range(first+1, len(nums)-1):
                if second > first + 1 and nums[second] == nums[second-1]:
                    continue
                
                # 后指针一直往前移动（数值越小）
                while second < third and nums[second]+nums[third] > target:
                    third -= 1
                if second >= third:
                    break
                # if nums[second]+nums[third] < target:
                #     break
                if nums[third] + nums[second] == target:
                    res.append([nums[first], nums[second], nums[third]])
        return res

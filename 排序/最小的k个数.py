class Solution:
    def smallestK(self, arr, k):
        def quicksort(nums, start ,end):
            # 退出递归
            if start >= end:
                return
            # 这里是nums[start]，不是nums[0]
            mid = nums[start]
            low = start
            high = end

            while low < high:
                # 其中有一个要使用=，否则循环不退出
                # 这里要先判断high。不然会报错
                while low < high and nums[high] > mid:
                    high -= 1
                nums[low] = nums[high]
                while low < high and nums[low] <= mid:
                    low += 1
                nums[high] = nums[low]

            
            nums[low] = mid

            quicksort(nums, start, low-1)
            quicksort(nums, low+1, end)
        quicksort(arr, 0, len(arr)-1)
        return arr[:k]
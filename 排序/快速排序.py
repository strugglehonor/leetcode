def quickSort(nums, start, end):
    if start >= end:
        # 递归的终止条件
        return
    left = start
    right = end
    mid = nums[start]

    while left < right:
        while nums[left] < mid and left < right:
            left += 1
        nums[left] = nums[right]
        while nums[right] > mid and left < right:
            right -= 1
        nums[right] = nums[left]
    # 退出循环后，left和right的值相同
    nums[left] = mid
    quickSort(nums, left+1, right)
    quickSort(nums, left, right-1)


if __name__ == '__main__':
    nums = [1,2,4,6,1]
    quickSort(nums, 0, len(nums)-1)
    print(nums)

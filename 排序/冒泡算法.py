def bubbleSort(nums):
    L = len(nums)
    for i in range(L-1, 0,  -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == '__main__':
    nums = [1,4,2,6,2,0]
    print(bubbleSort(nums))
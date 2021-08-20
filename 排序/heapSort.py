class Solution:
    def sortArray(self, nums):
        def swap(nums, i ,j):
            nums[i], nums[j] = nums[j], nums[i]

        def heapify(tree, i, n):
            if i > n:
                return
            c1 = 2*i+1
            c2 = 2*i+2
            maxval = i
            if c1 < n and tree[maxval] < tree[c1]:
                maxval = c1
            if c2 < n and tree[maxval] < tree[c2]:
                maxval = c2
            if maxval != i:
                swap(tree, i, maxval)
                # ??
                heapify(tree, maxval, n)
        
        def buildHeap(tree):
            # import math
            # for i in range(math.floor(len(tree)/2),-1,-1):
            #     heapify(tree,i, len(tree))
            n = len(tree)
            lastnode = n-1
            parent = (lastnode-1)//2
            # 这里i是-1,不是0
            for i in range(parent, -1,-1):
                heapify(tree, i, n)
        

        buildHeap(nums)
        length = len(nums)
        for j in range(length-1, 0, -1):
            swap(nums, j, 0)
            heapify(nums, 0, j)
        return nums

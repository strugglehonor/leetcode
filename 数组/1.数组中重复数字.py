# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    """
    总结：
        前面首先要加上两个循环,如果数组为空，返回false，
        如果数组有负数，或者有元素大于最大索引值，也返回false
        扫描数组，设数组元素下标为i，下标为i的元素为m，比较i和m的值，
            如果相等，继续扫描下一个元素
            如果不相等，比较下标为m的元素和m的值是否相等
                如果相等，就找到了一个重复的元素
                如果不相等，把他们的值交换，依次进行下去
    """
    def duplicate(self, numbers, duplication):
        # write code here
        if len(numbers) <= 0:
            return False
        for i in range(len(numbers)):
            if numbers[i] < 0 or numbers[i] > len(numbers) - 1:
                return False
        for i in range(len(numbers)):
            if numbers[i] == i:
                i += 1
            else:
                if numbers[numbers[i]] == numbers[i]:
                    duplication[0] = numbers[numbers[i]]
                    return True
                else:
                    numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]]
        return False



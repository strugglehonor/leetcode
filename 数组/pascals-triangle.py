# https://leetcode-cn.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        res = [[1]]
        while len(res) < numRows:
            newRows = [a+b for a,b in zip([0]+res[-1], res[-1]+[0])]
            res.append(newRows)
        return res

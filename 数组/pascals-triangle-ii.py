# https://leetcode-cn.com/problems/pascals-triangle-ii/
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        while len(res) < rowIndex+1:
            newRow = [a+b for a,b in zip([0]+res[-1], res[-1]+[0])]
            res.append(newRow)
        return res[rowIndex]

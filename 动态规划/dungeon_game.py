import sys

'''
@ calculateMinimumHP
@ param
    int[][]
@ return 
    int
'''
def calculateMinimumHPByRecur(dungeon, row, col):
    if row>=len(dungeon) or col>=len(dungeon[0]):
        return sys.maxsize
    n, m = len(dungeon), len(dungeon[0])
    if row == n-1 and col == m-1:
        if dungeon[row][col] > 0:
            return 0
        else:
            return -dungeon[row][col]
    # 分别计算往右走和往下走
    right = calculateMinimumHPByRecur(dungeon, row+1, col)
    bottom = calculateMinimumHPByRecur(dungeon, row, col+1)
    needHP = min(right, bottom)-dungeon[row][col]
    if needHP > 0:
        res = needHP
    else:
        res = 0
    return res+1
    
def calculateMinimumHPByDp(dungeon):
    n, m = len(dungeon), len(dungeon[0])
    # dp[i][j]表示从i, j出发可以救到公主的最小生命值
    dp = [[0]*m for _ in range(n)]
    dp[n-1][m-1] = max(-dungeon[n-1][m-1], 0)
    # if dungeon[n-1][m-1] > 0:
    #     dp[n-1][m-1] = 0
    # else:
    #     dp[n-1][m-1] = -dungeon[n-1][m-1]+1

    for i in range(n-2,-1,-1):
        dp[i][-1] = max(0, dp[i+1][-1] - dungeon[i][-1])
    for j in range(m-2,-1,-1):
        dp[-1][j] = max(0, dp[-1][j+1] - dungeon[-1][j])

    for i in range(n-2, -1, -1):
        for j in range(m-2, -1, -1):
            # right, bottom = _getValue(i-1, j, dp), _getValue(i, j-1, dp)
            # needHP = min(right, bottom)-dungeon[i][j]
            # dp[i][j] = needHP if needHP > 0 else 0
            dp[i][j] = max(0, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])

    return dp[0][0]+1

# def _getValue(i, j, arr):
#     n, m = len(arr), len(arr[0])
#     if i>n-1 or j>m-1 or i<0 or j<0:
#         return sys.maxsize
#     return arr[i][j]

if __name__ == '__main__':
    dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    print(calculateMinimumHPByRecur(dungeon, 0, 0), calculateMinimumHPByDp(dungeon))
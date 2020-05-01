class Solution:
    def movingCount(self, m: int, n: int, k: int) :
        count = 0
        visited = [[False]*n for i in range(m)]
        def g(x):
            # 计算x和y坐标的值
            s = 0
            while x>0:
                s += x%10
                x = x//10
            return s

        def f(m, n, k, x, y, count):
            if x<0 or x>=m or y<0 or y>=n or visited[x][y] or g(x)+g(y)>k:
                return
            count += 1
            visited[x][y] = True
            f(m, n, k, x - 1, y, count)
            f(m, n, k, x + 1, y,count)
            f(m, n, k, x, y + 1,count)
            f(m, n, k,x, y - 1,count)
        f(m,n,k,0,0,count)
        return count

if __name__ == '__main__':
    solution = Solution()
    print(solution.movingCount(2,2,3))

# class Solution:
#     def movingCount(self, m: int, n: int, k: int) :
#         visited = [[False]*n for i in range(m)]
#         def f(m, n, k, x, y, count):
#             if x<0 or x>=m or y<0 or y>=n or (x % 10 + x // 10 + y % 10 + y // 10 > k or visited[x][y]:
#                 return count
#             else:
#                 count += 1
#
#             return f(m, n, k, x - 1, y, count) + f(m, n, k, x + 1, y,count) + f(m, n, k, x, y + 1,count) + f(m, n, k,x, y - 1,count)
#         return f(m,n,k,0,0,0)


# if x<0 or x>=n or y<0 or y>=m or not visited[x][y]:
#     return count
# # 这里不一定是两位数
# if x % 10 + x // 10 + y % 10 + y // 10 <= k:
#     count += 1
#     visited[x][y] = True
# else:
#     return count


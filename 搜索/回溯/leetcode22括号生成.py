class Solution:
    def generateParenthesis(self, n: int):
        """
        左括号：Left小于N
        右括号：right小于n，而且左括号数量大于右括号数量
        :param n:
        :return:
        """
        """
        思路：使用DFS
        1）当前左右括号都有大于 0个可以使用的时候，才产生分支；

        2）产生左分支的时候，只看当前是否还有左括号可以使用；

        3）产生右分支的时候，还受到左分支的限制，右边剩余可以使用的括号数量一定得在严格大于左边剩余的数量的时候，才可以产生分支；

        4）在左边和右边剩余的括号数都等于 0的时候结算。

        作者：liweiwei1419
        链接：https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        L = []
        def dfs(s, left, right):
            if left == 0 and right == 0:
                L.append(s)
                return
            if left > 0:
                dfs(s+'(', left-1, right)
            if right > 0 and left < right:
                dfs(s+')', left, right-1)
        dfs('', n, n)
        return L


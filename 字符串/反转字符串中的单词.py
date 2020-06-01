class Solution:
    def reverseWords(self, s: str) -> str:
        L = s.split(" ")
        for i in range(len(L)):
            L[i] = L[i][::-1]
        return " ".join(L)

# 错误代码
def reverseWords(self, s: str) -> str:
    L = s.split(" ")
    for i in L:
        # 这里的i并没有赋值到L，所以不对
        i = i[::-1]
    return " ".join(L)
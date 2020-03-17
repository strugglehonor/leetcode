class Solution:
    def replaceSpace(self, s: str):
        a = []
        for c in s:
            if c == ' ':
                a.append('%20')
            else:
                a.append(c)
        return ''.join(a)



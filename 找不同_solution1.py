#给定两个字符串 s 和 t ，它们只包含小写字母。字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。请找出在 t 中被添加的字母。
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for char in s+t:
            ans ^= ord(char)
        return chr(ans)

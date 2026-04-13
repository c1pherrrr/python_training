#给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True

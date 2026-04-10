#给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
#KMP算法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n,m = len(haystack),len(needle)
#构造next数组
        nxt = [0]*m
        j = 0
        for i in range(1,m):
            while j>0 and needle[i] != needle[j]:
                j = nxt[j-1]
            if needle[i] == needle[j]:
                j += 1
            nxt[i] = j
#主串与模式串匹配
        j = 0
        for i in range(n):
            while j>0 and haystack[i] != needle[j]:
                j = nxt[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == m:
                return i-m+1
        return -1







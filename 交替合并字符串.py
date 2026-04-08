#给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        length = min(len(word1), len(word2))
        for i in range(length):
            result.append(word1[i])
            result.append(word2[i])
        result.append(word1[length:])
        result.append(word2[:length])
        return ''.join(result)
sol=Solution()
a=input("字符串1:")
b=input("字符串2:")
print(sol.mergeAlternately(a,b))
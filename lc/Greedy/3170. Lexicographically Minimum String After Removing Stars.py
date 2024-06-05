"""
ou are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

While there is a '*', do the following operation:

Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
Return the lexicographically smallest resulting string after removing all '*' characters.

周赛400第三题
"""
class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        remove = set()  # 记录已经被删除元素的下标
        premin = [[] for _ in range(26)] # 记录每个字母在哪些地方在哪些index出现过

        for i in range(n):
            if s[i] == "*":
                remove.add(i)
                # 我们需要找到离i最近，且字典序最小的元素来删除，这样才能保证字典序最大
                for j in range(26):
                    if len(premin[j]) > 0:
                        preSmallest = premin[j].pop()
                        remove.add(preSmallest)
                        break

            if s[i] != "*":
                index = ord(s[i]) - ord("a")
                premin[index].append(i)

        res = ""
        for i in range(n):
            if i not in remove:
                res += s[i]

        return res
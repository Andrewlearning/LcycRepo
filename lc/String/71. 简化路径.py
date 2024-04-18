"""
In a Unix-style file system, a period '.' refers to the current directory,
a double period '..' refers to the directory up a level,
and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'.
For this problem, any other format of periods such as '...' are treated as file/directory names.

其实这道题，输入只有 "/", ".", "..", "...", "word"
我们只要处理好这些情况就好

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return ""

        # 因为一开始可能会出现 "/////C/A" 这种多重斜杠的情况，所以我们把斜杠去掉
        # 然后去掉斜杠后原位置会出现 空格
        path = path.split("/")
        res = []

        for char in path:
            if char == "..":
                if len(res) > 0:
                    res.pop(-1)
            elif char != "." and char != "":
                res.append(char)

        return "/" + "/".join(res)

"""
https://leetcode-cn.com/problems/simplify-path/solution/zhan-by-powcai/代码
https://www.youtube.com/watch?v=l-og2X5GibY思路

这题的逻辑就是
.. 代表返回上一层
. 表示呆在这一层，不操作
字母代表层数
最后我们按层的要求把字符串输出

所以操作方法是
遇到字母，那么把字母加进结果
遇到.., 要是不可以pop了，就不处理，要是有元素，那就pop
"""
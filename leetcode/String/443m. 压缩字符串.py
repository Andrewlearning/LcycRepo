"""
给定一组字符，使用原地算法将其压缩。
压缩后的长度必须始终小于或等于原数组长度。
数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。
在完成原地修改输入数组后，返回数组的新长度。
进阶：
你能否仅使用O(1) 空间解决问题？

示例 1：
输入：
["a","a","b","b","c","c","c"]
输出：
返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
说明：
"aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
示例 2：
输入：
["a"]

输出：
返回 1 ，输入数组的前 1 个字符应该是：["a"]
解释：
没有任何字符串被替代。
"""


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # 重新整理字符串的指针
        k = 0
        i = 0
        while i < len(chars):
            # 相同字符串的右下标
            j = i + 1
            while j < len(chars) and chars[i] == chars[j]:
                j += 1

            # 得到相同字符串的长度
            length = j - i

            # 给头字母赋值
            chars[k] = chars[i]
            k += 1

            # 假如是length > 1的话，说明要往后面填数字
            if length > 1:
                for c in str(length):
                    chars[k] = c
                    k += 1

            # 更新左下标
            i = j - 1
            i += 1

        # 返回我们填完数字的最后一位
        return k

# https://www.acwing.com/video/1844/


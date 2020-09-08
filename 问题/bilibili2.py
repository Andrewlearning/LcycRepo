#

#
# class Solution:
#     def SpiralMatrix(self, matrix):
#         if not matrix and len(matrix) == 0:
#             return []
#
#         up = 0
#         down = len(matrix) - 1
#         left = 0
#         right = len(matrix[0]) - 1
#         res = []
#
#         while True:
#             for i in range(left, right + 1):
#                 res.append(matrix[up][i])
#             up += 1
#             if up > down:
#                 break
#
#             for i in range(up, down + 1):
#                 res.append(matrix[i][right])
#             right -= 1
#             if left > right:
#                 break
#
#             for i in range(right, left - 1,-1):
#                 res.append(matrix[down][i])
#
#             down -= 1
#             if up > down:
#                 break
#
#             for i in range(down, up - 1,-1):
#                 res.append(matrix[i][left])
#             left += 1
#             if left > right:
#                 break
#
#         return res
# s = Solution()
#
#
# print(s.SpiralMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12] ]))

# [[1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [9,10,11,12] ]

#
# class Solution:
#     def GetFragment(self , str ):
#         if not str and len(str) == 0:
#             return 0
#
#         dict = {}
#
#         cur = str[0]
#         count = 1
#
#         for i in range(1, len(str)):
#             if cur == str[i]:
#                 count += 1
#             else:
#                 if cur not in dict:
#                     dict[cur] = [count]
#                 elif cur in dict:
#                     dict[cur].append(count)
#                 cur = str[i]
#                 count = 1
#
#         if cur not in dict:
#             dict[cur] = [count]
#         elif cur in dict:
#             dict[cur].append(count)
#
#         res = 0
#         sp = 0
#         for key in dict:
#             res += sum(dict[key])
#             sp += len(dict[key])
#
#         print(res/sp)
#
# s = Solution()
# print(s.GetFragment("aaabbcaaaa"))
#

class Solution:
    def GetMaxConsecutiveOnes(self, arr, k):
        if not arr or len(arr) == 0:
            return 0

        left = 0
        right = 0
        count = 0
        res = 0

        for right in range(len(arr)):
            if count == k:
              res = max(res, right - left + 1)
              count = 0
              left = right
            elif arr[right] == 0 and count < k:
                right += 1
                count += 1

        return res

s = Solution()
print(s.GetMaxConsecutiveOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))





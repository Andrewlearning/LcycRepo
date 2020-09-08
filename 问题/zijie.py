
class Solution:
    def maxProduct(self, arr):
        # write code here

        if not arr and len(arr) == 0:
            return 0


        res = -1
        positive = 1
        negative = 1

        for num in arr:
            cur_positive = max(num, positive * num, negative * num)
            cur_negative = min(num, negative * num, positive * num)

            positive = cur_positive
            negative = cur_negative

            if max(positive, negative) > res:
                res = max(positive, negative)

        return res

s = Solution()



print([-10, 1, 2, -2, -3])
print(s.maxProduct([-10, 1, 2, -2, -3]))
print([-10, 2])
print(s.maxProduct([-10, 1, 2, -2, -3]))

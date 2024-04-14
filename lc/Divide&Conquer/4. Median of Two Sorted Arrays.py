class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        # 当两个数组的长度和为奇数时，意味着我们要取这两个数组合并排序后的第 total//2 + 1 个数
        if total % 2 == 1:
            return self.findKthsmallnumber(nums1,nums2,total//2 + 1)
        else:
            # 当两个数组的长度和为偶数时，意味着我们要取这两个数组合并排序后的第(totall//2 + total//2+1 个数)/2
            # [1,2] [3,4] total=4, 我们要取2,3这两个数
            a = self.findKthsmallnumber(nums1,nums2,total//2)
            b = self.findKthsmallnumber(nums1,nums2,total//2 + 1)
            return (a+b)//2.0


    # 作用:在nums1和nums2所有元素中，找到第K大的元素
    def findKthsmallnumber(self,nums1,nums2,k):
        len1, len2 = len(nums1), len(nums2)
        # base1,base2表示的是数组的偏移量，排除的元素不包括base
        # base1/2左边的元素就表示已经被排除了, 后续计算不会再设计
        base1, base2 = 0, 0

        while True:
            # 当一个数组的len为0了，说明它里面的元素已经完全被排除掉了
            # 所以我们只用在另一个数组里返回第k大的元素就可以了
            if len1 == 0:
                return nums2[base2 + k - 1]
            if len2 == 0:
                return nums1[base1 + k - 1]

            # 已知base1, base2分别指向两个数组的最小元素
            # k=1就是在这两个元素之间找到第k大的元素
            if k == 1:
                return min(nums1[base1], nums2[base2])

            # i,j表示从各自的base出发，还要走几步到k/2
            # 取nums1的第k/2个数,那么nums2要取的数就是 k/2 - i,
            # 因为我们每个数组要刚好取出 k/2个数
            i = min(k//2, len1)
            j = min(k-i, len2)

            # 把各自数组中第k/2(half k -> hk)个数给取出来
            num1_hk = nums1[base1 + i - 1]
            num2_hk = nums2[base2 + j - 1]


            if i + j == k and num1_hk == num2_hk:
                return num1_hk

            """
                nums1[1/2k] < nums2[1/2k], 说明两数组合并后第K大的数一定在nums2
                k/2, 当k为偶数时，k/2 = 1/2k, 当k为奇数时，k/2 会向下取整 -> 1/2k - 1
                nums1[1/2k] < nums2[1/2k], 说明两数组合并后第K大的数一定在nums2
                所以nums1 0 ~ i的数都可排除掉，因为第k大的数不可能在里面
                因为我们每次都排除掉 1/2k个数，导致搜索规模越来越小，所以时间复杂度为 log(k)
            """
            if num1_hk <= num2_hk:
                #说明num1,的前k/2个数都是没用的，直接移动base1排除
                base1 += i
                len1 -= i
                k -= i

            if  num1_hk >= num2_hk:
                #说明num2,的前k/2个数都是没用的，直接移动base2排除
                base2 += j
                len2 -= j
                k -= j
            """
                这里涉及到一个问题，为什么num1_hk <= num2_hk, num1_hk >= num2_hk，这里可以等于
                因为当两数相等，且i + j 并没有到k, 例如len长度已经不够了，所以取len 而不是k-i,
                就说明在nums1[0..i],nums2[0..j]
                都不存在中位数，所以等于两个判断语句都执行了一遍
                把nums1[0..i],nums2[0..j]直接排除掉了
            """



"""
https://algocasts.io/episodes/Qqpn6pkK
// Time: O(log(k)) <= O(log(m+n)), Space: O(1)

和acwing做法相似，更好懂一点

主要目的是，要在不合并两个数组的前提下，找到在这两个数组中第k大的元素
具体的做法就是每次都排除掉不可能出现第K大元素的部分，
"""


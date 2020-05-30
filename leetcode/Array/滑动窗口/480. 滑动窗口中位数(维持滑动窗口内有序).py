class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if k == 0:
            return []

        ans = []

        # 这个滑动窗口一直都是一个排序数组
        # 呈现一个递增的排列顺序
        window = sorted(nums[0:k])

        # 为什么这里要遍历到 len(nums)+1, 因为是要把最后一个元素加进ans里去
        for i in range(k, len(nums) + 1):

            ans.append((window[k // 2] + window[(k - 1) // 2]) / 2.0)

            if i == len(nums):
                break

            # 找到nums[i-k]这个元素在滑动窗口内的位置(按照顺序来说)
            index = bisect.bisect_left(window, nums[i - k])

            # 从窗口里面删除最左边的元素，既是nums[i-k]
            window.pop(index)

            # 把当前的元素插入到滑动窗口里面
            bisect.insort_left(window, nums[i])

        return ans


"""
https://www.youtube.com/watch?v=kDS6ScZwNnI
本题有点滑动窗口的最大值的感觉， 但是我们这里维持的滑动窗口，是一个排序好的滑动窗口
所以除了 正常的添加元素和删除元素以外，我们还有维持窗口的有序性

"""
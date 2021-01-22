"""
该数组为[1 3 -1 -3 5 3 6 7]，k为3。

窗口位置	            最小值	最大值
[1 3 -1] -3 5 3 6 7	 -1	    3
1 [3 -1 -3] 5 3 6 7	 -3	    3
1 3 [-1 -3 5] 3 6 7	 -3	    5
1 3 -1 [-3 5 3] 6 7	 -3	    5
1 3 -1 -3 [5 3 6] 7	  3	    6
1 3 -1 -3 5 [3 6 7]	  3	    7

您的任务是确定滑动窗口位于每个位置时，窗口中的最大值和最小值。
"""

if __name__ == "__main__":

    n, k = map(int, input().split())
    # 记录滑动窗口内元素的下标
    queue = []
    nums = list(map(int, input().split()))
    resLower = []

    for i in range(n):
        # 首先把不在滑动窗口内的元素给删掉
        if len(queue) and queue[0] < i - k + 1:
            queue.pop(0)

        # 保持queue元素的单调性, 当前是递增
        while len(queue) and nums[queue[-1]] >= nums[i]:
            queue.pop()

        queue.append(i)
        # 然后把当前queue的最小值给放进resLower
        # 由于queue是从小到大递增，所以[0]的最小的
        if i >= k - 1:
            resLower.append(nums[queue[0]])

    queue = []
    resHigher = []
    for i in range(n):

        if len(queue) > 0 and queue[0] < i - k + 1:
            queue.pop(0)

        while len(queue) > 0 and nums[queue[-1]] <= nums[i]:
            queue.pop()

        queue.append(i)
        if i >= k - 1:
            resHigher.append(nums[queue[0]])

    print(" ".join(map(str, resLower)))
    print(" ".join(map(str, resHigher)))

# 使用单调队列来做，时间复杂度是O(n)
# https://www.acwing.com/video/65/
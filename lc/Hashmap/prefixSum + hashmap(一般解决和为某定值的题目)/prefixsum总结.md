# 哪些问题是和用前缀和写
我们可以对比一下209和325
209是一道典型的滑动窗口，因为它要求的值是大于等于某个值，所以我们可以利用while不断调整窗口
325是一道典型的前缀和问题，它要求的值是刚好等于某个值，假如说我们利用滑动窗口while调整窗口的做法
那么很容易一不满足while的条件，就退出循环，这样会错过大量的可能性，导致答案不精准


前缀和问题一般使用hashmap来做

key = 数组的前缀和
value = 当前数组的最后下标

例如[1,2,3,4,5]
要求一个和可被3mod的子串

我们可以把

(1,0)
(3,1)
(6,2)...

这样存进hashmap,
然后通过 前缀和的相减，来看值是否达到要求，

6 - 3 = 3 % 3 = 0

最后取出两个前缀和的下标，相减得到

2 - 1 = 1


# 古城算法总结
https://www.bilibili.com/video/BV1xB4y1N7Ut/?spm_id_from=333.999.0.0&vd_source=b81616a45fd239becaebfee25e0dbd35
prefix几大考点
- 2sum系列
- 区间和 range sum
- silding window
- 单调队列

## 2sum
题目求出了2个数字的和，diff = target - nums[i]
通过简单的变化我们可以同样做到求出2数只差等于target
diff =  nums[i] - target, 而两数只差的概念在prefix sum中就是subarray的sum。这里我们就过渡到了prefix sum

"""
Input: 00000000000000000000000000001011
Output: 3
"""

class Solution(object):
    # 比较快但是比较难记忆，忽略
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0

        count = 0
        while n != 0:
            count += 1
            n = n & (n-1)
        return count

    # 使用这个比较好
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0

        count = 0
        for i in range(32):
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count


"""
两种做法：
1.位运算
n & (n-1),因为n 和 n-1 的最后一位总是差1，等于把n的已有1的最后一个1给消掉，当1被消完的时候，n == 0
羡慕例子是n=11,需要三次来转化，但是每次&的时候，都会把非最后位置的1消除，感觉这个算法不太好控制
    1011     1010    1000
  & 1010    &1001   & 111
  --------  ------  -------
    1010     1000    0000

    
2.利用&1来判断最后一位是1还是0,是1，就意味着最后最后一位肯定是1，所以我们每次判断一下最后一位是不是1，
然后再把n >> 1,然后在判断下一位

方法1是要比方法2快的，因为方法1中的0已经被省略掉了，而方法2每一位都要遍历，虽然时间复杂度都是O(1)
"""
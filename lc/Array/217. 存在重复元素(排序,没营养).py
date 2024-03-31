def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    hm = {}
    for num in nums:
        if num in hm:
            return True
        else:
            hm[num] = 1

    return False

"""
把元素存哈希表里判断下有没有重复
"""

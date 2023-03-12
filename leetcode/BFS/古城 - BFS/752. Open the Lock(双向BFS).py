class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        begin = set()
        end = set()

        # 我们可以把deads当做是visited, 假如遍历到这个节点，那么就不继续遍历下去了
        # 这样直到所有的点都走完，都还没到终点的话，说明没办法到达
        deads = set(deadends)

        # 起点从 0000 开始
        begin.add("0000")
        # 终点是target
        end.add(target)

        level = 0
        while len(begin) > 0 and len(end) > 0:
            next = set()
            for s in begin:
                if s in end:
                    return level
                if s in deads:
                    continue

                # 记录走过的点
                deads.add(s)
                for i in range(4):
                    char = s[i]
                    # 一个向前拨，一个向后拨
                    s1 = s[:i] + ("0" if char == "9" else chr(ord(char) + 1)) + s[i + 1:]
                    s2 = s[:i] + ("9" if char == "0" else chr(ord(char) - 1)) + s[i + 1:]

                    if s1 not in deads:
                        next.add(s1)
                    if s2 not in deads:
                        next.add(s2)
            level += 1
            # 这里我们把begin 和 end轮流进行BFS就好了，因为每次next都只有两个元素，所以不用分先后
            begin = end
            end = next

        return -1

"""
古城算法 ppt
https://docs.google.com/presentation/d/1R8rHF7l3C5DEOI0GTwSwSzkmyRmscu1KwjVIVpL4tgQ/edit#slide=id.gcabbc9c948_0_0
双向BFS
"""
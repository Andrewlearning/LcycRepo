"""
输入: [[1],[2],[3],[]]
输出: true
解释:
我们从 0 号房间开始，拿到钥匙 1。
之后我们去 1 号房间，拿到钥匙 2。
然后我们去 2 号房间，拿到钥匙 3。
最后我们去了 3 号房间。
由于我们能够进入每个房间，我们返回 true。

示例 2：
输入：[[1,3],[3,0,1],[2],[0]]
输出：false
解释：我们不能进入 2 号房间。
"""

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited, queue = {0}, [0]
        while queue:
            room_index = queue.pop(-1)
            for key in rooms[room_index]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)

        return len(visited) == len(rooms)

"""
没啥好说的，就是进到一个房间， 然后把能去的房间都加进 visited, 和queue里
一直这样走就能去完所有的房间， 如果走不完就return false
https://leetcode-cn.com/problems/keys-and-rooms/solution/7xing-dfs-8xing-bfs-liang-chong-fang-fa-san-chong-/
"""


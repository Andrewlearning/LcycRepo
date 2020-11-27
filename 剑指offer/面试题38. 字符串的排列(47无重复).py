class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []

        self.lens = len(s)
        self.visited = [False] * self.lens
        self.res = []
        # 关键点，先排序好
        self.helper(sorted(s), "")

        return self.res

    def helper(self, s, path):
        if len(path) > self.lens:
            return

        if len(path) == self.lens:
            self.res.append(path[:])

        for i in range(self.lens):
            if self.visited[i] == True:
                continue
            # 关键点，出现重复节点且已被访问过
            if i > 0 and s[i] == s[i - 1] and self.visited[i - 1]:
                continue

            self.visited[i] = True
            pre = path
            path += s[i]

            self.helper(s, path)

            path = pre
            self.visited[i] = False



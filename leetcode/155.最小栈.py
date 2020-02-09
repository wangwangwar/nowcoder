#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min is None or self.min > x:
            self.min = x

    def pop(self) -> None:
        x = self.stack.pop()
        if self.min == x:
            self._updateMin()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

    def _updateMin(self) -> None:
        self.min = None
        for e in self.stack:
            if self.min == None or self.min > e:
                self.min = e

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# @lc code=end

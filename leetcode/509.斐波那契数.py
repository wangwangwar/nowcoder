#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#
# 思路
# 1. 递归
# 2. 动态规划，记录中间值

# @lc code=start


class Solution:
    def fib(self, n: int) -> int:
        return self.fibMemTopDown(n)

    def fibRec(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def __init__(self):
        self.mem = {0: 0, 1: 1}

    def fibMemTopDown(self, n: int) -> int:
        val = self.mem.get(n)
        if val is None:
            res_n1 = self.fib(n - 1)
            self.mem[n-1] = res_n1
            res_n2 = self.fib(n - 2)
            self.mem[n-2] = res_n2
            return res_n1 + res_n2
        else:
            return val

    def fibMemBottomUp(self, n: int) -> int:
        i = 2
        while i <= n:
            res_i1 = self.mem.get(i - 1)
            res_i2 = self.mem.get(i - 2)
            self.mem[i] = res_i1 + res_i2
            i += 1
        return self.mem[n]

# @lc code=end

#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
# 题解
# 不断重复构造数，使用hash表记录出现过的数，如果有循环判为false。直到归为1

# @lc code=start


class Solution:
    def __init__(self):
        self.dict = dict()

    def isHappy(self, n: int) -> bool:
        if self.dict.get(n) is not None:
            return False
        else:
            self.dict[n] = True
        n_str = str(n)
        sum = 0
        for c in n_str:
            n = int(c)
            sum += n * n
        if sum == 1:
            return True
        else:
            return self.isHappy(sum)
# @lc code=end

#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# 思路
# 1. 递归，贪心

# @lc code=start


class Solution:
    def __init__(self):
        self.digitCharDict = dict([("2", "abc"), ("3", "def"), ("4", "ghi"), (
            "5", "jkl"), ("6", "mno"), ("7", "pqrs"), ("8", "tuv"), ("9", "wxyz")])

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        l = []
        for c in self.digitCharDict[digits[0]]:
            rest = self.letterCombinations(digits[1:])
            if len(rest) == 0:
                l.append(c)
            else:
                l.extend(list(map(lambda s: c + s, rest)))

        return l

# @lc code=end

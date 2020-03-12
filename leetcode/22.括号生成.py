#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# 题解
# backtracking，注意：1. 排除无效的情况。2. 终止条件是什么？

# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self._gen("", n, n)

    def _gen(self, result: str, left: int, right: int) -> List[str]:
        # invalid
        if left > 0 and right == 0:
            return []

        # 终止条件
        if left == 0 and right == 0:
            return [result]

        list = []
        # )
        if right > left:
            list.extend(self._gen(result + ")", left, right - 1))

        # (
        if left > 0:
            list.extend(self._gen(result + "(", left - 1, right))

        return list


# @lc code=end

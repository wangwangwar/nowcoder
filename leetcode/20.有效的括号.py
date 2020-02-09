#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# 题解
# 用栈，左括号入栈，遇到匹配的右括号把左括号出栈。如果没有匹配的左括号，非法。如果最后栈中还剩左括号，非法。

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')' and len(stack) > 0 and stack.pop() == '(':
                continue
            elif c == '}' and len(stack) > 0 and stack.pop() == '{':
                continue
            elif c == ']' and len(stack) > 0 and stack.pop() == '[':
                continue
            else:
                return False
        return len(stack) == 0


# @lc code=end

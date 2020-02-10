#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#
# 思路
# 快慢指针？快指针一次走两个，慢指针一次走一个。会错过吗？画示意图发现在一次循环内一定会相遇
# `
# 17/17 cases passed (48 ms)
# Your runtime beats 90.54 % of python3 submissions
# Your memory usage beats 55.05 % of python3 submissions (16.2 MB)
# `

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        slow_p = head
        fast_p = head.next
        while slow_p != fast_p:
            if fast_p.next is None or fast_p.next.next is None:
                return False
            fast_p = fast_p.next.next
            slow_p = slow_p.next
        return True


# @lc code=end

#
# @lc app=leetcode.cn id=382 lang=python3
#
# [382] 链表随机节点

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 蓄水池抽样算法 (Reservoir Sampling)
#   先初始化一个集合，集合中有k个元素，将此集合作为蓄水池。然后从第k+1个元素开始遍历，并且按一定的概率替换掉蓄水池里面的元素。
# TAOCP sample code
#   Init : a reservoir with the size： k
#   for i= k+1 to N
#       M=random(1, i);
#       if( M < k)
#        SWAP the Mth value and ith value
#   end for

import random


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    SAMPLE_SIZE = 100000

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self._list = []
        cur = head
        i = 0
        while cur != None:
            if i < self.SAMPLE_SIZE:
                self._list.append(cur.val)
            else:
                m = random.randrange(i)
                if m < self.SAMPLE_SIZE:
                    self._list[m] = cur.val
            cur = cur.next
            i += 1

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return random.choice(self._list)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

if __name__ == "__main__":
    import collections

    head = ListNode(1)
    cur = head
    for _ in range(1000000):
        cur.next = ListNode(random.randrange(100))
        cur = cur.next
    for _ in range(100000):
        cur.next = ListNode(1)
        cur = cur.next
    solution = Solution(head)
    dic = collections.defaultdict(int)
    for i in range(100000):
        ret_num = solution.getRandom()
        dic[ret_num] += 1

    for k, v in dic.items():
        print(k, ":", v)

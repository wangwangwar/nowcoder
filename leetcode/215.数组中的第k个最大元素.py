#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# 思路
# 1. 使用最大堆。时间复杂度：O(n * lgn)，空间复杂度：O(n)
# `
# 32/32 cases passed (120 ms)
# Your runtime beats 37.55 % of python3 submissions
# Your memory usage beats 54.13 % of python3 submissions (13.7 MB)
# `
# 1.1. heapq
# `
# 32/32 cases passed (76 ms)
# Your runtime beats 71.64 % of python3 submissions
# Your memory usage beats 49.36 % of python3 submissions (14 MB)
# `
#
# 2. 排序
# 3. 快速选择

# @lc code=start
from queue import PriorityQueue
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findKthLargest1_1(nums, k)

    def findKthLargest1(self, nums: List[int], k: int) -> int:
        queue = PriorityQueue(k)
        for n in nums:
            if not queue.full():
                queue.put(n)
            else:
                min_k = queue.queue[0]
                if n > min_k:
                    queue.get()
                    queue.put(n)
        return queue.queue[0]

    def findKthLargest1_1(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

# @lc code=end

#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第K大元素
#

# @lc code=start
from queue import PriorityQueue
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = PriorityQueue(k)
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if not self.queue.full():
            self.queue.put(val)
        else:
            min_k = self.queue.queue[0]
            if val > min_k:
                self.queue.get()
                self.queue.put(val)

        return self.queue.queue[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end


if __name__ == '__main__':
    obj = KthLargest(3, [4, 5, 8, 2])
    print(obj.add(3))
    print(obj.add(5))
    print(obj.add(10))
    print(obj.add(9))
    print(obj.add(4))

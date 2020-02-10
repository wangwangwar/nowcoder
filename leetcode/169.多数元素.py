#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# 思路
# 1. 朴素办法：用 dict 记录每个元素出现的次数，当次数超过⌊ n/2 ⌋时，即为多数元素。时间复杂度：，
# `
# 44/44 cases passed (216 ms)
# Your runtime beats 43.83 % of python3 submissions
# Your memory usage beats 48.89 % of python3 submissions (14.5 MB)
# `
# 2. 从第一个数开始count=1，遇到相同的就加1，遇到不同的就减1，减到0就重新换个数开始计数，总能找到最多的那个
# `
# 44/44 cases passed (192 ms)
# Your runtime beats 80.49 % of python3 submissions
# Your memory usage beats 48.76 % of python3 submissions (14.5 MB)
# `
from typing import List


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.majorityElement2(nums)

    def majorityElement1(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            if d.get(num) is None:
                d[num] = 1
            else:
                d[num] += 1
            if d[num] > len(nums) / 2:
                return num

    def majorityElement2(self, nums: List[int]) -> int:
        maj = nums[0]
        count = 1
        i = 1
        while i < len(nums):
            if nums[i] == maj:
                count += 1
            else:
                count -= 1
                if count == 0:
                    maj = nums[i + 1]
            i += 1
        return maj
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    s.majorityElement([6, 5, 5])

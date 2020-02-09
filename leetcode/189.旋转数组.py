#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
# 题解
# 1. 从数组尾部开始，反复交换相邻元素，向头部推进，直到头部。循环k次。时间复杂度太高 O(kn)
# 2. 旋转！

# @lc code=start


class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        real_k = k % len(nums)
        while i < real_k:
            j = len(nums) - 1
            while j > 0:
                jj = j - 1
                nums[j], nums[jj] = nums[jj], nums[j]
                j -= 1
            i += 1

    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        reverse_sublist(nums, 0, l - k)
        reverse_sublist(nums, l - k, l)
        nums.reverse()


def reverse_sublist(lst, start, end):
    lst[start:end] = lst[start:end][::-1]
    return lst


# @lc code=end

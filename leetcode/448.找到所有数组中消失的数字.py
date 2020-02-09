#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#
# 题解
# 1. 遍历数组，把（元素值绝对值-1）作下标找到下标所在元素置为相反数。 再次遍历数组，所有正数的下标+1即为消失的数字。时间复杂度 O(n)，空间复杂度 O(1)
# 2. 使用字典（hash表）来记录出现过的数字。时间复杂度 O(n)，空间复杂度 O(n)
#
# @lc code=start


class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        return [i + 1 for i, num in enumerate(nums) if num > 0]
# @lc code=end


if __name__ == '__main__':
    solution = Solution()
    print(solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))

#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# 思路：
# 1. 使用另外一个空数组做容器，然后copy回nums1数组，时间复杂度：O(m + n),空间复杂度:O(m + n)
# 2. nums1做容器，原地合并，从nums1尾部开始向前填充数据。时间复杂度：O(m + n),空间复杂度:O(1)

# @lc code=start


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        self.merge2(nums1, m, nums2, n)

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m -= 1
        n -= 1
        i = m + n + 1
        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmpNums = nums1[:]
        i, j = 0, 0
        while i < m or j < n:
            if j == n:
                tmpNums[i + n] = nums1[i]
                i += 1
            elif i == m:
                tmpNums[j + m] = nums2[j]
                j += 1
            elif nums1[i] < nums2[j]:
                tmpNums[i + j] = nums1[i]
                i += 1
            else:
                tmpNums[i + j] = nums2[j]
                j += 1

        z = 0
        while z < m + n:
            nums1[z] = tmpNums[z]
            z += 1


# @lc code=end

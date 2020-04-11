#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#
# 时间复杂度：O(n)一趟扫描
# 空间复杂度：O(n)

# @lc code=start


class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]

        l = [0, 1]
        latest_key_num = 1

        for i in range(2, num + 1):
            remainder = i % latest_key_num
            if remainder == 0:
                l.append(1)
                latest_key_num = i
            else:
                l.append(1 + l[remainder])

        return l
# @lc code=end

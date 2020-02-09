#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
# 题解
# 从左到右扫描字符串，不光观察当前字符，还要观察下一个字符。当字符是 I，而下一个字符是 V 或 X 时，两个字符组成 IV 或 IX，对 X 和 C 同理。
#
# 提交结果
# 3999/3999 cases passed (52 ms)
# Your runtime beats 75.72 % of python3 submissions
# Your memory usage beats 57.36 % of python3 submissions (13.2 MB)

# @lc code=start


class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        sum = 0
        while i < len(s) - 1:
            cur, next = s[i], s[i + 1]
            if cur == 'I':
                if next == 'V':
                    sum += 4
                    i += 2
                elif next == 'X':
                    sum += 9
                    i += 2
                else:
                    sum += 1
                    i += 1
            elif cur == 'X':
                if next == 'L':
                    sum += 40
                    i += 2
                elif next == 'C':
                    sum += 90
                    i += 2
                else:
                    sum += 10
                    i += 1
            elif cur == 'C':
                if next == 'D':
                    sum += 400
                    i += 2
                elif next == 'M':
                    sum += 900
                    i += 2
                else:
                    sum += 100
                    i += 1
            else:
                sum += self._trans(cur)
                i += 1

        if i < len(s):
            sum += self._trans(s[i])

        return sum

    def _trans(self, s: str) -> int:
        if s == 'I':
            return 1
        elif s == 'V':
            return 5
        elif s == 'X':
            return 10
        elif s == 'L':
            return 50
        elif s == 'C':
            return 100
        elif s == 'D':
            return 500
        elif s == 'M':
            return 1000
        raise Exception
# @lc code=end


if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt('IV'))

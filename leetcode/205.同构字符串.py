#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
# 思路
# 1. 首先比较 s 和 t 长度，如果不同，非同构。如果相同，使用字典，同步遍历s和t。s中元素如果未在字典中出现过且t中对对应下标元素也未作为value，那么以s元素作为key，t中对应下标元素作为value记录一条;如果出现过，使用对应的value和t中对应下标元素比较，如果不相同，非同构。直到遍历完成。

# @lc code=start


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self._inner(s, t)

    def _inner(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = dict()
        i = 0
        while i < len(s):
            val = d.get(s[i])
            if val is None:
                if contain_value(d, t[i]):
                    return False
                else:
                    d[s[i]] = t[i]
            elif val != t[i]:
                return False
            i += 1
        return True


def contain_value(d: dict, val: str) -> bool:
    for e in d.values():
        if e == val:
            return True
    return False

# @lc code=end

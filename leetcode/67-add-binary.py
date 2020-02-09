# 二进制求和
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 输入为非空字符串且只包含数字 1 和 0。
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
from typing import Callable


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = add(a, b).lstrip('0')
        if ans == '':
            return '0'
        else:
            return ans


def add(a: str, b: str) -> str:
    xorRes = xorFunc(a, b)
    carry = andFunc(a, b)
    leftShiftCarry = leftShift(carry, 1)
    if allZero(xorRes):
        return leftShiftCarry
    elif allZero(leftShiftCarry):
        return xorRes
    else:
        return add(xorRes, leftShiftCarry)


def allZero(s: str) -> bool:
    for c in s:
        if c != '0':
            return False
    return True


def binStrFunc(a: str, b: str, op: Callable[[str, str], str]) -> str:
    if len(a) > len(b):
        b = b.zfill(len(a))
    elif len(a) < len(b):
        a = a.zfill(len(b))

    result = ''
    i = 0
    while i < len(a):
        result += op(a[i], b[i])
        i += 1
    return result


def andOp(a: str, b: str) -> str:
    if a == '1' and b == '1':
        return '1'
    else:
        return '0'


def xorOp(a: str, b: str) -> str:
    if a == '1' and b == '0' or a == '0' and b == '1':
        return '1'
    else:
        return '0'


def andFunc(a: str, b: str) -> str:
    return binStrFunc(a, b, andOp)


def xorFunc(a: str, b: str) -> str:
    return binStrFunc(a, b, xorOp)


def leftShift(s: str, bits: int) -> str:
    return s + '0' * bits


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary('11', '1'))

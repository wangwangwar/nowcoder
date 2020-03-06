# 在字符串中找出连续最长的数字串
def solution(s: str) -> str:
    tmpStr = ""
    maxStrList = [tmpStr]
    maxStrLen = 0
    for _, c in enumerate(s):
        if c.isnumeric():
            tmpStr += c
            if len(tmpStr) > maxStrLen:
                maxStrList = [tmpStr]
                maxStrLen = len(tmpStr)
            elif len(tmpStr) == maxStrLen:
                maxStrList.append(tmpStr)
        else:
            tmpStr = ""
    string = "".join(maxStrList) + "," + str(maxStrLen)
    return string

if __name__ == '__main__':
    while True:
        try:
            s = input()
            result = solution(s)
            print(result)
        except:
            break
        

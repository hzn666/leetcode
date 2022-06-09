import collections


def minWindow(s: str, t: str) -> str:
    # 计数器
    need = collections.Counter(t)
    # 需要的字符数
    needCnt = len(t)

    i = 0
    # 记录最小子串的区间
    res = (0, float('inf'))
    for j, c in enumerate(s):
        # 如果现在s中的c是我们要找的t中的字符，则需要的字符数-1
        if need[c] > 0:
            needCnt -= 1
        # 更新计数器，计数器为负代表有多余字符
        need[c] -= 1
        # 如果当前的子串中已经包含t中所有字符
        if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
            # 这时不急着统计子串的长度，因为左边可能还有多余字符
            while True:  # 步骤二：增加i，排除多余元素
                # 遍历左边的字符
                c = s[i]
                # 如果这个字符没有多余，就不收缩左边界了
                if need[c] == 0:
                    break
                need[c] += 1
                i += 1
            # 这时应该记录结果了，如果找到的子串区间小于之前找到的，则更新结果
            if j - i < res[1] - res[0]:  # 记录结果
                res = (i, j)

            # 在左边界固定的前提下，我们已经找到了一个极小子串，现在需要人为收缩左边界，重复上述操作
            # 收缩前的左边界一定是t中的某个字符
            # 所以收缩后，need和needCnt都需要更新
            need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
            needCnt += 1
            i += 1
    return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))

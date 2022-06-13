import collections


def minWindow(s: str, t: str) -> str:
    # 计数器，需要凑齐的字符
    need = collections.Counter(t)
    # 计数器，记录滑动窗口中的字符
    window = collections.defaultdict(int)

    # 左右指针
    left = 0
    right = 0
    # 有效值，窗口中满足need条件的字符个数
    valid = 0
    # 起始索引
    start = 0
    # 长度
    length = float("inf")

    # 遍历s
    while right < len(s):
        # 取字符
        c = s[right]
        # 右移窗口
        right += 1

        # 进行窗口内数据的一系列更新
        if need[c] > 0:
            window[c] += 1
            if need[c] == window[c]:
                valid += 1

        # 判断左侧窗口是否需要收缩
        while valid == len(need):
            # 更新最小覆盖子串
            if (right - left) < length:
                start = left
                length = right - left
            # pop_c是移出窗口的字符
            pop_c = s[left]
            # 左移窗口
            left += 1

            # 进行窗口内数据的一系列更新
            if need[pop_c] > 0:
                if window[pop_c] == need[pop_c]:
                    valid -= 1
                window[pop_c] -= 1
    # 返回最小覆盖子串
    return '' if length == float("inf") else s[start:start + length]


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))

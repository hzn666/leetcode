import collections


def maxSlidingWindow(nums, k):
    # 数组长度
    n = len(nums)
    # 队列，队头存储最大值
    q = collections.deque()

    # 先将[0,k)个元素送进队列
    for i in range(k):
        # 存储候选最大值
        # 如果队列不为空，且当前元素比队尾元素大，则将队尾元素弹出
        while q and nums[i] > q[-1]:
            q.pop()
        q.append(nums[i])

    # 第一个窗口的k个元素已经送进队列
    # 这个时候队头是最大值
    ans = [q[0]]

    # 继续添加[k,n)的元素到队列中
    # 窗口滑动
    for i in range(k, n):
        # nums[i - k]是当前要退出窗口的元素
        # 如果当前元素是最大值，则队头也要弹出
        if q and nums[i - k] == q[0]:
            q.popleft()
        # 存储候选最大值
        # 如果队列不为空，且当前元素比队尾元素大，则将队尾元素弹出
        while q and nums[i] > q[-1]:
            q.pop()
        q.append(nums[i])
        # 每次滑动一次窗口，就append一次当前窗口的最大值，即队列头
        ans.append(q[0])

    return ans


nums = [-7, -8, 7, 5, 7, 1, 6, 0]
k = 4
print(maxSlidingWindow(nums, k))

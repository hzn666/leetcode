import collections


class MaxQueue:

    def __init__(self):
        self.q = collections.deque()
        self.max = collections.deque()

    def max_value(self) -> int:
        return self.max[0] if self.q else -1

    def push_back(self, value: int) -> None:
        self.q.append(value)
        while self.max and self.max[-1] < value:
            self.max.pop()
        self.max.append(value)

    def pop_front(self) -> int:
        if not self.q:
            return -1
        a = self.q.popleft()
        if a == self.max[0]:
            self.max.popleft()
        return a

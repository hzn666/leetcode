class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.:
            return x
        if n < 0:
            x = 1 / x
            n = -n
        res = 1

        while n:
            if n % 2:
                res *= x
            x *= x
            n = n // 2
        return res

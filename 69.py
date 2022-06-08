def mySqrt(x: int) -> int:
    left, right = 0, x

    while left <= right:
        mid = left + (right - left) // 2

        pf = mid * mid

        if pf <= x:
            left = mid + 1
        elif pf > x:
            right = mid - 1

    return right


print(mySqrt(0))

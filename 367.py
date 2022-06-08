def isPerfectSquare(num: int) -> bool:
    left, right = 0, num

    while left <= right:

        mid = left + (right - left) // 2

        if mid * mid <= num:
            left = mid + 1
        else:
            right = mid - 1

    if right * right == num:
        return True
    else:
        return False


print(isPerfectSquare(4))

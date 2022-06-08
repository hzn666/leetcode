from typing import List

def isBoomerang(points: List[List[int]]) -> bool:
    a = points[0]
    b = points[1]
    c = points[2]

    if a == b or a == c or b == c:
        return False

    result = (b[1] - a[1]) * (c[0] - b[0]) == (b[0] - a[0]) * (c[1] - b[1])

    if result:
        return False
    else:
        return True
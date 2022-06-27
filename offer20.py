def isNumber(s: str) -> bool:
    res = True
    try:
        num = float(s)
    except:
        res = False
    return res
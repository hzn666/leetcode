def removeDuplicates(s: str) -> str:
    stack = []

    for i in range(len(s)):
        c = s[i]
        if not stack:
            stack.append(c)
        elif c == stack[-1]:
            stack.pop()
        elif c != stack[-1]:
            stack.append(c)

    return "".join(stack)

s = "abbaca"
removeDuplicates(s)

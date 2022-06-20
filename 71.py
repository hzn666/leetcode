def simplifyPath(path: str) -> str:
    path = path.split("/")
    stack = []

    for name in path:
        if name == "..":
            if stack:
                stack.pop()
        elif name and name != ".":
            stack.append(name)

    return "/" + "/".join(stack)


path = "/home/"
print(simplifyPath(path))

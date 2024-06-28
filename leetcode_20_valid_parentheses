
def isValid(s: str) -> bool:

    stack = []
    hash_map = {")": "(", "]": "[", "}": "{"}

       # if s is None:
       #     return True

    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in hash_map.keys():
            if not stack:
                return False
            if hash_map[char] != stack.pop():
                return False

    return not stack

print(isValid("()[]{}"))

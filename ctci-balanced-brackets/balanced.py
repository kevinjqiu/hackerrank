MATCHING_PAIRS = {
    '}': '{',
    ']': '[',
    ')': '(',
}


def is_matched(expression):
    stack = []

    for ch in expression:
        if ch in MATCHING_PAIRS.values():
            stack.append(ch)
            continue

        if len(stack) == 0:
            return False

        if stack[-1] == MATCHING_PAIRS[ch]:
            stack.pop()
        else:
            stack.append(ch)

    return len(stack) == 0


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

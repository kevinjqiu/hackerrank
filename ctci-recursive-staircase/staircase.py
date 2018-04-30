memoized = {}


def ways(n):
    if n in memoized:
        return memoized[n]

    if n == 0:
        memoized[n] = 0
        return 0
    if n == 1:
        memoized[n] = 1
        return 1
    if n == 2:
        memoized[n] = 2
        return 2
    if n == 3:
        memoized[n] = 4
        return 4

    result = ways(n-1) + ways(n-2) + ways(n-3)
    memoized[n] = result
    return result


s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(ways(n))

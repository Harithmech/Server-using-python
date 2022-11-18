s = "mississippi"
p = "m??*ss*?i*pi"

n, m = len(s), len(p)
count = 0

if p[0] != "*":
    count = 0
else:
    for a in p:
        if a != "*":
            break
        count += 1

ans = [[-1 for a in range(m)] for b in range(n)]


def func(i, j):
    if i == -1:
        if j <= count:
            return 1
        else:
            return 0
    if j == -1:
        return 0
    if ans[i][j] != -1:
        return ans[i][j]
    if p[j] == "?":
        ans[i][j] = func(i-1, j-1)
    elif p[j] == "*":
        ans[i][j] = func(i, j-1) or func(i-1, j)
    elif s[i] == p[j]:
        ans[i][j] = func(i-1, j-1)
    return True if ans[i][j] == 1 else False


print(ans)
print(func(n-1, m-1))

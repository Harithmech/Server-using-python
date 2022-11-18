s = "coollab"
p = "collab"

n, m = len(s), len(p)
ans = [[-1 for i in range(m)] for j in range(n)]


def func(i, j):
    if j == -1:
        return 1
    if i == -1:
        return 0
    if ans[i][j] != -1:
        return ans[i][j]
    if s[i] != p[j]:
        ans[i][j] = func(i-1, j)
    else:
        ans[i][j] = func(i-1, j-1) + func(i-1, j)
    return ans[i][j]


print(func(n-1, m-1))

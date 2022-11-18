s1 = "abcde"
s2 = "ace"

n, m = len(s1), len(s2)

# memoization
ans = [[-1 for i in range(m)] for j in range(n)]


def LCS(i, j):
    if i < 0 or j < 0:
        return 0
    if ans[i][j] != -1:
        return ans[i][j]
    if s1[i] == s2[j]:
        ans[i][j] = 1 + LCS(i-1, j-1)
    else:
        ans[i][j] = max(LCS(i-1, j), LCS(i, j-1))
    return ans[i][j]


print(LCS(n-1, m-1))

s1 = "abcde"
s2 = "ace"

n, m = len(s1), len(s2)

# memoization
ans = [["" for i in range(m)] for j in range(n)]


def LCS(i, j):
    if i < 0 or j < 0:
        return ""
    if ans[i][j] != "":
        return ans[i][j]
    if s1[i] == s2[j]:
        ans[i][j] = s1[i] + LCS(i-1, j-1)
    else:
        if len(ans[i-1][j]) > len(ans[i][j-1]):
            ans[i][j] = LCS(i-1, j)
        else:
            ans[i][j] = LCS(i, j-1)
    return ans[i][j]



print(LCS(n-1, m-1))

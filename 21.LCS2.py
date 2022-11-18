s1 = "appa"
s2 = "amma"

n, m = len(s1), len(s2)

ans = [[-1 for i in range(m+1)] for j in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if s1[i-1] == s2[j-1]:
            ans[i][j] = 1 + ans[i-1][j-1]
        else:
            ans[i][j] = max(ans[i-1][j], ans[i][j-1])

print(ans[n][m])


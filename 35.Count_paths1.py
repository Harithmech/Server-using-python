m, n = 3, 2

ans = [[-1 for i in range(n)] for j in range(m)]


def func(i, j):
    if i == m-1 or j == n-1:
        return 1
    if ans[i][j] != -1:
        return ans[i][j]
    else:
        ans[i][j] = func(i+1, j) + func(i, j+1)
    return ans[i][j]


print(func(0, 0))


# Bottom-top

# m, n = 3, 2
# ans = [[0 for i in range(n)] for j in range(m)]

# for i in range(m):
#     ans[i][0] = 1

# for i in range(n):
#     ans[0][i] = 1

# for i in range(1, m):
#     for j in range(1, n):
#         ans[i][j] = ans[i-1][j] + ans[i][j-1]

# print(ans[m-1][n-1])

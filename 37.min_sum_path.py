import math
grid = [[1, 2, 3], [4, 5, 6]]
n, m = len(grid), len(grid[0])
ans = [[-1 for i in range(m)] for j in range(n)]


def func(i, j):

    if i < 0 or j < 0:
        return math.inf
    if ans[i][j] != -1:
        return ans[i][j]
    elif i == 0 and j == 0:
        ans[i][j] = grid[i][j]
    else:
        ans[i][j] = grid[i][j] + min(func(i-1, j), func(i, j-1))
    return ans[i][j]


print(func(n-1, m-1))

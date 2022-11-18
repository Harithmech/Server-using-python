obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
n, m = len(obstacleGrid), len(obstacleGrid[0])
ans = [[-1 for i in range(m)] for j in range(n)]


def func(i, j):
    if obstacleGrid[i][j] == 1:
        return 0
    if i == 0 and j == 0:
        return 1
    if ans[i][j] != -1:
        return ans[i][j]
    ans[i][j] = 0
    if j > 0:
        ans[i][j] += func(i, j-1)
    if i > 0:
        ans[i][j] += func(i-1, j)
    return ans[i][j]


print(func(n-1, m-1))

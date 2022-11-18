arr = [[4, 100, 200, 0], [70, 50, 4, 2]]
N = 2
M = len(arr[0])
ans = [-1 for i in range(M+1)]


def maxSum(i):
    if i >= M:
        return 0
    if ans[i] != -1:
        return ans[i]
    # ans[i] = max(arr[0][i]+maxSum(i+2), arr[1][i]+maxSum(i+2), maxSum(i+1))
    # In order to reduce the number of function calls
    # irrespective of choosing the element from first or second row we never choose elements from column 2
    ans[i] = max(max(arr[0][i], arr[1])+maxSum(i+2), maxSum(i+1))
    return ans[i]


print(maxSum(0))

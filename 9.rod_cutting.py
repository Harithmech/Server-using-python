prices = [2, 5, 9, 9, 10, 10, 11]
N = len(prices)
ans = [-1 for i in range(N+1)]


def maxVal(i):
    global ans
    if i == 0:
        return 0
    if ans[i] != -1:
        return ans[i]
    for j in range(1, i+1):
        ans[i] = max(ans[i], prices[j-i]+maxVal(i-j))
    return ans[i]


print(maxVal(N))

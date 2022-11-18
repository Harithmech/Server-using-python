# Longest increasing subsequence

# Brute-force approach
# exponential time complexity
arr = [10, 0, 5, 3, 7, 9, 2]
N = len(arr)
ans1 = 0
for i in range(N):
    ans = 0
    temp = arr[i]
    for j in range(i, N):
        if temp <= arr[j]:
            temp = arr[j]
            ans += 1
    ans1 = max(ans1, ans)

print(ans1)

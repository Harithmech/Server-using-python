# Brute force approach
# arr = [1, 10, 100, 40, 20]
# N = len(arr)
# ans = 0
# for i in range(0, N):
#     for j in range(0, N):
#         if i == j or j == i-1 or j == i+1:
#             continue
#         ans = max(ans, arr[i]+arr[j])
# print(ans)


# Top down approach
# arr = [1, 10, 100, 40, 20]
# N = len(arr)
# ans = [-1 for i in range(N+1)]
# def maxSum(i):
#     if i >= N:
#         return 0
#     if ans[i] != -1:
#         return ans[i]
#     ans[i] = max(arr[i]+maxSum(i+2), maxSum(i+1))
#     return ans[i]
# print(maxSum(0))


# Bottom-up approach 
arr = [1, 10, 100, 40, 20]
N = len(arr)
ans = [-1 for i in range(N+1)]


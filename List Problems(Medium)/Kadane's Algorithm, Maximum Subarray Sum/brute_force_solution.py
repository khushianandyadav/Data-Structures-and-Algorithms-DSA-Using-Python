nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

n = len(nums)
maxi = float("-inf")
for i in range(0, n):
    total = 0
    for j in range(i, n):
        total = total + nums[j]
        maxi = max(maxi, total)
print(maxi)

'''
TC -> O(N(N+1)/2) similar to O(N**2)
SC -> O(1)
'''

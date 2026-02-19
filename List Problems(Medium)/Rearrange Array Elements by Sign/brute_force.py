#LeetCode 2149

nums = [5, 10, -3, -1, -10, 6]

pos = [x for x in nums if x >= 0]
neg = [y for y in nums if y < 0]

for i in range (0, len(pos)):
    nums[2*i] = pos[i]
    nums[(2*i)+1] = neg[i]

print(nums)

#TC -> O(N + N/2)
#SC -> O(N/2 + N/2) -> O(N)

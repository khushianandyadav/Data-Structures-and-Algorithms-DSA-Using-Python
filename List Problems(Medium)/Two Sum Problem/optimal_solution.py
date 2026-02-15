# dictionary searches in time O(1)


nums = [5, 9, 1, 2, 4, 15, 6, 3]
target = 24

n = len(nums)
hash_map = {}
for i in range(0, n):
    remaining = target - nums[i]
    if remaining in hash_map:
        print([hash_map[remaining], i])
    hash_map[nums[i]] = i
    

# TC -> O(N)
# SC -> O(N)
nums = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]
x = 1
hash_map = {}
n = len(nums)
for i in range(0, n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
print(hash_map[1])


# TC -> O(1) avg case and v v rare worst case O(N)
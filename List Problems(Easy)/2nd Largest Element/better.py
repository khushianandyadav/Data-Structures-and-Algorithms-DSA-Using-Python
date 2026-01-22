nums = [55, 23, 97, -55, 45, 32, 88, 21, 100]

largest = float("-inf")
s_largest = float("-inf")
n = len(nums)
for i in range(0, n):
    largest = max(nums[i], largest)

for i in range(0, n):
    if nums[i] > s_largest and nums[i] != largest:
        s_largest = nums[i]

print(s_largest)

'''
TC = O(N + N) -> O(2N) similar to O(N)
SC -> O(1)

Optimal Solution will have TC O(N)
'''
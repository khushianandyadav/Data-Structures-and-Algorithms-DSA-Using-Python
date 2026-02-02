nums = [3, 4, 1, 7, 9, 7, 11, 45, 5]
k = 10
n = len(nums)
k = k%n
def reverse(nums, left, right):
    while left<right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

reverse(nums, n-k, n-1)
reverse(nums, 0, n-k-1)
reverse(nums, 0, n-1)

print(nums)
'''
TC -> O(n)
SC -> O(1)
'''
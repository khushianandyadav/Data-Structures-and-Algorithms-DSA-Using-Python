nums = [1, 5, 6, 3, 90, 4, 2, 8, 9, 10, 7, 89, 21, 91, 92]
n = len(nums)
nums.sort()
count = 0
last_smaller = float("-inf")
longest = 0
for i in range(0, n):
    num = nums[i]
    if num-1 == last_smaller:
        count += 1
        last_smaller = num
    elif num != last_smaller:
        count = 1
        last_smaller = num
    longest = max(longest, count)
print(longest)

'''
TC -> O(N log(N) + N)
SC -> O(1)
'''
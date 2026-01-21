nums = [13, 42, 55, 56, 78, 90, 102, 450]
n = len(nums)
is_sorted = True
for i in range(0, n-1):
    if nums[i] > nums[i+1]:
        is_sorted = False
        break
        
print(is_sorted)

'''
TC -> O(N)
SC -> O(1)
'''

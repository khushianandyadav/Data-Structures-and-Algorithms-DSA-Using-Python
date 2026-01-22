nums = [55, 32, 97, -55, 45, 32, 88, 21, 93]
nums.sort()
n = len(nums)
print(nums[n-2])

'''
TC -> O(N log N)
SC -> O(1) ....stack space is ignored

Why O(n log n)? (Intuition)
1️⃣ Divide and conquer → log n

Timsort (like merge sort) repeatedly splits the array into smaller pieces and merges them back.

Each split halves the data → log n levels

Similar to merge sort’s recursion depth

2️⃣ Linear work at each level → n

At every level of merging:

All n elements are visited once

Merging is a linear-time operation

3️⃣ Total time
Work per level = O(n)
Number of levels = O(log n)

Total = O(n log n)
'''
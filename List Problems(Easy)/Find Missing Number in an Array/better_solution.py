nums = [9, 6, 4, 2, 3, 5, 8, 0, 1]

n = len(nums)
freq = {}

for i in range(0, n+1):
    freq[i] = 0


for num in nums:
    freq[num] = 1

for k, v in freq.items():
    if v == 0:
        print(k)


'''
each for loop runs at TC O(N)
so TC->O(3N) similar to O(N)
SC-> O(N) --for dictionary
'''
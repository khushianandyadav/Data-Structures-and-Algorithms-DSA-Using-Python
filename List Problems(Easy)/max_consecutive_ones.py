#Leetcode 485


#You will be given a list consisting of 1s and 0s and you have to return how many times 
#maximum no of 1s have occurred consecutively in the list.

nums = [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1]

count = 0
max_count = 0

for i in range(0, len(nums)):
    if nums[i] == 1:
        count += 1

    else:
        max_count = max(max_count, count)
        count = 0

print(max(max_count, count))


# TC -> O(N)
# SC -> O(1)
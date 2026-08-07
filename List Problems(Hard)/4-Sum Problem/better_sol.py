nums = [1, 0, -1, 5, -2, 2, 0, 9]
def fourSum(nums):
    target = 0
    n = len(nums)
    my_set = set()
    for i in range(0, n):
        for j in range(i+1, n):
            hash_set = set()
            for k in range(j+1, n):
                fourth = target - (nums[i] + nums[j] + nums[k])
                if fourth in hash_set:
                    t = [nums[i], nums[j], nums[k], fourth]
                    t.sort()
                    my_set.add(tuple(t))
                hash_set.add(nums[k])

    result = []
    for ans in my_set:
        result.append(list(ans))
    return result


print(fourSum(nums))

#TC -> O(N^3)
#SC -> O(N)
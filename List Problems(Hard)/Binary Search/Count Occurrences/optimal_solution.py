
nums = [1, 2, 3, 3, 3, 3, 3, 5, 6, 8, 9, 9, 10]
target = 3

def lowerBound(nums, target):
    n = len(nums)
    lb = -1
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid-1
        else:
            low = mid+1
    return lb
    
def upperBound(nums, target):
    n = len(nums)
    ub = n
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid-1
        else:
            low = mid+1
    return ub


def countOccur(nums, target):
    lb = lowerBound(nums, target)
    if lb == -1:
        return 0
    ub = upperBound(nums, target)
    #return ub-lb
    print(ub-lb)
    
countOccur(nums, target)


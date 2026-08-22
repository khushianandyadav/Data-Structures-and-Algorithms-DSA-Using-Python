# 1) Identify the sorted part.
# 2) Check if target is in sorted part.

nums = [17, 18, 20, 1, 3, 4, 5, 7, 8, 10, 11, 13, 14, 16]
target = 4

def search(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high) // 2
        if nums[mid] == target:
            print(mid)
        if nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return -1


search(nums, target)
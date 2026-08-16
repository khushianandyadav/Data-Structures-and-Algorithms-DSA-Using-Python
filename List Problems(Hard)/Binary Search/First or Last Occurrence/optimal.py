nums = [1, 2, 3, 3, 3, 3, 3, 5, 6, 8, 9, 9, 10]
target = 3
class Solution:
    def lowerBound(self,nums, target):
        n = len(nums)
        lb = -1
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb
    
    def upperBound(self, nums, target):
        n = len(nums)
        ub = -1
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub
    
    def searchRange(self, nums, target):
        lb = self.lowerBound(nums, target)
        if lb == -1:
            print([-1, -1])
            return

        ub = self.upperBound(nums, target)
        print([lb, ub-1])

obj = Solution()
obj.searchRange(nums, target)
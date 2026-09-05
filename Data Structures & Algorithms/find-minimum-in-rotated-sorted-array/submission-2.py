class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1

        res = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = (left+right) // 2
            res = min(res, nums[mid]) # Because we will move the pointer away from the mid, so we have to keep checking
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return res
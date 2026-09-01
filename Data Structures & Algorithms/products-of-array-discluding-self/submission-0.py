class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        1, 2, 8, 48
        48, 48, 24, 6

        prefix = []
        suffix = []

        presum = 1
        for n in nums:
            presum *= n
            prefix.append(presum)
        
        suffsum = 1
        for i in range(len(nums)-1, -1, -1):
            suffsum *= nums[i]
            suffix.insert(0, suffsum)
        
        ans = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                ans[i] = suffix[i+1]
            elif i == len(nums)-1:
                ans[i] = prefix[i-1]
            else:
                ans[i] = suffix[i+1] * prefix[i-1]
        return ans


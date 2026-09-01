class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        ans = []
        s = set()
        for i in range(len(nums)-2):
            j, k = i + 1, n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    if (nums[i], nums[j], nums[k]) not in s:
                        ans.append([nums[i], nums[j], nums[k]])
                        s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        return ans
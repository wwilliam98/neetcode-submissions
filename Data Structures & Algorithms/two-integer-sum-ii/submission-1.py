class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range(n):
            other_target = target - numbers[i]
            low, high = i + 1, n - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == other_target:
                    return [i+1, mid+1]
                elif numbers[mid] > other_target:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1
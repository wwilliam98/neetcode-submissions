class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        left, right = 1, max(piles)

        ans = right
        while left <= right:
            rate = (left + right) // 2

            time_needed = 0
            for p in piles:
                time_needed += math.ceil(p/rate)
            
            if time_needed <= h:
                ans = rate
                right = rate - 1
            else:
                left = rate + 1
        return ans
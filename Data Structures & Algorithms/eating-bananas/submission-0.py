class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            rate = (left + right) // 2

            total_hour = 0
            for p in piles:
                total_hour += math.ceil(p/rate)

            if total_hour <= h:
                res = rate
                right = rate - 1
            else:
                left = rate + 1
        return res
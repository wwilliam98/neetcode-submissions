class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                prev, prev_i = stack.pop()
                ans[prev_i] = i-prev_i
            stack.append((t, i))
        return ans
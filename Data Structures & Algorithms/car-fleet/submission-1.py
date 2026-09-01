class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_s = [(p, s) for p, s in zip(position, speed)]
        p_s.sort()
        steps_needed = [(target-p)/s for p, s in p_s]

        stack = []
        for s in steps_needed:
            while stack and stack[-1] <= s:
                stack.pop()
            stack.append(s)
        return len(stack)
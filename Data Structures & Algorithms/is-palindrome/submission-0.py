class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        print(s)
        p1, p2 = 0, len(s)-1
        while p1 <= p2:
            if s[p1] != s[p2]:
                return False
            else:
                p1 += 1
                p2 -= 1
        return True
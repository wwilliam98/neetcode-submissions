class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapp = [0] * 26
        for e in s:
            mapp[ord(e)-97] += 1

        for e in t:
            mapp[ord(e)-97] -= 1

        return mapp == [0] * 26
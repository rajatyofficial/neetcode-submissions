class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # edge cases

        if len(s) == len(set(s)):
            return len(s)

        max_l = 0
        unique = set()
        l=0
        r=0

        while l<=r and r<len(s):

            if s[r] not in unique:
                unique.add(s[r])
                r+=1
                max_l = max(max_l,len(unique))
            else:
                unique.remove(s[l])
                l+=1
        return max_l
        return max_l 
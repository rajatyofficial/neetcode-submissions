class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0 # Left pointer (equivalent to your 'i')
        max_freq = 0 # Tracks the most frequent character in the current window

        for r in range(len(s)): # Right pointer (equivalent to your 'j')
            # Add the current character to our frequency map
            count[s[r]] = count.get(s[r], 0) + 1
            
            # Update the max frequency found so far in the current window
            max_freq = max(max_freq, count[s[r]])

            # Check if the current window is invalid
            # Window length is (r - l + 1)
            if (r - l + 1) - max_freq > k:
                # The window is invalid, so shrink it from the left
                count[s[l]] -= 1
                l += 1
            
            # Update the max length found so far
            res = max(res, r - l + 1)
        
        return res
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, it can't be a substring
        if len(s1) > len(s2):
            return False
            
        s1_count = [0] * 26
        window_count = [0] * 26
        
        # Populate the frequency array for s1
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1
            
        # Slide a window over s2
        for i in range(len(s2)):
            # Add the new character on the right side of the window
            window_count[ord(s2[i]) - ord('a')] += 1
            
            # If our window has exceeded the length of s1, 
            # remove the character that fell out on the left side
            if i >= len(s1):
                left_char_index = ord(s2[i - len(s1)]) - ord('a')
                window_count[left_char_index] -= 1
                
            # If the frequency arrays match, we found a permutation!
            if s1_count == window_count:
                return True
                
        return False
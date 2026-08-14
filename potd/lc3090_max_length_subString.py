class Solution:
    def maximumLengthSubstring(self, s: str) -> int: 
        freq = {}
        i = 0
        max_length = 0
        
        for j in range(len(s)):
            freq[s[j]] = freq.get(s[j], 0) + 1
            
            while freq[s[j]] > 2:
                freq[s[i]]-=1
                i+=1
                
            max_length=max(max_length,j-i+1)
            
        return max_length
from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        
        i = 0
        max_length = 0
        max_freq = 0

        for j in range(len(s)):
            count[s[j]] += 1

            max_freq = max(max_freq, count[s[j]])

            # Characters that need to be replaced
            replacements = (j - i + 1) - max_freq

            if replacements > k:
                count[s[i]] -= 1
                i += 1

            max_length = max(max_length, j - i + 1)

        return max_length
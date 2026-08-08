class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
       
        n, m = len(word1), len(word2)
        
        # last_match[j] will store the earliest possible index in word1 
        # from the right side that can match the suffix word2[j:]
        last_match = [-1] * (m + 1)
        last_match[m] = n
        
        # Step 1: Precompute from right to left
        w1_idx = n - 1
        for w2_idx in range(m - 1, -1, -1):
            while w1_idx >= 0 and word1[w1_idx] != word2[w2_idx]:
                w1_idx -= 1
            if w1_idx >= 0:
                last_match[w2_idx] = w1_idx
                w1_idx -= 1 # Move left for the next character
            else:
                break
                
        ans = []
        w2_idx = 0
        modified = False
        
        # Step 2: Greedily build the sequence from left to right
        for w1_idx in range(n):
            if w2_idx == m:
                break
                
            # Case 1: Characters match perfectly
            if word1[w1_idx] == word2[w2_idx]:
                ans.append(w1_idx)
                w2_idx += 1
            # Case 2: Mismatch, but we can safely skip/modify this character
            elif not modified and last_match[w2_idx + 1] > w1_idx:
                ans.append(w1_idx)
                w2_idx += 1
                modified = True # Consume our one-time modification limit
                
        return ans if len(ans) == m else []
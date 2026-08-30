from collections import Counter

def makeLargestPalindrome(s: str, target: str) -> str:
    n = len(s)
    count = Counter(s)
    
    # Step 1: Check if a palindrome is possible
    odd_chars = [char for char, freq in count.items() if freq % 2 != 0]
    if len(odd_chars) > 1:
        return ""
        
    mid_char = odd_chars[0] if odd_chars else ""
    if mid_char:
        count[mid_char] -= 1
        
    # Reduce frequencies for the left half
    half_count = {char: freq // 2 for char, freq in count.items() if freq // 2 > 0}
    half_len = n // 2
    
    # Helper for backtracking/DFS to find the smallest valid half string > target's first half
    def dfs(index, current_half, is_greater):
        if index == half_len:
            # Construct full palindrome
            left = "".join(current_half)
            candidate = left + mid_char + left[::-1]
            return candidate if candidate > target else ""
            
        # Try characters from 'a' to 'z'
        for char in sorted(half_count.keys()):
            if half_count[char] > 0:
                if not is_greater and char < target[index]:
                    continue
                
                # Prune if we are equal to target prefix and next char is smaller than target[index]
                if not is_greater and char == target[index]:
                    match_greater = False
                else:
                    match_greater = True
                    
                half_count[char] -= 1
                current_half.append(char)
                
                res = dfs(index + 1, current_half, is_greater or match_greater)
                if res:
                    return res
                    
                current_half.pop()
                half_count[char] += 1
                
        return ""

    return dfs(0, [], False)

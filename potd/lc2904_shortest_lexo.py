class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, ch in enumerate(s) if ch == '1']

        # Not enough 1s
        if len(ones) < k:
            return ""

        best_start = -1
        best_len = float('inf')

        # Every k consecutive 1s gives one possible shortest substring
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]

            length = end - start + 1

            if length < best_len:
                best_len = length
                best_start = start

            elif length == best_len:
                candidate = s[start:end + 1]
                best = s[best_start:best_start + best_len]

                if candidate < best:
                    best_start = start

        return s[best_start:best_start + best_len]
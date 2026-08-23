class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        mid=n//2 

         # Calculate initial sums and count '?' for both halves
        left_sum = sum(int(c) for c in num[:mid] if c != '?')
        right_sum = sum(int(c) for c in num[mid:] if c != '?')

        left_q = num[:mid].count('?')
        right_q = num[mid:].count('?')

        # Calculate the differences
        sum_diff = left_sum - right_sum
        q_diff = right_q - left_q

        # Bob wins if and only if the question mark difference 
        # can perfectly compensate for the sum difference.
        # Every pair of Bob's '?' can neutralize a sum difference of 9.
        return not (q_diff % 2 == 0 and sum_diff == (q_diff // 2) * 9)

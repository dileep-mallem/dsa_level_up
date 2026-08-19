class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int: # type: ignore
        rows ={}
        count=0 
        

        for row , seat in reservedSeats :
                rows[row] = rows.get(row, 0) | (1 << (seat - 1))

        ans=(n-len(rows))*2
        # Masks for:
        # left   = seats 2-5
        # middle = seats 4-7
        # right  = seats 6-9
        left = 0b000011110
        middle = 0b001111000
        right = 0b111100000

        for reserved in rows.values():
            if (reserved & left )==0 and (reserved & right )==0:
                ans+=2
            elif (reserved & left) == 0 or (reserved & middle) == 0 or (reserved & right) == 0:
                ans += 1

        return ans 
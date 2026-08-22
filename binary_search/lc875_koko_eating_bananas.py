import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k=(no of Banaseas eaten)//hours  , range(1,max(piles))
        # time =piles//k 

        def finish_time(k) :
            time=sum(math.ceil(pile/k) for pile in piles)
            return time<=h
        s=1;e=max(piles)
        while s<e :
            mid=s+(e-s)//2 
            if finish_time(mid) :
                e=mid
            else :
                s=mid+1
        return s

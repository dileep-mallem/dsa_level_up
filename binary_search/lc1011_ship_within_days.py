import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def can_load(k):
            current_weight=0
            days_used=1
            for i in weights :
                current_weight+=i
                if current_weight > k :
                    days_used+=1
                    current_weight=i
            return days_used<=days


        # Weight Range  (max(weights,sum(weights))
        low=max(weights)
        high=sum(weights)

        while low<high :
            mid=low+(high-low)//2 

            if can_load(mid) :
                high=mid
            else :
                low=mid+1
        return low

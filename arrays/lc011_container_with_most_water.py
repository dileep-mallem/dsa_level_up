# Topic : Two Pointers 
#TC : O(n) SC:O(1) 
#Diff : Med 

class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height) - 1
        max_area =0 

        while l < r :  
            width = r - l 
            area = min([height[l],height[r]]) * width 

            if area >= max_area :
                max_area=area 

            if height[l] < height[r] : 
                l+=1 
            else  : # if greater r-=1 , if equal either one can move so itwits
                r-=1
                 
        return max_area
# s=Solution()
# print(s.maxArea([1,8,6,2,5,4,8,3,7]))
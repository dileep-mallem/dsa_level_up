# Topic : Two Pointers 
#TC : O(n) SC:O(1) 
#Diff : Med 

class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1
        max_area=0
        while l < r :
            width = r - l 
            area=width * min(height[l],height[r])

            if area > max_area :
                max_area=area 
            if height[l] < height[r] :
                l+=1
            else :
                r-=1


        return max_area
s=Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
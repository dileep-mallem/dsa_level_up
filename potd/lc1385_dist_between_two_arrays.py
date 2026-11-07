class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        result=0
        f=1
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    f=0
                    break 
            if f==1:
                result +=1
            elif f==0:
                f=1
        return result 
                   
              
                
                
                
                    
            
                    
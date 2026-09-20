class Solution:
    def reverseDegree(self, s: str) -> int:
        # ord('z)-ord(ch) + 1 * i+1 


        result=0 

        for i in range(len(s)) : 
            result += (ord('z')-ord(s[i])+1) * (i+1)   
        return result    

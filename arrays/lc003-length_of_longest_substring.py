class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        # If char appear in Str again , then  moves left pointer to to max(j,d[s[j]+1]) -> d[s[j]] + 1 (most) , change the last Occurence index of char ,  lenght = j-i+1 
        d={}
        n=len(s)
        max_length=0
        
        i=0
        j=0

        while j < n :
            if s[j] in d : 
                i=max(i,d[s[j]]+1) # **
                d[s[j]]=j
            else :
                d[s[j]]=j
            max_length=max(max_length,j-i+1)
            j+=1
        return max_length
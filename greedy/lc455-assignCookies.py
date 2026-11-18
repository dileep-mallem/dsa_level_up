class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:

        def assignCookies(greedy , size) : 
            n=len(greedy)
            m=len(size)

            greedy.sort()
            size.sort()
            l,r=0,0

            while l<m and r<n:
                if greedy[r]<=size[l]:
                    r+=1
                l+=1
            return r
        
        return assignCookies(g,s)
        
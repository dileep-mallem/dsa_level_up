from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d=defaultdict(list)
       # Values : List of word
        for word in strs :
            key="".join(sorted(word)) # Key : Sorted Word 
            d[key].append(word)
        return d.values() # O(nk logk) k=abvg word length 

        # for word in strs :
        #     count=[0]*26 
        #     for ch in word :
        #         count[ord(ch)-ord('a')]+=1
        #     key=tuple(count) # list cant be key (they are mutable)
        #     d[key].append(word)
        # return d.values()

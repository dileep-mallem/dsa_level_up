#Strings , Think Edge Cases , No need for seprate condns for Continue 

class Solution(object):
    def longestCommonPrefix(self, strs):
        s=strs[0]
        r=""
        if strs==[]:
            return ""
        elif len(strs)==1 :
            return s
        else :
            for i in range(0,len(s)):
                for j in range(1,len(strs)):
                    if i < len(strs[j]) :
                        if s[i] != strs[j][i] : #char mismatch
                            return s[0:i]  
                    else :
                        return s[0:i]
            return s
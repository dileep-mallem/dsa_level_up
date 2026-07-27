class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map={')':'(',']':'[','}':'{'}                                                                 
        stack=[]
        for ch in s :
            if ch in map :
                top=stack.pop() if stack else '#'
                if top!=map[ch]:
                    return False     
            else : 
                stack.append(ch)
        return len(stack)==0 
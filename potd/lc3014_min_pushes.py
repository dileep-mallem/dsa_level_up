class Solution(object):
    def minimumPushes(self, word):
        #String has all distint ( for 0-7 push=1 and then 8-15 =2 , so on till 25)
        
        n=len(word)
        total=0
        for i in range(n):
            total+= (i//8) + 1 
        return total 
       
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        if n//10==0 :
            return False

        sum=0
        prod=1
        orig=n
        while n!=0 :
            a=n%10
            sum+= a 
            prod *= a 
            n=n//10

        return True if orig%(sum+prod)==0 else False   

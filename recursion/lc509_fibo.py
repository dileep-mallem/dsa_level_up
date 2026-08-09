class Solution:
    def fib(self, n: int) -> int:
        # F(n) = F(n-1) + F(n-1) BC : F(0) = 0 and F(1) = 1

        # def f(n) : 
        #     if n==0 or n==1 :
        #         return n
        #     else : 
        #         return f(n-1) + f(n-2)
        
        # return f(n)
        if n <= 1:
            return n
        
        # Track the two previous terms
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
            
        return b

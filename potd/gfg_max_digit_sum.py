class Solution:
    def findMax(self, n):
        # code here
        
        # Brute : 
        
        # result=n
        # r=float('-inf')
        # for j in range(1,n+1) :
        #     summ=0
        #     i=j
        #     while i!=0 :
        #         summ+=i%10
        #         i=i//10 
        #     if summ > r :
        #         r=summ
        #         result=j
        #     if summ==r :
        #         result=max(j,result)
        # return result
        
        # Helper function to easily compute the sum of digits
        def get_digit_sum(num: int) -> int:
            return sum(int(digit) for digit in str(num))

        # Base case: start with the number itself as the best candidate
        best_num = n
        max_sum = get_digit_sum(n)
        
        s = str(n)
        
        # Explore shifting each digit position down by 1 and filling the rest with 9s
        for i in range(len(s)):
            if s[i] == '0':
                continue
            
            # Form the candidate using clean string slicing
            prefix = s[:i]
            decreased_digit = str(int(s[i]) - 1)
            suffix = '9' * (len(s) - i - 1)
            
            # Combine components and convert to integer (automatically drops leading zeros)
            candidate = int(prefix + decreased_digit + suffix)
            candidate_sum = get_digit_sum(candidate)
            
            # Update the best candidate found so far
            if candidate_sum > max_sum:
                max_sum = candidate_sum
                best_num = candidate
            elif candidate_sum == max_sum:
                best_num = max(best_num, candidate)
                
        return best_num

                
            
                
            

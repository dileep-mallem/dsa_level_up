class Solution:
    def countSubarray(self, arr: list[int], l: int, r: int) -> int:
        # code here
        # BRute
        
        # n=len(nums)   TC : O(n**2)
        # count=0 
        # for i in range(n):
        #     for j in range(i,n):
        #         if l<=sum[i:j+1]<=r :
        #             count+=1
        # return count

        #  Optimal : Dyanamic Sliding Window O(n)
        # countSA <=r - countSA<=l-1 
            def countSA(k) :
            
                if k < 0 :
                    return 0
                    
                i=0
                total=0
                ans=0
                
                for j in range(len(arr)) :
                    total+=arr[j]
                    
                    while total>k and i<=j :
                        total-=arr[i]
                        i+=1
                        
                    ans+=(j-i+1)
                        
                return ans
            return countSA(r) - countSA(l-1)
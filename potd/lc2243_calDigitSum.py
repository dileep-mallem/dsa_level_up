class Solution:
    def digitSum(self, s: str, k: int) -> str:

        

        while len(s) > k :
            temp=[] 
            i=0
            while i<len(s) : 
                # Python slicing also safely handles going past the end of a string, so you don't even need the if (i+k) > n check).
                chunk=s[i:i+k]
                chunk_sum=sum(int(digit) for digit in chunk)

                temp.append(str(chunk_sum))
                i+=k 

            s="".join(temp)
        
        return s
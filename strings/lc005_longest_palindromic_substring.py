class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
            
        start, end = 0, 0
        n=len(s)
        def exp_center(left ,right : int) : 
            while left >=0 and right < n and s[left]==s[right] : 
                left-=1
                right+=1
            return right-left-1
        for i in range(n) : 
            # For odd Palindomres (one center )
            len1=exp_center(i,i)

            # FOr odd(two Centres)
            len2=exp_center(i,i+1)

            max_len=max(len1,len2)

            if max_len > (end-start+1) : 
                start=i-(max_len-1)//2
                end=i+max_len//2
        return s[start:end+1]
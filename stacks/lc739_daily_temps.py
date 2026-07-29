# Monotonic Stacks , med , Did brute , Bottled up Optimal(did but had some mistakes)

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n=len(temperatures)

        # BRUTE

        # l=0
        # result=[0]*n
        # for i in range(l+1,n):
        #     while i < n :
        #         if temperatures[i] > temperatures[l] :
        #             length=i-l
        #             result[l]=length 
        #             break 
        #         i+=1
        #     l+=1
        # return result

        # Using Stacks 
        stack=[] # Stores indices
        result=[0]*n
        for i in range(n):
            while stack  and temperatures[i] > temperatures[stack[-1]]:
                prev_index=stack.pop()
                result[prev_index]=i-prev_index
            stack.append(i)
        return result
            
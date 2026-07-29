class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        stack=[] # Strod index of Previous Greater Element 
        stack.append(nums[0])
        result=[-1]*n
        for i in range(n):
            l=i+1
            while l < n :
                if nums[l] > stack[-1]:
                    # stack.pop()
                    stack.append(nums[l])
                if nums[l] > nums[i] :
                    result[i]=nums[l]
                    i+=1
                    break
                l+=1
            # if nums[i] < nums[stack[-1]] :
            #     result[i]=nums[stack[-1]]
            for j in stack :
                if j > nums[i] :
                    result[i]=j
                    break
        return result


        #  for i in range(2 * n):
        #     idx = i % n
        #     while stack and nums[stack[-1]] < nums[idx]:
        #         prev_idx = stack.pop()
        #         result[prev_idx] = nums[idx]
        #     if i < n:  # only push indices during the first pass
        #         stack.append(idx)

        # return result
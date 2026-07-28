class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1=len(nums1)
        n2=len(nums2)
        result=[-1]*n1
        pos={}
        for i in range(n2):
            pos[nums2[i]]=i

        for i in range(n1) :
            # j=nums2.index(nums1[i]) + 1 # O(n) each time
            j=pos[nums1[i]]+1 # O(1) 
            while j < n2 :

                if nums2[j] > nums1[i]:
                    result[i]=nums2[j]
                    break
                j+=1
        return result
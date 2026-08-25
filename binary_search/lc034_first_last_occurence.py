class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # Lower Bound (First Occurence)
        def lower(a,key) :
            s=0
            e=len(a)-1
            result=-1
            while s <= e : 
                mid = s + (e-s)//2 
                if a[mid]==key :
                    result=mid 
                    e=mid-1
                elif a[mid]<key :
                    s=mid+1
                else :
                    e=mid-1
            return result
        
        # For Upper Bound  ( Last Occurence)

        def upper(a,key) :
            s=0
            e=len(a)-1
            result=-1

            while s<=e :
                mid= s+(e-s)//2
                if a[mid]==key :
                    result=mid 
                    s=mid+1
                elif a[mid]>key:
                    e=mid-1
                else :
                    s=mid+1
            return result 

        return [lower(nums,target),upper(nums,target)]

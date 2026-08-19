class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int: # type: ignore
        # Binary Search 

        # Lower Bound = smallest Index where arr[ind] >= target 

        def search(arr,key) :
            n=len(arr)
            ans=n 

            s=0
            e=n-1

            while s<=e :
                mid=s+(e-s)//2 

                if arr[mid]>=key :
                    ans=mid 
                    e=mid-1
                else :
                    s=mid+1
            return ans 
        return search(nums,target)
        
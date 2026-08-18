class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search is Performed in Sorted Array 
        # Iterative 
        # def search(arr, key ) :
        #     start , end = 0 , len(arr)-1
        #     while start <= end :
        #         mid = start + (end - start ) //2  
        #         if arr[mid]==key :
        #             return mid 
        #         elif arr[mid] <  key :
        #             start = mid + 1
        #         else :
        #             end = mid -1 
        #     return -1 
        # return search(nums , target)

        # recursive Approach 
        def s2(arr, s, e,key): 
            if s <= e :
                mid = s + (e-s)//2
                if arr[mid]==key :
                    return mid 
                if arr[mid] < key :
                    return s2(arr,mid+1,e,key)
                if arr[mid] > key :
                    return s2(arr,s,mid-1,key)
            return -1 
        return s2(nums,0,len(nums)-1,target)
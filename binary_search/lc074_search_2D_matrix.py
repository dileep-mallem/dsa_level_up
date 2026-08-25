class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        arr=matrix
        m=len(arr)
        n=len(arr[0])
        start=0
        end=(m*n)-1
        while start <= end  :

            mid=start + (end-start)//2 
            mid_value=arr[mid//n][mid%n]
            if mid_value==target :
                return True 
            elif mid_value < target :
                start=mid+1 
            else :
                end=mid-1
        return False

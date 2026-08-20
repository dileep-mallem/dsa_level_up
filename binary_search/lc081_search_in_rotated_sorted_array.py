class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        def search(arr , key ):
            low=0
            high=len(arr)-1
            while low<=high :
                mid=low + (high-low)//2

                if arr[mid]==key :
                    return True    
                # Handle duplicates
                if nums[low]==nums[mid]==nums[high]:
                    low += 1
                    high -= 1
                    continue
               
                if arr[low]<=arr[mid] :
                    if arr[low] <= key < arr[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1 
                else :
                    if arr[mid] < key <= arr[high]:
                        low = mid + 1
                    else:
                        high = mid - 1
            return False

        return search(nums,target)

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n=max(nums)
        result=0
        for i in nums : 
            result += abs(i-n)
        return result
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        result=[]

        for v in matrix : 
            result.append(v.count(1))
        return result
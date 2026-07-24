# Difficulty : Easy
# Pattern    : Brute force (nested loop)
# Time: O(n²)   Space: O(1)
# Date: 2026-07-18 | Attempts: 1
# Revisit: Yes — redo in Week 4 with hash map
# ─────────────────────────────────────

# FIRST INSTINCT:
# Check every pair — if they sum to target, return indices
# Didnt think of membership operators



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Logic
        result=[]
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if (nums[i]+nums[j])==target and i!=j and i not in result and j not in result :
                    result.append(i)
                    result.append(j)
        return result 




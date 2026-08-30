class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        indexed_nums = sorted((num, i) for i, num in enumerate(nums))
        
        groups = []
        for num, idx in indexed_nums:
            if not groups or num - groups[-1][-1][0] > limit:
                groups.append([(num, idx)])
            else:
                groups[-1].append((num, idx))
                
        res = [0] * len(nums)
        for group in groups:
            values = sorted([num for num, idx in group])
            indices = sorted([idx for num, idx in group])
            
            for val, idx in zip(values, indices):
                res[idx] = val
                
        return res

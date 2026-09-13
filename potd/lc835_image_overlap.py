class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int: # type: ignore
        
        # Get coordinates of all 1s in both images
        list1 = [(r, c) for r, row in enumerate(img1) for c, val in enumerate(row) if val == 1]
        list2 = [(r, c) for r, row in enumerate(img2) for c, val in enumerate(row) if val == 1]
        
        # Dictionary to count frequencies of shift vectors
        shift_counts = {}
        max_overlap = 0
        
        # Calculate the shift vector for every pair of 1s
        for r1, c1 in list1:
            for r2, c2 in list2:
                shift = (r2 - r1, c2 - c1)
                shift_counts[shift] = shift_counts.get(shift, 0) + 1
                if shift_counts[shift] > max_overlap:
                    max_overlap = shift_counts[shift]
                    
        return max_overlap

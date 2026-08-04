# Covers PSE,NSE , BEst , HArd , Must Had Depth Knowlwdge aboout The 
class Solution(object):
    def largestRectangleArea(self, heights):
        # Brute : Nestedd Loops , Check Evrey Possibilty TC : ~O(n**2)

        # n=len(heights)
        # max_area=heights[0]

        # for i in range(n):
        #     for j in range(i,n):
        #         width = j - i + 1
        #         area = width * min(heights[i:j+1])
        #         if area > max_area  :
        #             max_area = area 
       
        # return max_area

    #   2. brute force idea in plain words: for every single bar, find its nearest shorter neighbor on the left(PSE), and its nearest shorter neighbor on the right(NSE). The rectangle width for that bar is the gap between those two boundaries.
    #  and Compute for every bar , and return max  TC L O(5n) Pse : O(2n) NSE : O(2n) looop O(n) Sc : O(4n)

    # Optimal # O(2n)

        # st=[]
        # max_area=0
        # n=len(heights)
        # for i in range(n) :
        #     while st and heights[st[-1]] > heights[i] :
        #         element = st.pop()
        #         nse = i
        #         pse = st.pop() if st else -1

        #         max_area=max(max_area,element * (nse - pse -1))
        #     st.append(i)
        # # If ELemnt were Reamin in Stadk 
        # while st :
        #     element = heights[st[-1]]
        #     nse = n # Imaginary Index
        #     pse = st.pop() if st else -1 
        #     max_area=max(max_area,element * (nse - pse -1))
        # return max_area


        stack = []  # storesindices,
        max_area = 0
        n = len(heights)
        for i in range(n + 1):
            current_height = heights[i] if i < n else 0 # img nse 
            while stack and heights[stack[-1]] >= current_height:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)
        return max_area
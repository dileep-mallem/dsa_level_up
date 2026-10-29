class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        n=len(image)
        m=len(image[0])

        start_color=image[sr][sc]
        if start_color == color:
            return image
        # We should the Connected compoenet of Strating Pixel 

        def dfs(row,col) : 
            if not (0 <= row < n and 0 <= col < m) or image[row][col] != start_color:
                return

            image[row][col]=color

            dfs(row - 1, col)  # Up
            dfs(row + 1, col)  # Down
            dfs(row, col - 1)  # Left
            dfs(row, col + 1)  # Right

        
        

        dfs(sr,sc)
        return image

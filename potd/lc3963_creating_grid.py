class Solution:
    def createGrid(self, m: int, n: int) -> list[str]: 
        
        right,down=(0,1),(1,0)

        grid=[['#']*n for _ in range(m)] #O(m*n)
        grid[0][0]='.'
        flag=0

        i,j=0,0
        while i<m-1 or j<n-1 : #O(m+n)
                #  Handle the boundaries first:
                if i==m-1 : # bottom edge
                    j+=1 
                elif j==n-1 : # right edge
                    i+=1 
                else :
                    if flag==0 :
                        j+=1
                        flag=1
                    else :
                        i+=1
                        flag=0 
                grid[i][j]='.'

        # list of lists to list of strings
        return ["".join(row) for row in grid] # O(m*n)

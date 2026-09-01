from collections import deque
class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        
        m=len(classroom)
        n=len(classroom[0])
        max_energy = energy  # Save initial energy
        start_row,start_col=0,0

        # Finding Staring Pos  and liiters pos's
        litter_positions=[]
        for i in range(m) : 
            for j in range(n) : 
                if classroom[i][j]=='S' : 
                    start_row,start_col=i,j
                elif classroom[i][j]=='L' :
                    litter_positions.append((i, j))
        total_litter = len(litter_positions)
        

        # Target mask means all litter bits are set to 1 (e.g., if 3 litters, 111 in binary = 7)
        target_mask = (1 << total_litter) - 1 
        
        # Map each (r, c) of litter to its unique bit ID
        litter_id = {pos: i for i, pos in enumerate(litter_positions)}
        
        # 2. Queue stores: (row, col, current_energy, collected_litter_mask, total_moves)
        queue = deque([(start_row, start_col, max_energy, 0, 0)])
        
        # 3. Visited set keeps track of (row, col, current_energy, collected_litter_mask)
        # to avoid processing the exact same scenario multiple times
        visited = {(start_row, start_col, max_energy, 0)}
        
        # Direction offsets for Up, Down, Left, Right
        row_offsets = [-1, 1, 0, 0]
        col_offsets = [0, 0, -1, 1]
        
        while queue:
            r, c, energy, mask, moves = queue.popleft()
            
            # If we have collected all litter, return the moves immediately
            if mask == target_mask:
                return moves
                
            # If out of energy, we cannot move further from this state
            if energy == 0:
                continue
                
            # Explore all 4 adjacent directions
            for i in range(4):
                nr, nc = r + row_offsets[i], c + col_offsets[i]
                
                # Boundary check and Obstacle check
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_energy = energy - 1
                    next_mask = mask
                    
                    # If the next cell is a Reset station, recharge fully
                    if classroom[nr][nc] == 'R':
                        next_energy = max_energy
                        
                    # If the next cell is Litter, collect it if not already done
                    if classroom[nr][nc] == 'L':
                        lit_id = litter_id[(nr, nc)]
                        next_mask |= (1 << lit_id)
                        
                    # If this state hasn't been seen before, mark it visited and queue it
                    state = (nr, nc, next_energy, next_mask)
                    if state not in visited:
                        visited.add(state)
                        queue.append((nr, nc, next_energy, next_mask, moves + 1))
                        
        return -1

    
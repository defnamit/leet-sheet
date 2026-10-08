from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start_r, start_c = -1, -1
        litter_positions = []
        
        # Parse grid to find start and litter locations
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_positions.append((r, c))
                    
        total_litter = len(litter_positions)
        target_mask = (1 << total_litter) - 1
        
        # Quick check if there is no litter to collect initially
        if total_litter == 0:
            return 0

        # Map each litter cell to its bit index
        litter_map = {pos: i for i, pos in enumerate(litter_positions)}
        
        # Initial mask check if student starts directly on a litter position
        initial_mask = 0
        if (start_r, start_c) in litter_map:
            initial_mask |= (1 << litter_map[(start_r, start_c)])
            
        if initial_mask == target_mask:
            return 0

        # BFS Queue: (r, c, current_energy, mask)
        queue = deque([(start_r, start_c, energy, initial_mask)])
        
        # Visited set: (r, c, current_energy, mask)
        visited = set([(start_r, start_c, energy, initial_mask)])
        
        moves = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            for _ in range(len(queue)):
                r, c, cur_energy, mask = queue.popleft()
                
                # If out of energy, student cannot make a move from this cell
                if cur_energy == 0:
                    continue
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Boundary check and obstacle check
                    if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                        cell = classroom[nr][nc]
                        
                        # Energy calculation after move
                        if cell == 'R':
                            nxt_energy = energy  # Fully restored
                        else:
                            nxt_energy = cur_energy - 1
                        
                        # Bitmask calculation after move
                        nxt_mask = mask
                        if cell == 'L':
                            litter_idx = litter_map[(nr, nc)]
                            nxt_mask |= (1 << litter_idx)
                        
                        # Check goal condition
                        if nxt_mask == target_mask:
                            return moves + 1
                        
                        # Push to queue if not visited
                        next_state = (nr, nc, nxt_energy, nxt_mask)
                        if next_state not in visited:
                            visited.add(next_state)
                            queue.append(next_state)
                            
            moves += 1
            
        return -1

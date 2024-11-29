import numpy as np
from collections import deque

class find_path:
    def __init__(self):
        self.DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def bfs(self, grid, start, goal):
        """BFS algorithm to find the shortest path in a grid"""
        grid = np.array(grid)
        rows, cols = grid.shape
        
        # Initialize queue for BFS (with starting node)
        queue = deque([start])
        
        # Set to track visited nodes to avoid revisiting them
        visited = np.zeros_like(grid, dtype=bool)
        visited[start] = True
        
        # Dictionary to track the path (came_from)
        came_from = np.full((rows, cols, 2), -1, dtype=int)
        
        # Start BFS loop
        while queue:
            current = queue.popleft()
            
            # If we reach the goal, reconstruct the path
            if grid[current[0]][current[1]] == '=':
                path = []
                while current != start:
                    path.append(current)
                    current = tuple(came_from[current[0], current[1]])
                path.append(start)
                return path[::-1]  # Return the path from start to goal
            
            # Explore the neighbors
            for direction in self.DIRECTIONS:
                neighbor = (current[0] + direction[0], current[1] + direction[1])
                
                # Skip out-of-bound or blocked cells
                if not (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols):
                    continue
                if grid[neighbor] == 1 or visited[neighbor]:
                    continue
                
                # Mark the neighbor as visited and add it to the queue
                visited[neighbor] = True
                queue.append(neighbor)
                came_from[neighbor[0], neighbor[1]] = current
    
        return None  # If no path is found
    

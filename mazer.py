import numpy as np

class maze:
    def __init__(self):
        pass
    
    def find_char_indices(self, matrix, chart):
        indices = []
        for i, row in enumerate(matrix):
            for j, char in enumerate(row):
                if char == chart:
                    indices.append((i, j))
        return indices
    
    def find_min_index(self, lst):
        if not lst:
            raise ValueError("The list is empty.")
        return lst.index(min(lst))

    def calculate_distances(self, matrix, target_index):
        target_row, target_col = target_index
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        # Create a distance matrix
        distance_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                # Calculate Manhattan distance
                distance_matrix[i][j] = np.sqrt((i - target_row)*(i - target_row) + (j - target_col)*(j - target_col))

        return np.array(distance_matrix)
    
    def visual(self, grid, solution):
        print(grid)
        grid = np.array(grid)
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i][j] == '=':grid[i][j] = int(0)
                if grid[i][j] == '#':grid[i][j] = int(1)
                if grid[i][j] == 'A':grid[i][j] = int(2) 
                
        grid[solution[-1][0]][solution[-1][1]] = int(3)
   
        return grid
    
    def action(self, sol, start):
        curr = start
        actions = []
        for i in range(len(sol)):
            if sol[i][0]-curr[0] > 0: 
                print("guney git") 
                actions.append("Guneye Git")
            if sol[i][0]-curr[0] < 0: 
                print("kuzey git")
                actions.append("Kuzeye Git")
            if sol[i][1]-curr[1] > 0: 
                print("dogu git")
                actions.append("Doguya Git")
            if sol[i][1]-curr[1] < 0: 
                actions.append("Batiya Git")
                print("bati git")
            curr = sol[i]
        return actions
    
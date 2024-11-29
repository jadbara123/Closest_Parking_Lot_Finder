import visual
import find
import mazer
import matrix

a_star = find.find_path()
maze_master = mazer.maze()
mat = matrix.matrix()
if __name__ == "__main__":
    goal = maze_master.find_char_indices(mat, '=')[0]
    start = maze_master.find_char_indices(mat, 'A')[0]
    #print(goal)
    distance_matrix = maze_master.calculate_distances(mat, goal)
    #print(distance_matrix)
    sol = a_star.bfs(mat, start, goal)
    #print(sol)
    grid = maze_master.visual(mat, sol)
    #print(grid)
    actions = maze_master.action(sol, start)
    grid_display = visual.GridDisplay(actions, sol, grid)
    if len(grid) == 0:
        grid_display.display_error_message()
    else:
        grid_display.run()  # Start the game loop
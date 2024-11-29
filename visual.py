import pygame 

class GridDisplay:
    def __init__(self, actions, sol, grid, cell_size=50):
        """Initialize the grid display."""
        self.grid = grid
        self.cell_size = cell_size
        self.grid_rows, self.grid_cols = grid.shape
        self.screen_width = self.grid_cols * self.cell_size+200
        self.screen_height = self.grid_rows * self.cell_size+len(sol)*40
        self.actions = actions

        # Define colors
        self.colors = {
            '0': (0, 255, 0),     # Green for 0
            '1': (255, 0, 0),     # Red for 1
            '2': (255, 255, 0),   # Yellow for 2
            '3': (0, 0, 255),     # Blue for 3
            'default': (255, 255, 255)  # White for other values
        }
        # Set up f
        # Set up the display
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Grid Display")

    def display_error_message(self, message="no valid lot"):
        """Display an error message in red."""
        # Define text color (red)
        text_color = (255, 0, 0)
        
        # Set up font
        font = pygame.font.SysFont('Arial', 36)
        
        # Create the text surface
        text_surface = font.render(message, True, text_color)
        
        # Get the text rectangle to center the message on the screen
        text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        
        # Fill the screen with white background
        self.screen.fill((255, 255, 255))
        
        # Draw the text on the screen
        self.screen.blit(text_surface, text_rect)
        
        # Update the display
        pygame.display.flip()
        # Initialize Pygame
        pygame.init()

        # Set up the display
        self.screen = pygame.display.set_mode((600, 400))  # Window size (600x400)
        pygame.display.set_caption("Error Message Display")

        # Main loop to keep the window open
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Display the error message

    def draw_grid(self):
        """Draw the grid on the pygame screen."""
        for row in range(self.grid_rows):
            for col in range(self.grid_cols):
                value = self.grid[row, col]
                color = self.colors.get(value, self.colors['default'])  # Default to white for unknown values
                pygame.draw.rect(self.screen, color, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))
                pygame.draw.rect(self.screen, (255, 255, 255), (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size), 1)  # Grid lines

    def draw_legend(self, actions):
        """Draw the legend on the screen."""
        legend_x = self.grid_cols * self.cell_size + 20  # Position for the legend
        legend_y = 50
        act_y = self.grid_rows * self.cell_size + 20  # Position for the actions
        act_x = 50
        
        # Define legend labels and corresponding colors
        legend_items = [
            ('Dolu Park', self.colors['1']),  # Red for 1
            ('Bos Park', self.colors['0']),  # Green for 0
            ('Start', self.colors['2']),   # Yellow for 2
            ('En Yakin', self.colors['3'])   # Blue for 3
        ]
        
        # Draw legend items
        for idx, (label, color) in enumerate(legend_items):
            # Draw the color box for the legend
            pygame.draw.rect(self.screen, color, (legend_x, legend_y + idx * 40, 30, 30))  # Color box
            # Render the text for the legend
            font = pygame.font.SysFont('Arial', 18)
            label_text = font.render(label, True, (255, 255, 255))  # Black text
            self.screen.blit(label_text, (legend_x + 40, legend_y + idx * 40))  # Position the text
        
        for idx, (label) in enumerate(actions):
            # Draw the color box for the legend
            font = pygame.font.SysFont('Arial', 18)
            label_text = font.render(label, True, (255, 255, 255))  # Black text
            self.screen.blit(label_text, (act_x, act_y+idx * 30))  # Position the text
    
    def update(self):
        """Update the display."""
        self.screen.fill((0, 0, 0))  # Fill the background with black
        self.draw_grid() 
        self.draw_legend(self.actions)            # Draw the grid
        pygame.display.flip()        # Update the display

    def run(self):
        """Main game loop to keep the window open and handle events."""
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.update()  # Update the grid display

        pygame.quit()

# main.py

import pygame  # Import the pygame library for visualization
import sys  # Import sys for exiting the program
from kruskal_maze import KruskalMaze  # Import the KruskalMaze class for generating the maze

# Movement directions for visualization (down and right)
dx = [1, 0]
dy = [0, 1]

# Define the size of the maze grid
rows, cols = 30, 30

# Create a KruskalMaze instance with the specified number of rows and columns
kruskal_maze = KruskalMaze(rows, cols)

# Generate the maze using Kruskal's algorithm and get the minimum spanning tree (MST)
mst = kruskal_maze.generate_maze()

# Visualize the MST and get the required grid and edge states for rendering
list_mst, check_list = kruskal_maze.visualize_maze(mst)

# Initialize pygame for visualization
pygame.init()

# Define the screen size for rendering the maze
width, height = 800, 800
screen = pygame.display.set_mode((width, height))  # Create a display window
pygame.display.set_caption("Maze Visualization")  # Set the window title
screen.fill((28, 28, 28))  # Fill the background with a dark color

# Define the color for drawing the maze
white = (255, 255, 255)

# Set the spacing ratio between grid points
ratio = 20

# Set the initial offset for drawing the maze
init_x, init_y = 50, 50

# Draw the maze grid based on the MST data
for i in range(rows + 1):  # Loop through all rows in the grid
    for j in range(cols + 1):  # Loop through all columns in the grid
        x, y = init_x + j * ratio, init_y + i * ratio  # Calculate the coordinates of the current point
        for k in range(2):  # Loop through movement directions (right and down)
            new_x = i + dx[k]
            new_y = j + dy[k]
            # Check if the edge exists in the MST and draw the line if necessary
            if 0 <= new_x <= rows and 0 <= new_y <= cols and list_mst.get((i, j, new_x, new_y), True):
                pygame.draw.line(screen, white, (x, y), (init_x + new_y * ratio, init_y + new_x * ratio), 2)

# Update the display to show the drawn maze
pygame.display.flip()

# Main event loop to keep the pygame window open
while True:
    for event in pygame.event.get():  # Process events
        if event.type == pygame.QUIT:  # If the user closes the window
            pygame.quit()  # Quit pygame
            sys.exit()  # Exit the program

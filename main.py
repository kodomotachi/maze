# main.py

import pygame
import sys
from kruskal_maze import KruskalMaze

# Movement directions
dx = [1, 0]
dy = [0, 1]

rows, cols = 30, 30
kruskal_maze = KruskalMaze(rows, cols)
mst = kruskal_maze.generate_maze()
list_mst, check_list = kruskal_maze.visualize_maze(mst)

pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Visualization")
screen.fill((28, 28, 28))

white = (255, 255, 255)
ratio = 20
init_x, init_y = 50, 50

for i in range(rows + 1):
    for j in range(cols + 1):
        x, y = init_x + j * ratio, init_y + i * ratio
        for k in range(2):
            new_x = i + dx[k]
            new_y = j + dy[k]
            if 0 <= new_x <= rows and 0 <= new_y <= cols and list_mst.get((i, j, new_x, new_y), True):
                pygame.draw.line(screen, white, (x, y), (init_x + new_y * ratio, init_y + new_x * ratio), 2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

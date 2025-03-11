import pygame
import sys
from kruskal_maze import KruskalMaze

pygame.init()
pygame.font.init()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(maze, start, end, path=[]):
    x, y = start
    if start == end:
        return path + [start]

    for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new_x, new_y = x + direction[0], y + direction[1]
        if (new_x, new_y) in maze and maze[(new_x, new_y)] is True and (new_x, new_y) not in path:
            new_path = dfs(maze, (new_x, new_y), end, path + [start])
            if new_path:
                return new_path

    return None

def draw_button(screen, text, rect, color=(0, 200, 0)):
    pygame.draw.rect(screen, color, rect)
    font = pygame.font.SysFont(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def is_button_clicked(rect, pos):
    return rect.collidepoint(pos)

width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Visualization")
screen.fill((28, 28, 28))

white = (255, 255, 255)
red = (255, 0, 0)

rows, cols = 30, 30
ratio = 20
init_x, init_y = 50, 50

kruskal_maze = KruskalMaze(rows, cols)
mst = kruskal_maze.generate_maze()
list_mst, check_list = kruskal_maze.visualize_maze(mst)

create_button_rect = pygame.Rect(50, 10, 150, 40)
solve_button_rect = pygame.Rect(220, 10, 150, 40)

running = True
solving_path = []
while running:
    screen.fill((28, 28, 28))

    for i in range(rows + 1):
        for j in range(cols + 1):
            x, y = init_x + j * ratio, init_y + i * ratio
            for k in range(2):
                new_x = i + dx[k]
                new_y = j + dy[k]
                if 0 <= new_x <= rows and 0 <= new_y <= cols and list_mst.get((i, j, new_x, new_y), True):
                    pygame.draw.line(screen, white, (x, y), (init_x + new_y * ratio, init_y + new_x * ratio), 2)

    if solving_path:
        for (px, py) in solving_path:
            px_coord = init_x + py * ratio + ratio // 2
            py_coord = init_y + px * ratio + ratio // 2
            pygame.draw.rect(screen, red, (px_coord, py_coord, ratio // 2, ratio // 2))

    draw_button(screen, "Create maze", create_button_rect)
    draw_button(screen, "Solve maze", solve_button_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if is_button_clicked(create_button_rect, event.pos):
                    kruskal_maze = KruskalMaze(rows, cols)
                    mst = kruskal_maze.generate_maze()
                    list_mst, check_list = kruskal_maze.visualize_maze(mst) # Cập nhật check_list
                    solving_path = []
                elif is_button_clicked(solve_button_rect, event.pos):
                    start = (0, 0)
                    end = (rows - 1, cols - 1)
                    solving_path = dfs(check_list, start, end)

                    if solving_path:
                        for (step_x, step_y) in solving_path:
                            pygame.time.delay(200)
                            screen.fill((28, 28, 28))
                            for i in range(rows + 1):
                                for j in range(cols + 1):
                                    x, y = init_x + j * ratio, init_y + i * ratio
                                    for k in range(2):
                                        new_x = i + dx[k]
                                        new_y = j + dy[k]
                                        if 0 <= new_x <= rows and 0 <= new_y <= cols and list_mst.get(
                                                (i, j, new_x, new_y), True):
                                            pygame.draw.line(screen, white, (x, y),
                                                             (init_x + new_y * ratio, init_y + new_x * ratio), 2)

                            current_px = init_x + step_y * ratio + ratio // 2
                            current_py = init_y + step_x * ratio + ratio // 2
                            pygame.draw.rect(screen, red, (current_px, current_py, ratio // 2, ratio // 2))
                            pygame.display.flip()

pygame.quit()
sys.exit()
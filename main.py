import pygame
import sys
import random # to shuffle array in python 

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw a Dot in Pygame")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Fill the screen with white
screen.fill((28, 28, 28))

# Draw a red dot at position (400, 300)
# pygame.draw.circle(screen, red, (400, 300), 2)  # (surface, color, position, radius)

# 150 with 15 unit

arr_check = []
dx = [16, 0, 0, -16]
dy = [0, 16, -16, 0]

# for i in range(0, 31, 2):
# 	for j in range(0, 31, 2):
# 		for k in range(4):	
# 			new_x = i + dx[k]
# 			new_y = j + dy[k]
			
# 			if (new_x >= 0 and new_y >= 0 and new_x < 31 and new_y < 31):	
# 				arr_check.append(((i, j), (new_x, new_y)));

# random.shuffle(arr_check)

# parent = {}

# for i in range(0, 31, 2):	
# 	for j in range(0, 31, 2):	
# 		parent[(i, j)] = (i, j)


# print(arr_check)

init_up_left_i = 55
init_up_left_j = 55
ratio = 20

# for i in range(31):
# 	for j in range(31):
# 		pygame.draw.circle(screen, white, (150 + i * 16, 100 + j * 16), 2) # to draw point in Pygame's window

for i in range(31):
	for j in range(31):
		for k in range(4):
			new_x = init_up_left_i + i * ratio + dx[k]
			new_y = init_up_left_j + j * ratio + dy[k]

			if (new_x >= init_up_left_i and new_x <= init_up_left_i + ratio * 30 and new_y >= init_up_left_j and new_y <= init_up_left_j + ratio * 30):
				pygame.draw.line(screen, white, (init_up_left_i + i * ratio, init_up_left_j + j * ratio), (new_x, new_y), 1)

# Update the display
pygame.display.flip()

# Main loop to keep the window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

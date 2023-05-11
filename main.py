# file made by savior
'''
Goals:
[x] mirror cursor through the middle
[x] mirror cursor 4 ways
[ ] reset button that clears screen
// or/and
[ ] trailing disappearing

'''
import pygame
import math
from random import randint
from settings import *

# Initialize Pygame
pygame.init()
# Set the size of the window

window = pygame.display.set_mode((WIDTH,HEIGHT))
# Set the title of the window
pygame.display.set_caption("Kaleidoscope Drawing")

# Set up the clock to control the frame rate
clock = pygame.time.Clock()

# Set up the colors to use for drawing
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the brush size
BRUSH_SIZE = 5

# Set up the drawing surface
drawing_surface = pygame.Surface((1000,800))
# Set up the current position of the mouse
current_mouse_pos = (0, 0)
# Set up the previous position of the mouse
previous_mouse_pos = (0, 0)
# Set up the flag for if the mouse button is held down
mouse_button_down = False

def mirror():
     if mouse_button_down:
        right2left = WIDTH - current_mouse_pos[0]
        left2right = (WIDTH/2 - current_mouse_pos[0]) + WIDTH/2
        bottom2top =  (HEIGHT - current_mouse_pos[1])
        top2bottom = (HEIGHT/2 - current_mouse_pos[1] + HEIGHT/2)
        drawingleft = current_mouse_pos[0] < WIDTH/2
        drawingright = current_mouse_pos[0] > WIDTH/2
        drawingtop = current_mouse_pos[1] < HEIGHT/2
        drawingbottom = current_mouse_pos[1] > HEIGHT/2
            
        pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)), current_mouse_pos, BRUSH_SIZE)

        # ---------------------------for drawing in the corners------------------------------
        # drawing on top right
        if drawingtop and drawingright:
            pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(right2left, top2bottom), BRUSH_SIZE)
            pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(right2left, current_mouse_pos[1]), BRUSH_SIZE)
            pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(current_mouse_pos[0], top2bottom), BRUSH_SIZE)

        # drawing on top left
        if drawingtop and drawingleft:
            pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(left2right, top2bottom), BRUSH_SIZE)
            pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(current_mouse_pos[0], top2bottom), BRUSH_SIZE)
            pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(left2right, current_mouse_pos[1]), BRUSH_SIZE)

        # drawing on bottom right
        if drawingbottom and drawingright:
            pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(right2left, bottom2top), BRUSH_SIZE)
            pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(current_mouse_pos[0], bottom2top), BRUSH_SIZE)
            pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(right2left, current_mouse_pos[1]), BRUSH_SIZE)

        # drawing on bottom left
        if drawingbottom and drawingleft:
            pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(left2right, bottom2top), BRUSH_SIZE)
            pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(left2right, current_mouse_pos[1]), BRUSH_SIZE)
            pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(current_mouse_pos[0], bottom2top), BRUSH_SIZE)


        
# Main game loop
running = True
while running:
 # Handle events
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_button_down = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_button_down = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    BRUSH_SIZE -= 1
                elif event.key == pygame.K_UP:
                    BRUSH_SIZE += 1
                elif event.key == pygame.K_1:
                    BRUSH_SIZE = 10
                elif event.key == pygame.K_2:
                    BRUSH_SIZE = 20
                elif event.key == pygame.K_3:
                    BRUSH_SIZE = 30

 # Get the current position of the mouse
    current_mouse_pos = pygame.mouse.get_pos()

 # Draw on the drawing surface
    mirror()

 # Clear the screen
    window.fill(BLACK)
 # Blit the drawing surface to the screen
    window.blit(drawing_surface, (0, 0))
 # Update the screen
    pygame.display.update()

 # Cap the frame rate
clock.tick(FPS)
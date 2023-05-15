# file made by savior
'''
Goals:
[x] mirror cursor through the middle
[x] mirror cursor 4 ways
[ ] reset button that clears screen
// or/and
[ ] trailing disappearing
[ ] single color mode
[ ] 2 or 4 axis mode

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
fourway = True


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
        if fourway:
            if drawingtop and drawingright:
                pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(right2left, top2bottom), BRUSH_SIZE)
                pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(right2left, current_mouse_pos[1]), BRUSH_SIZE)
                pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(current_mouse_pos[0], top2bottom), BRUSH_SIZE)

            # drawing on top left
            if drawingtop and drawingleft:
                pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(left2right, top2bottom), BRUSH_SIZE)
                pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(left2right, current_mouse_pos[1]), BRUSH_SIZE)
                pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(current_mouse_pos[0], top2bottom), BRUSH_SIZE)

            # drawing on bottom right
            if drawingbottom and drawingright:
                pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(right2left, bottom2top), BRUSH_SIZE)
                pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(right2left, current_mouse_pos[1]), BRUSH_SIZE)
                pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(current_mouse_pos[0], bottom2top), BRUSH_SIZE)

            # drawing on bottom left
            if drawingbottom and drawingleft:
                pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(left2right, bottom2top), BRUSH_SIZE)
                pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(left2right, current_mouse_pos[1]), BRUSH_SIZE)
                pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(current_mouse_pos[0], bottom2top), BRUSH_SIZE)
        if fourway == False:
            if drawingright:
                pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(right2left, current_mouse_pos[1]), BRUSH_SIZE)
            if drawingleft:
                pygame.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(left2right, current_mouse_pos[1]), BRUSH_SIZE)

# Main game loop
running = True
while running:
 # handle events
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
                if event.key >= pygame.K_0 and event.key <= pygame.K_9:
                    # Get the integer value from the key
                    key_value = event.key - pygame.K_0
                    # Update count
                    count = key_value * 10
                    BRUSH_SIZE = count
                if event.key == pygame.K_c:
                    drawing_surface.fill(BLACK)
                if event.key == pygame.K_2 and pygame.K_LCTRL:
                    fourway = False
                if event.key == pygame.K_4 and pygame.K_LCTRL:
                    fourway = True
                if event.key == pygame.K_MINUS:
                    zoom_out()

 # get the current position of the mouse
    current_mouse_pos = pygame.mouse.get_pos()

 # call mirror funciton
    mirror()

 # Clear the screen
    window.fill(BLACK)
 # Blit the drawing surface to the screen
    window.blit(drawing_surface, (0, 0))
 # Update the screen
    pygame.display.update()

 # Cap the frame rate
clock.tick(FPS)


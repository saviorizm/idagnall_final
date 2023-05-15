# file made by savior
'''
Goals:
[x] mirror cursor through the middle
[x] mirror cursor 4 ways
[x] reset button that clears screen
// or/and
[ ] trailing disappearing
[ ] single color mode
[x[] 2 or 4 axis mode
[x] controls screen

'''
import pygame
import math
from random import randint
from settings import *
import os

# Initialize Pygame
pygame.init()
# Set the size of the window
window = pygame.display.set_mode((WIDTH,HEIGHT))
# Set the title of the window
pygame.display.set_caption("Kaleidoscope Drawing")
# Set up the clock to control the frame rate
clock = pygame.time.Clock()
# asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
#  load images
code_keybinds_image = pygame.image.load(os.path.join(img_folder, "code_keybinds.jpg")).convert()
code_keybinds_rect = code_keybinds_image.get_rect()

# variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
fourway = True
BRUSH_SIZE = 5
show_keybinds = False

# Set up the drawing surface
drawing_surface = pygame.Surface((1000,800))
# Set up the current position of the mouse
current_mouse_pos = (0, 0)
# Set up the previous position of the mouse
previous_mouse_pos = (0, 0)
# Set up the flag for if the mouse button is held down
mouse_button_down = False
def toggle_keybind_screen():
    global show_keybinds
    show_keybinds = not show_keybinds    

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
                    key_value = event.key - pygame.K_0
                    count = key_value * 10
                    BRUSH_SIZE = count
                if event.key == pygame.K_c:
                    drawing_surface.fill(BLACK)
                if event.key == pygame.K_t:
                    fourway = False
                if event.key == pygame.K_f:
                        fourway = True
                if event.key == pygame.K_ESCAPE:
                    toggle_keybind_screen()
                

 # get the current position of the mouse
    current_mouse_pos = pygame.mouse.get_pos()

 # call mirror funciton
    mirror()
    # keybind_screen()

 # Clear the screen
    window.fill(BLACK)
 # Blit the drawing surface to the screen
    window.blit(drawing_surface, (0, 0))
    if show_keybinds:
        window.blit(code_keybinds_image, code_keybinds_rect)
 # Update the screen
    pygame.display.update()

 # Cap the frame rate
clock.tick(FPS)


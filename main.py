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
import pygame as pg
from random import randint
from settings import *
import os
from time import time

# Initialize pg
pg.init()
# Set the size of the window
window = pg.display.set_mode((WIDTH,HEIGHT))
# Set the title of the window
pg.display.set_caption("Kaleidoscope Drawing")
# Set up the clock to control the frame rate
clock = pg.time.Clock()
# asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
#  load images
code_keybinds_image = pg.image.load(os.path.join(img_folder, "code_keybinds.jpg")).convert()
code_keybinds_rect = code_keybinds_image.get_rect()
# load music
pg.mixer.init()
pg.mixer.music.load("whitearmor-let_me_know.mp3")
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(.5)

# variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
fourway = True
BRUSH_SIZE = 5
show_keybinds = False
start_time = time()

# Set up the drawing surface
drawing_surface = pg.Surface((1000,800))
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
            
        # draws directly where the player is
        pg.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)), current_mouse_pos, BRUSH_SIZE)
        # ---------------------------for drawing in the corners------------------------------
        # if user drawing on top right
        if fourway:
            if drawingtop and drawingright:
                pg.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(right2left, top2bottom), BRUSH_SIZE)
                pg.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(right2left, current_mouse_pos[1]), BRUSH_SIZE)
                pg.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(current_mouse_pos[0], top2bottom), BRUSH_SIZE)

            # if user drawing on top left
            if drawingtop and drawingleft:
                pg.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(left2right, top2bottom), BRUSH_SIZE)
                pg.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(left2right, current_mouse_pos[1]), BRUSH_SIZE)
                pg.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(current_mouse_pos[0], top2bottom), BRUSH_SIZE)

            # if user drawing on bottom right
            if drawingbottom and drawingright:
                pg.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(right2left, bottom2top), BRUSH_SIZE)
                pg.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(right2left, current_mouse_pos[1]), BRUSH_SIZE)
                pg.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(current_mouse_pos[0], bottom2top), BRUSH_SIZE)

            # if user drawing on bottom left
            if drawingbottom and drawingleft:
                pg.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(left2right, bottom2top), BRUSH_SIZE)
                pg.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(left2right, current_mouse_pos[1]), BRUSH_SIZE)
                pg.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(current_mouse_pos[0], bottom2top), BRUSH_SIZE)
        if fourway == False:
            if drawingright:
                pg.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(right2left, current_mouse_pos[1]), BRUSH_SIZE)
            if drawingleft:
                pg.draw.circle(drawing_surface, (randint(0,255),randint(0,255),randint(0,255)),(left2right, current_mouse_pos[1]), BRUSH_SIZE)

# Main game loop
running = True
while running:
    running_time = time() - start_time
    if running_time < 4.0:
        window.blit(code_keybinds_image, code_keybinds_rect)
    else:
        show_keybinds = False
 # handle events
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    mouse_button_down = True
                elif event.type == pg.MOUSEBUTTONUP:
                    mouse_button_down = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        BRUSH_SIZE -= 1
                    if event.key >= pg.K_0 and event.key <= pg.K_9:
                        key_value = event.key - pg.K_0
                        count = key_value * 10
                        BRUSH_SIZE = count
                    if event.key == pg.K_c:
                        drawing_surface.fill(BLACK)
                    if event.key == pg.K_t:
                        fourway = False
                    if event.key == pg.K_f:
                            fourway = True
                    if event.key == pg.K_ESCAPE:
                        toggle_keybind_screen()
                
 # get the current position of the mouse
        current_mouse_pos = pg.mouse.get_pos()
 # call mirror funciton
        mirror()
 # Clear the screen
        window.fill(BLACK)
 # Blit the drawing surface to the screen
        window.blit(drawing_surface, (0, 0))
# keybind_screen()
        if show_keybinds:
            window.blit(code_keybinds_image, code_keybinds_rect)
 # Update the screen
    pg.display.update()

 # Cap the frame rate
clock.tick(FPS)


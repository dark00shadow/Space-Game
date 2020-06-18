# Imports
import pyglet
from pyglet.window import key
from pyglet.gl import *
import RectangleCollision
from random import randint
# Point variables
points = 0
# Paths
Path0 = 'Textures/'
Path1 = 'Textures/player/'
Path2 = 'Textures/blocks/'
Path3 = 'Textures/energy cell/'
# Create the window
window = pyglet.window.Window(caption='Space Game', width=600, height=600)
# Location of window to the middel of screen
window.set_location(window.screen.width//2-window.width//2, window.screen.height//2-window.height//2)
# Make it so images with transparent works
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
# Window icon to the icon
icon = pyglet.image.load(Path0+ 'icon.ico')
window.set_icon(icon)
# Changes the background
background = pyglet.image.load(Path0 + 'background1.png')
# To help with key stuff
KeyH = key.KeyStateHandler()
window.push_handlers(KeyH)
# Player object
class player():
    # For triger once
    key_pressed_once_W = 0
    key_pressed_once_S = 0
    key_pressed_once_A = 0
    key_pressed_once_D = 0
    # Direction
    direction = ''
    # For flip stuff
    flip = 'up'
    # Speed of player(kinda)
    speed = 2
    # Position of player
    posx = 300
    posy = 300
    # Image for player
    image = pyglet.image.load(Path1 + 'Player-Flip=Up.png')
# Block1 object
class block1():
    # Position x 1
    posx1 = 50
    # Position y 1
    posy1 = 460
    # Position x 2
    posx2 = 400
    # Position y 2
    posy2 = 100
    # Image for block1
    image = pyglet.image.load(Path2+ 'block1.png')
# Block2 object
class block2():
    # Position 1
    posx1 = 400
    posy1 = 460
    # Image for block2
    image = pyglet.image.load(Path2+ 'block2.png')
# Energy cell object(this is the goal)
class energy_cell():
    # Position
    posx = randint(100,500)
    posy = randint(100,500)
    # Image for energy cell
    image = pyglet.image.load(Path3+ 'energy cell.png')
# Label object(this is the point label)
class Label():
    posx = 500
    posy = 500
    # Label stuff for label
    label = pyglet.text.Label('points:' + str(points), x=posx,y=posy,color=(0, 0, 255, 255))
# Solid stuff for player and blocks(aka make it so the player cant go through blocks)
def solid(obj1x,obj1y,obj2x,obj2y,obj1w,obj1h,obj2w,obj2h):
    if RectangleCollision.collision.rectangle(energy_cell.posx,energy_cell.posy,obj2x,obj2y,18,28,obj2w,obj2h):
        energy_cell.posx = randint(200,400)
        energy_cell.posy = randint(200,400)
    if RectangleCollision.collision.rectangle(obj1x,obj1y,obj2x,obj2y,obj1w,obj1h,obj2w,obj2h):
        if player.direction == 'up': player.posy -= player.speed
        if player.direction == 'down': player.posy += player.speed
        if player.direction == 'left': player.posx += player.speed
        if player.direction == 'right': player.posx -= player.speed
# Update method
def Update1(dt):
    # Cant go outside of the screen
    if player.posx >= 572:
        player.posx -= player.speed
    if player.posx <= 1:
        player.posx += player.speed
    if player.posy >= 572:
        player.posy -= player.speed
    if player.posy <= 1:
        player.posy += player.speed
    # Solids
    solid(player.posx,player.posy,block1.posx1,block1.posy1,30,30,98,32)
    solid(player.posx,player.posy,block1.posx2,block1.posy2,30,30,98,32)
    solid(player.posx,player.posy,block2.posx1,block2.posy1,30,30,64,64)
    # Collision
    if RectangleCollision.collision.rectangle(energy_cell.posx,energy_cell.posy,player.posx,player.posy,18,28,30,30):
        global points
        points += 1
        energy_cell.posx = randint(100,500)
        energy_cell.posy = randint(100,500)
        Label.label = pyglet.text.Label('points:' + str(points), x=Label.posx,y=Label.posy,color=(0, 0, 255, 255))
    # Flip stuff
    if player.flip == 'up':
        player.image = pyglet.image.load(Path1 + 'Player-Flip=Up.png')
        flip = ''
    if player.flip == 'down':
        player.image = pyglet.image.load(Path1 + 'Player-Flip=Down.png')
        flip = ''
    if player.flip == 'left':
        player.image = pyglet.image.load(Path1 + 'Player-Flip=Left.png')
        flip = ''
    if player.flip == 'right':
        player.image = pyglet.image.load(Path1 + 'Player-Flip=Right.png')
        flip = ''
    # Movment
    # W
    if KeyH[key.W] and not KeyH[key.S] and not KeyH[key.D] and not KeyH[key.A]:
        player.direction = 'up'
        player.posy += player.speed
    # S
    if not KeyH[key.W] and KeyH[key.S] and not KeyH[key.D] and not KeyH[key.A]:
        player.direction = 'down'
        player.posy -= player.speed
    # A
    if not KeyH[key.W] and not KeyH[key.S] and not KeyH[key.D] and KeyH[key.A]:
        player.direction = 'left'
        player.posx -= player.speed
    # D
    if not KeyH[key.W] and not KeyH[key.S] and KeyH[key.D] and not KeyH[key.A]:
        player.direction = 'right'
        player.posx += player.speed
    # Flip Stuff
    # W
    if KeyH[key.W] and not KeyH[key.S] and not KeyH[key.D] and not KeyH[key.A] and player.key_pressed_once_W == 0:
        player.flip = 'up'
        player.key_pressed_once_W = 1
    if not KeyH[key.W] and player.key_pressed_once_W == 1:
        player.key_pressed_once_W = 0
    # S
    if not KeyH[key.W] and KeyH[key.S] and not KeyH[key.D] and not KeyH[key.A] and player.key_pressed_once_S == 0:
        player.flip = 'down'
        player.key_pressed_once_S = 1
    if not KeyH[key.S] and player.key_pressed_once_S == 1:
        player.key_pressed_once_S = 0
    # A
    if not KeyH[key.W] and not KeyH[key.S] and not KeyH[key.D] and KeyH[key.A] and player.key_pressed_once_A == 0:
        player.flip = 'left'
        player.key_pressed_once_A = 1
    if not KeyH[key.A] and player.key_pressed_once_A == 1:
        player.key_pressed_once_A = 0
    # D
    if not KeyH[key.W] and not KeyH[key.S] and KeyH[key.D] and not KeyH[key.A] and player.key_pressed_once_D == 0:
        player.flip = 'right'
        player.key_pressed_once_D = 1
    if not KeyH[key.D] and player.key_pressed_once_D == 1:
        player.key_pressed_once_D = 0
@window.event
def on_draw():
    # Clears the window
    window.clear()
    # Draw background
    background.blit(-100,-100)
    # Draw player
    player.image.blit(player.posx,player.posy)
    # Draw blocks
    block1.image.blit(block1.posx1,block1.posy1)
    block1.image.blit(block1.posx2,block1.posy2)
    block2.image.blit(block2.posx1,block2.posy1)
    # Draw energy cell
    energy_cell.image.blit(energy_cell.posx,energy_cell.posy)
    # Draw label
    Label.label.draw()
# for update1
pyglet.clock.schedule_interval(Update1, 1/120)
# idk its makes it work
pyglet.app.run()
import pyglet
from pyglet.window import key
from pyglet.gl import *
import RectangleCollision
Path0 = 'Textures/'
Path1 = 'Textures/player/'
window = pyglet.window.Window(caption='Space Jam 001 Game', width=600, height=600)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
background = pyglet.image.load(Path0 + 'background1.png')
KeyH = key.KeyStateHandler()
window.push_handlers(KeyH)
class player():
    key_pressed_once_W = 0
    key_pressed_once_S = 0
    key_pressed_once_A = 0
    key_pressed_once_D = 0
    W_S_A_D_are_pressed = 0
    flip = 'up'
    speed = 2
    posx = 300
    posy = 300
    image = pyglet.image.load(Path1 + 'Player-Flip=Up.png')
def Update1(dt):
    if player.posx >= 572:
        player.posx -= player.speed
    if player.posx <= 1:
        player.posx += player.speed
    if player.posy >= 572:
        player.posy -= player.speed
    if player.posy <= 1:
        player.posy += player.speed
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
        player.posy += player.speed
    # S
    if not KeyH[key.W] and KeyH[key.S] and not KeyH[key.D] and not KeyH[key.A]:
        player.posy -= player.speed
    # A
    if not KeyH[key.W] and not KeyH[key.S] and not KeyH[key.D] and KeyH[key.A]:
        player.posx -= player.speed
    # D
    if not KeyH[key.W] and not KeyH[key.S] and KeyH[key.D] and not KeyH[key.A]:
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
    window.clear()
    background.blit(-100,-100)
    player.image.blit(player.posx,player.posy)
pyglet.clock.schedule_interval(Update1, 1/120)
pyglet.app.run()
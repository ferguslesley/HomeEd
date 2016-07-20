
#Config File for Constants From
#SUPER Green-Tank MAX


from pygame import *


DEBUG = True
START_FPS = 30
MAX_FPS = 500
MIN_FPS = 15
FPS = START_FPS  # frames per second setting
fpsClock = time.Clock()
SCREEN_W = 800
SCREEN_H = 600
MAX_SPEED = 20
NORM_SPEED = 5
MIN_SPEED = 3
# set up the window
DISPLAYSURF = display.set_mode((SCREEN_W, SCREEN_H), 0, 32)
display.set_caption('SUPER TANK MAX')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
TankImgUp = image.load('TankSpriteForward.png', )
TankImgRight = image.load('TankSpriteRight.png', )
TankImgDown = image.load('TankSpriteBackwards.png', )
TankImgLeft = image.load('TankSpriteLeft.png', )
Tankx = 10
Tanky = 10
direction = 'right'
TankImg = TankImgRight
lasers = []
firing = False
MAXLASERS = 5
lastTime = 0
TankSpeed = NORM_SPEED
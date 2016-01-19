import pygame, sys
from pygame.locals import *

pygame.init()

pygame.mixer.init()

while True:
    soundObj = pygame.mixer.Sound('beep1.ogg')
    soundObj.play()
    import time
    time.sleep(1) # wait and let the sound play for 1 second
    soundObj.stop()

    keys = pygame.key.get_pressed()
    if keys[K_LCTRL]:
        pygame.quit()
        sys.exit()

        
        

    

    

# Import the pygame library and initialise the game engine
import pygame
pygame.init()

# Open a new window, captian it "Pong"
screen = pygame.display.set_mode ((700,500))
pygame.display.set_caption("Pong")

# here's the variable that runs our game loop
doExit = False

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#variables to hold paddle position        
#these go above game loop 
p1x = 1       
p1y = 200
p2x = 680
p2y = 200

#ball variables
bx = 350 #xposition
by = 250 #yposition

bVx = 5 #x velocity (horizontal speed)
bVy = 5 #y velocity (vetical speed) 
while not doExit: #GAME LOOP------------------------------------
    #ball movement
    bx += bVx
    by += bVy
    
    #reflect ball off side walls of sceen, change score
    if bx < 0: #this has been split up from right wall collision so we can increase scores
        bVx *= -1
        p2Score += 1 #python doesn't do ++ its DUMB 
    if bx < 0 or bx + 20 > 700:
        bVx *= -1
        
    if by < 0 or by + 20 > 500:
        bVy *= -1
        
    # event queue stuff---------------------
    clock.tick(60) #set the FPS
    
    for event in pygame.event.get(): #check if user did something
        if event.type == pygame.QUIT: #chrck if user clicked close
            doExit = True # Flag that we are done so we exit game loop
                 #game logic-------------------
    keys = pygame.key.get_pressed()      
    if keys[pygame.K_w]:
         p1y-=5
    if keys[pygame.K_s]:
         p1y+=5
    keys2 = pygame.key.get_pressed()      
    if keys2[pygame.K_UP]:
         p2y-=5
    if keys2[pygame.K_DOWN]:
        p2y+=5 
    
    #ball-paddle reflection
    if bx < p1x + 20 and by + 20 > p1y and by < p1y + 100:
        bVx *= -1
    if bx+20 > p2x and by + 20 > p2y and by < p2y + 100:
        bVx *= -1
         
              
    #render section will go here----------------
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 20, 100), 1)
    pygame.draw.rect(screen, (255, 255, 255), (p2x, p2y, 20, 100), 1)
 
    #draw a line down he middle
    pygame.draw.line(screen, (120, 140, 230), [349, 0], [349, 500], 10)
    pygame.draw.circle(screen, (200, 200, 0), (bx, by), 10)
    #update the screen
    pygame.display.flip()
    
     #display scores
    font = pygame.font.Font(None, 74) #use default font
    text = font.render(str(p1Score), 1, (255, 255, 255))
    screen.blit(text, (250, 10))
    text = font.render(str(p2Score), 1, (255, 255, 255))
    screen.blit(text, (420,10))

#END GAME LOOP---------------------------------------------------------
            
pygame.quit()#when game is done close down pygame 

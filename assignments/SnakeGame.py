#-------------------------------------------------------------------------------------------------------------#

#Remix of traditional snake game.
#Created with Python's Pygame package.
#Move with standard WASD and arrow key controls.
#This version of the snake game was modified from the tutorial posted by Syntec (on behalf of TheNewBoston.com)
#All modifications and changes are commented in-line below.

#-------------------------------------------------------------------------------------------------------------#

import pygame, time, random

pygame.init()

#Define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
blue = (0,0,155)

#Set display size, caption
display_width = 600
display_height  = 400
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

#Clock, globals
clock = pygame.time.Clock()
block_size = 10
FPS = 10
font = pygame.font.SysFont(None, 25)

#Draws the snakes
def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])
        
def snake2(block_size, snakelist2):
    for XnY in snakelist2:
        pygame.draw.rect(gameDisplay, blue, [XnY[0],XnY[1],block_size,block_size])

#Allows for message display
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

#Main loop
def gameLoop(FPS):

    #Constants
    gameExit = False
    gameOver = False
    FPS = 10

    lead_x = display_width/2
    lead_y = display_height/2

    lead2_x = display_width/2
    lead2_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    lead2_x_change = 0
    lead2_y_change = 0

    snakeList = []
    snakeLength = 1

    snakeList2 = []
    snakeLength2 = 1

    randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
    
    while not gameExit:
        
        #Quit screen message
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            #Quit screen key detection
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop(FPS)

        #Standard movement key detection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            #First snake
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    
                #Second Snake
                elif event.key == pygame.K_a:
                    lead2_x_change = -block_size
                    lead2_y_change = 0
                elif event.key == pygame.K_d:
                    lead2_x_change = block_size
                    lead2_y_change = 0
                elif event.key == pygame.K_w:
                    lead2_y_change = -block_size
                    lead2_x_change = 0
                elif event.key == pygame.K_s:
                    lead2_y_change = block_size
                    lead2_x_change = 0

        #Border detection
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        elif lead2_x >= display_width or lead2_x < 0 or lead2_y >= display_height or lead2_y < 0:
            gameOver = True
      
        #Calculates changes in movement
        lead_x += lead_x_change
        lead_y += lead_y_change

        lead2_x += lead2_x_change
        lead2_y += lead2_y_change

        #Draws apple
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size,block_size])

        #Defines the snakes
        #First Snake
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        #Second Snake
        snakeHead2 = []
        snakeHead2.append(lead2_x)
        snakeHead2.append(lead2_y)
        snakeList2.append(snakeHead2)

        #Snake lists
        if len(snakeList) > snakeLength:
            del snakeList[0]

        if len(snakeList2) > snakeLength2:
            del snakeList2[0]

        #Snake segment hit detection
        for eachSegment in snakeList [:-1]:
            if eachSegment == snakeHead:
                gameOver = True
            elif eachSegment == snakeHead2:
                snakeLength2 -=1

        for eachSegment2 in snakeList2 [:-1]:
            if eachSegment2 == snakeHead2:
                gameOver = True
            elif eachSegment2 == snakeHead:
                snakeLength -=1

        #Defines snakes
        snake(block_size, snakeList)
        snake2(block_size, snakeList2)

        #Wraps up the screen
        pygame.display.update()

        #Apple detection
        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
            randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
            snakeLength += 2
            FPS += 1

        elif lead2_x == randAppleX and lead2_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
            randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
            snakeLength2 += 2
            FPS += 1
        clock.tick(FPS)

    pygame.quit()
    quit()
gameLoop(FPS)

